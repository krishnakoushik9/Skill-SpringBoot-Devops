#!/usr/bin/env python3
"""
JMX Generator - Automatically generate JMeter test files from OpenAPI specifications.

WHAT:
    This script parses OpenAPI/Swagger specifications and generates corresponding
    JMeter (.jmx) test plan files for performance testing.

WHY:
    - Eliminates manual JMX file creation
    - Keeps performance tests synchronized with API definitions
    - Reduces human error in test configuration
    - Enables continuous performance testing in CI/CD pipelines

HOW:
    Single file:    python jmx_generator.py --spec <openapi.yaml> --output <output.jmx>
    All files:      python jmx_generator.py --spec-dir <specs_dir> --output-dir <jmx_dir>
    Watch mode:     python jmx_generator.py --spec-dir <specs_dir> --output-dir <jmx_dir> --watch
"""

import yaml
import json
import os
import sys
import argparse
import hashlib
import xml.etree.ElementTree as ET
from xml.dom import minidom
from datetime import datetime
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class APIEndpoint:
    """
    Represents a single API endpoint extracted from OpenAPI specification.
    
    WHAT: Data container for endpoint information
    WHY: Provides structured access to endpoint details for JMX generation
    """
    path: str
    method: str
    operation_id: str
    summary: str
    description: str
    tags: List[str]
    parameters: List[Dict[str, Any]]
    request_body: Optional[Dict[str, Any]]
    responses: Dict[str, Any]
    
    def get_sample_body(self) -> str:
        """Extract sample request body from the spec."""
        if not self.request_body:
            return ""
        
        content = self.request_body.get('content', {})
        json_content = content.get('application/json', {})
        
        if 'example' in json_content:
            return json.dumps(json_content['example'], indent=2)
        
        schema = json_content.get('schema', {})
        return self._generate_sample_from_schema(schema)
    
    def _generate_sample_from_schema(self, schema: Dict) -> str:
        """Generate sample JSON from schema definition."""
        if not schema:
            return "{}"
        
        sample = {}
        properties = schema.get('properties', {})
        
        for prop_name, prop_def in properties.items():
            prop_type = prop_def.get('type', 'string')
            
            if prop_type == 'string':
                if prop_def.get('format') == 'email':
                    sample[prop_name] = "test@example.com"
                elif prop_def.get('format') == 'uuid':
                    sample[prop_name] = "123e4567-e89b-12d3-a456-426614174000"
                elif prop_def.get('format') == 'date-time':
                    sample[prop_name] = datetime.now().isoformat()
                elif prop_def.get('format') == 'password':
                    sample[prop_name] = "password123"
                elif 'enum' in prop_def:
                    sample[prop_name] = prop_def['enum'][0]
                else:
                    sample[prop_name] = f"sample_{prop_name}"
            elif prop_type == 'integer':
                sample[prop_name] = prop_def.get('default', 1)
            elif prop_type == 'number':
                sample[prop_name] = prop_def.get('default', 1.0)
            elif prop_type == 'boolean':
                sample[prop_name] = prop_def.get('default', True)
            elif prop_type == 'array':
                sample[prop_name] = []
            elif prop_type == 'object':
                sample[prop_name] = {}
        
        return json.dumps(sample, indent=2)


@dataclass
class TestPlanConfig:
    """
    Configuration for JMeter test plan generation.
    
    WHAT: Settings that control how JMX files are generated
    WHY: Allows customization of thread counts, durations, and test behavior
    """
    name: str = "Generated Test Plan"
    num_threads: int = 10
    ramp_up_period: int = 60
    loop_count: int = 1
    duration: int = 300
    think_time_min: int = 1000
    think_time_max: int = 3000
    connect_timeout: int = 5000
    response_timeout: int = 30000
    include_assertions: bool = True
    include_listeners: bool = True
    group_by_tags: bool = True


class JMXGenerator:
    """
    Generates JMeter test plans from OpenAPI specifications.
    
    WHAT: Main engine that converts OpenAPI specs to JMX files
    WHY: Automates the creation of performance test files
    HOW: Parses OpenAPI YAML/JSON, extracts endpoints, builds JMeter XML structure
    """
    
    def __init__(self, config: Optional[TestPlanConfig] = None):
        self.config = config or TestPlanConfig()
        self.endpoints: List[APIEndpoint] = []
        self.servers: List[Dict[str, str]] = []
        self.api_info: Dict[str, str] = {}
        self.components: Dict[str, Any] = {}
    
    def parse_openapi_spec(self, spec_path: str) -> None:
        """
        Parse an OpenAPI specification file.
        
        WHAT: Reads and parses OpenAPI YAML or JSON file
        WHY: Extracts API information needed for JMX generation
        HOW: Uses yaml.safe_load with UTF-8 encoding to handle all characters
        """
        with open(spec_path, 'r', encoding='utf-8') as f:
            if spec_path.endswith(('.yaml', '.yml')):
                spec = yaml.safe_load(f)
            else:
                spec = json.load(f)
        
        self.api_info = spec.get('info', {})
        self.servers = spec.get('servers', [{'url': 'http://localhost:8080'}])
        self.components = spec.get('components', {})
        
        paths = spec.get('paths', {})
        for path, path_item in paths.items():
            for method in ['get', 'post', 'put', 'patch', 'delete', 'head', 'options']:
                if method in path_item:
                    operation = path_item[method]
                    endpoint = APIEndpoint(
                        path=path,
                        method=method.upper(),
                        operation_id=operation.get('operationId', f"{method}_{path}"),
                        summary=operation.get('summary', ''),
                        description=operation.get('description', ''),
                        tags=operation.get('tags', ['default']),
                        parameters=self._resolve_parameters(
                            path_item.get('parameters', []) + operation.get('parameters', [])
                        ),
                        request_body=self._resolve_request_body(operation.get('requestBody')),
                        responses=operation.get('responses', {})
                    )
                    self.endpoints.append(endpoint)
    
    def _resolve_parameters(self, parameters: List[Dict]) -> List[Dict]:
        """Resolve parameter references."""
        resolved = []
        for param in parameters:
            if '$ref' in param:
                ref_path = param['$ref'].split('/')[-1]
                param = self.components.get('parameters', {}).get(ref_path, param)
            resolved.append(param)
        return resolved
    
    def _resolve_request_body(self, request_body: Optional[Dict]) -> Optional[Dict]:
        """Resolve request body references."""
        if not request_body:
            return None
        if '$ref' in request_body:
            ref_path = request_body['$ref'].split('/')[-1]
            request_body = self.components.get('requestBodies', {}).get(ref_path, request_body)
        return request_body
    
    def generate_jmx(self, output_path: str) -> str:
        """
        Generate JMeter test plan XML.
        
        WHAT: Creates complete JMX file from parsed OpenAPI spec
        WHY: Produces ready-to-use JMeter test plan
        HOW: Builds XML structure with all JMeter elements
        """
        root = ET.Element('jmeterTestPlan', {
            'version': '1.2',
            'properties': '5.0',
            'jmeter': '5.6.3'
        })
        
        hash_tree = ET.SubElement(root, 'hashTree')
        test_plan = self._create_test_plan()
        hash_tree.append(test_plan)
        test_plan_tree = ET.SubElement(hash_tree, 'hashTree')
        
        self._add_user_defined_variables(test_plan_tree)
        self._add_http_defaults(test_plan_tree)
        self._add_header_manager(test_plan_tree)
        self._add_cookie_manager(test_plan_tree)
        self._add_cache_manager(test_plan_tree)
        
        if self.config.group_by_tags:
            self._add_endpoints_by_tag(test_plan_tree)
        else:
            self._add_single_thread_group(test_plan_tree)
        
        if self.config.include_listeners:
            self._add_listeners(test_plan_tree)
        
        xml_str = ET.tostring(root, encoding='unicode')
        pretty_xml = minidom.parseString(xml_str).toprettyxml(indent='  ')
        
        lines = pretty_xml.split('\n')
        lines = [line for line in lines if line.strip()]
        final_xml = '\n'.join(lines)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(final_xml)
        
        return output_path
    
    def _create_test_plan(self) -> ET.Element:
        """Create the main TestPlan element."""
        test_plan = ET.Element('TestPlan', {
            'guiclass': 'TestPlanGui',
            'testclass': 'TestPlan',
            'testname': self.config.name,
            'enabled': 'true'
        })
        
        self._add_string_prop(test_plan, 'TestPlan.comments', 
            f"Auto-generated from: {self.api_info.get('title', 'Unknown API')}\n"
            f"Version: {self.api_info.get('version', 'N/A')}\n"
            f"Generated: {datetime.now().isoformat()}")
        self._add_bool_prop(test_plan, 'TestPlan.functional_mode', False)
        self._add_bool_prop(test_plan, 'TestPlan.tearDown_on_shutdown', True)
        self._add_bool_prop(test_plan, 'TestPlan.serialize_threadgroups', False)
        
        elem_prop = ET.SubElement(test_plan, 'elementProp', {
            'name': 'TestPlan.user_defined_variables',
            'elementType': 'Arguments',
            'guiclass': 'ArgumentsPanel',
            'testclass': 'Arguments',
            'testname': 'User Defined Variables',
            'enabled': 'true'
        })
        ET.SubElement(elem_prop, 'collectionProp', {'name': 'Arguments.arguments'})
        
        self._add_string_prop(test_plan, 'TestPlan.user_define_classpath', '')
        
        return test_plan
    
    def _add_user_defined_variables(self, parent: ET.Element) -> None:
        """Add user-defined variables for configuration."""
        args = ET.SubElement(parent, 'Arguments', {
            'guiclass': 'ArgumentsPanel',
            'testclass': 'Arguments',
            'testname': 'User Defined Variables',
            'enabled': 'true'
        })
        
        collection = ET.SubElement(args, 'collectionProp', {'name': 'Arguments.arguments'})
        
        server_url = self.servers[0].get('url', 'http://localhost:8080') if self.servers else 'http://localhost:8080'
        
        from urllib.parse import urlparse
        parsed = urlparse(server_url)
        
        variables = {
            'PROTOCOL': parsed.scheme or 'http',
            'SERVER': parsed.hostname or 'localhost',
            'PORT': str(parsed.port or (443 if parsed.scheme == 'https' else 80)),
            'BASE_PATH': parsed.path.rstrip('/') or '',
            'THREADS': str(self.config.num_threads),
            'RAMP_UP': str(self.config.ramp_up_period),
            'DURATION': str(self.config.duration),
            'THINK_TIME_MIN': str(self.config.think_time_min),
            'THINK_TIME_MAX': str(self.config.think_time_max),
            'AUTH_TOKEN': '${__P(auth.token,)}',
        }
        
        for name, value in variables.items():
            elem = ET.SubElement(collection, 'elementProp', {
                'name': name,
                'elementType': 'Argument'
            })
            self._add_string_prop(elem, 'Argument.name', name)
            self._add_string_prop(elem, 'Argument.value', value)
            self._add_string_prop(elem, 'Argument.metadata', '=')
        
        ET.SubElement(parent, 'hashTree')
    
    def _add_http_defaults(self, parent: ET.Element) -> None:
        """Add HTTP Request Defaults."""
        defaults = ET.SubElement(parent, 'ConfigTestElement', {
            'guiclass': 'HttpDefaultsGui',
            'testclass': 'ConfigTestElement',
            'testname': 'HTTP Request Defaults',
            'enabled': 'true'
        })
        
        elem_prop = ET.SubElement(defaults, 'elementProp', {
            'name': 'HTTPsampler.Arguments',
            'elementType': 'Arguments',
            'guiclass': 'HTTPArgumentsPanel',
            'testclass': 'Arguments',
            'testname': 'User Defined Variables',
            'enabled': 'true'
        })
        ET.SubElement(elem_prop, 'collectionProp', {'name': 'Arguments.arguments'})
        
        self._add_string_prop(defaults, 'HTTPSampler.domain', '${SERVER}')
        self._add_string_prop(defaults, 'HTTPSampler.port', '${PORT}')
        self._add_string_prop(defaults, 'HTTPSampler.protocol', '${PROTOCOL}')
        self._add_string_prop(defaults, 'HTTPSampler.contentEncoding', 'UTF-8')
        self._add_string_prop(defaults, 'HTTPSampler.path', '')
        self._add_string_prop(defaults, 'HTTPSampler.concurrentPool', '6')
        self._add_string_prop(defaults, 'HTTPSampler.connect_timeout', str(self.config.connect_timeout))
        self._add_string_prop(defaults, 'HTTPSampler.response_timeout', str(self.config.response_timeout))
        
        ET.SubElement(parent, 'hashTree')
    
    def _add_header_manager(self, parent: ET.Element) -> None:
        """Add HTTP Header Manager with common headers."""
        manager = ET.SubElement(parent, 'HeaderManager', {
            'guiclass': 'HeaderPanel',
            'testclass': 'HeaderManager',
            'testname': 'HTTP Header Manager',
            'enabled': 'true'
        })
        
        collection = ET.SubElement(manager, 'collectionProp', {'name': 'HeaderManager.headers'})
        
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'Bearer ${AUTH_TOKEN}',
        }
        
        for name, value in headers.items():
            elem = ET.SubElement(collection, 'elementProp', {
                'name': '',
                'elementType': 'Header'
            })
            self._add_string_prop(elem, 'Header.name', name)
            self._add_string_prop(elem, 'Header.value', value)
        
        ET.SubElement(parent, 'hashTree')
    
    def _add_cookie_manager(self, parent: ET.Element) -> None:
        """Add HTTP Cookie Manager."""
        manager = ET.SubElement(parent, 'CookieManager', {
            'guiclass': 'CookiePanel',
            'testclass': 'CookieManager',
            'testname': 'HTTP Cookie Manager',
            'enabled': 'true'
        })
        
        ET.SubElement(manager, 'collectionProp', {'name': 'CookieManager.cookies'})
        self._add_bool_prop(manager, 'CookieManager.clearEachIteration', False)
        self._add_bool_prop(manager, 'CookieManager.controlledByThreadGroup', False)
        
        ET.SubElement(parent, 'hashTree')
    
    def _add_cache_manager(self, parent: ET.Element) -> None:
        """Add HTTP Cache Manager."""
        manager = ET.SubElement(parent, 'CacheManager', {
            'guiclass': 'CacheManagerGui',
            'testclass': 'CacheManager',
            'testname': 'HTTP Cache Manager',
            'enabled': 'true'
        })
        
        self._add_bool_prop(manager, 'clearEachIteration', True)
        self._add_bool_prop(manager, 'useExpires', True)
        self._add_bool_prop(manager, 'CacheManager.controlledByThreadGroup', False)
        
        ET.SubElement(parent, 'hashTree')
    
    def _add_endpoints_by_tag(self, parent: ET.Element) -> None:
        """Add thread groups organized by API tags."""
        tag_groups: Dict[str, List[APIEndpoint]] = {}
        for endpoint in self.endpoints:
            tag = endpoint.tags[0] if endpoint.tags else 'default'
            if tag not in tag_groups:
                tag_groups[tag] = []
            tag_groups[tag].append(endpoint)
        
        for tag, endpoints in tag_groups.items():
            self._add_thread_group(parent, f"{tag} Tests", endpoints)
    
    def _add_single_thread_group(self, parent: ET.Element) -> None:
        """Add a single thread group with all endpoints."""
        self._add_thread_group(parent, "API Tests", self.endpoints)
    
    def _add_thread_group(self, parent: ET.Element, name: str, endpoints: List[APIEndpoint]) -> None:
        """Add a thread group with specified endpoints."""
        thread_group = ET.SubElement(parent, 'ThreadGroup', {
            'guiclass': 'ThreadGroupGui',
            'testclass': 'ThreadGroup',
            'testname': name,
            'enabled': 'true'
        })
        
        self._add_string_prop(thread_group, 'ThreadGroup.on_sample_error', 'continue')
        
        loop_ctrl = ET.SubElement(thread_group, 'elementProp', {
            'name': 'ThreadGroup.main_controller',
            'elementType': 'LoopController',
            'guiclass': 'LoopControlPanel',
            'testclass': 'LoopController',
            'testname': 'Loop Controller',
            'enabled': 'true'
        })
        self._add_bool_prop(loop_ctrl, 'LoopController.continue_forever', False)
        self._add_string_prop(loop_ctrl, 'LoopController.loops', '-1')
        
        self._add_string_prop(thread_group, 'ThreadGroup.num_threads', '${THREADS}')
        self._add_string_prop(thread_group, 'ThreadGroup.ramp_time', '${RAMP_UP}')
        self._add_bool_prop(thread_group, 'ThreadGroup.scheduler', True)
        self._add_string_prop(thread_group, 'ThreadGroup.duration', '${DURATION}')
        self._add_string_prop(thread_group, 'ThreadGroup.delay', '0')
        self._add_bool_prop(thread_group, 'ThreadGroup.same_user_on_next_iteration', True)
        
        tg_tree = ET.SubElement(parent, 'hashTree')
        
        for endpoint in endpoints:
            self._add_http_sampler(tg_tree, endpoint)
            self._add_think_time(tg_tree)
    
    def _add_http_sampler(self, parent: ET.Element, endpoint: APIEndpoint) -> None:
        """Add an HTTP sampler for an endpoint."""
        sampler_name = f"{endpoint.method} {endpoint.path}"
        if endpoint.summary:
            sampler_name = f"{endpoint.summary} ({endpoint.method})"
        
        sampler = ET.SubElement(parent, 'HTTPSamplerProxy', {
            'guiclass': 'HttpTestSampleGui',
            'testclass': 'HTTPSamplerProxy',
            'testname': sampler_name,
            'enabled': 'true'
        })
        
        if endpoint.request_body and endpoint.method in ['POST', 'PUT', 'PATCH']:
            self._add_bool_prop(sampler, 'HTTPSampler.postBodyRaw', True)
            
            elem_prop = ET.SubElement(sampler, 'elementProp', {
                'name': 'HTTPsampler.Arguments',
                'elementType': 'Arguments'
            })
            collection = ET.SubElement(elem_prop, 'collectionProp', {'name': 'Arguments.arguments'})
            
            arg_elem = ET.SubElement(collection, 'elementProp', {
                'name': '',
                'elementType': 'HTTPArgument'
            })
            self._add_bool_prop(arg_elem, 'HTTPArgument.always_encode', False)
            self._add_string_prop(arg_elem, 'Argument.value', endpoint.get_sample_body())
            self._add_string_prop(arg_elem, 'Argument.metadata', '=')
        else:
            elem_prop = ET.SubElement(sampler, 'elementProp', {
                'name': 'HTTPsampler.Arguments',
                'elementType': 'Arguments',
                'guiclass': 'HTTPArgumentsPanel',
                'testclass': 'Arguments',
                'testname': 'User Defined Variables',
                'enabled': 'true'
            })
            collection = ET.SubElement(elem_prop, 'collectionProp', {'name': 'Arguments.arguments'})
            
            for param in endpoint.parameters:
                if param.get('in') == 'query':
                    arg_elem = ET.SubElement(collection, 'elementProp', {
                        'name': param['name'],
                        'elementType': 'HTTPArgument'
                    })
                    self._add_bool_prop(arg_elem, 'HTTPArgument.always_encode', True)
                    
                    schema = param.get('schema', {})
                    default_value = schema.get('default', '')
                    if schema.get('type') == 'integer':
                        default_value = str(default_value) if default_value else '1'
                    elif schema.get('type') == 'string':
                        default_value = default_value or f"${{{param['name'].upper()}}}"
                    
                    self._add_string_prop(arg_elem, 'Argument.value', str(default_value))
                    self._add_string_prop(arg_elem, 'Argument.metadata', '=')
                    self._add_bool_prop(arg_elem, 'HTTPArgument.use_equals', True)
                    self._add_string_prop(arg_elem, 'Argument.name', param['name'])
        
        path = endpoint.path
        for param in endpoint.parameters:
            if param.get('in') == 'path':
                param_name = param['name']
                path = path.replace(f"{{{param_name}}}", f"${{{param_name.upper()}}}")
        
        self._add_string_prop(sampler, 'HTTPSampler.path', '${BASE_PATH}' + path)
        self._add_string_prop(sampler, 'HTTPSampler.method', endpoint.method)
        self._add_bool_prop(sampler, 'HTTPSampler.follow_redirects', True)
        self._add_bool_prop(sampler, 'HTTPSampler.auto_redirects', False)
        self._add_bool_prop(sampler, 'HTTPSampler.use_keepalive', True)
        self._add_bool_prop(sampler, 'HTTPSampler.DO_MULTIPART_POST', False)
        self._add_string_prop(sampler, 'HTTPSampler.embedded_url_re', '')
        self._add_string_prop(sampler, 'HTTPSampler.connect_timeout', '')
        self._add_string_prop(sampler, 'HTTPSampler.response_timeout', '')
        
        sampler_tree = ET.SubElement(parent, 'hashTree')
        
        if self.config.include_assertions:
            self._add_response_assertion(sampler_tree, endpoint)
            if '200' in endpoint.responses or '201' in endpoint.responses:
                self._add_json_assertion(sampler_tree)
    
    def _add_response_assertion(self, parent: ET.Element, endpoint: APIEndpoint) -> None:
        """Add response code assertion."""
        assertion = ET.SubElement(parent, 'ResponseAssertion', {
            'guiclass': 'AssertionGui',
            'testclass': 'ResponseAssertion',
            'testname': 'Response Code Assertion',
            'enabled': 'true'
        })
        
        collection = ET.SubElement(assertion, 'collectionProp', {'name': 'Asserion.test_strings'})
        
        expected_codes = []
        for code in endpoint.responses.keys():
            if code.isdigit() and int(code) < 400:
                expected_codes.append(code)
        
        if not expected_codes:
            expected_codes = ['200', '201', '204']
        
        for code in expected_codes:
            ET.SubElement(collection, 'stringProp', {'name': str(hash(code))}).text = code
        
        self._add_string_prop(assertion, 'Assertion.custom_message', '')
        self._add_string_prop(assertion, 'Assertion.test_field', 'Assertion.response_code')
        self._add_bool_prop(assertion, 'Assertion.assume_success', False)
        self._add_int_prop(assertion, 'Assertion.test_type', 40)
        
        ET.SubElement(parent, 'hashTree')
    
    def _add_json_assertion(self, parent: ET.Element) -> None:
        """Add JSON format assertion."""
        assertion = ET.SubElement(parent, 'JSONPathAssertion', {
            'guiclass': 'JSONPathAssertionGui',
            'testclass': 'JSONPathAssertion',
            'testname': 'JSON Response Assertion',
            'enabled': 'true'
        })
        
        self._add_string_prop(assertion, 'JSON_PATH', '$')
        self._add_string_prop(assertion, 'EXPECTED_VALUE', '')
        self._add_bool_prop(assertion, 'JSONVALIDATION', False)
        self._add_bool_prop(assertion, 'EXPECT_NULL', False)
        self._add_bool_prop(assertion, 'INVERT', False)
        self._add_bool_prop(assertion, 'ISREGEX', False)
        
        ET.SubElement(parent, 'hashTree')
    
    def _add_think_time(self, parent: ET.Element) -> None:
        """Add random think time between requests."""
        timer = ET.SubElement(parent, 'UniformRandomTimer', {
            'guiclass': 'UniformRandomTimerGui',
            'testclass': 'UniformRandomTimer',
            'testname': 'Think Time',
            'enabled': 'true'
        })
        
        self._add_string_prop(timer, 'ConstantTimer.delay', '${THINK_TIME_MIN}')
        self._add_string_prop(timer, 'RandomTimer.range', 
            '${__jexl3(${THINK_TIME_MAX} - ${THINK_TIME_MIN})}')
        
        ET.SubElement(parent, 'hashTree')
    
    def _add_listeners(self, parent: ET.Element) -> None:
        """Add result listeners for reporting."""
        view_tree = ET.SubElement(parent, 'ResultCollector', {
            'guiclass': 'ViewResultsFullVisualizer',
            'testclass': 'ResultCollector',
            'testname': 'View Results Tree',
            'enabled': 'true'
        })
        self._add_bool_prop(view_tree, 'ResultCollector.error_logging', False)
        self._add_obj_prop(view_tree, 'saveConfig')
        ET.SubElement(parent, 'hashTree')
        
        summary = ET.SubElement(parent, 'ResultCollector', {
            'guiclass': 'SummaryReport',
            'testclass': 'ResultCollector',
            'testname': 'Summary Report',
            'enabled': 'true'
        })
        self._add_bool_prop(summary, 'ResultCollector.error_logging', False)
        self._add_obj_prop(summary, 'saveConfig')
        ET.SubElement(parent, 'hashTree')
        
        aggregate = ET.SubElement(parent, 'ResultCollector', {
            'guiclass': 'StatVisualizer',
            'testclass': 'ResultCollector',
            'testname': 'Aggregate Report',
            'enabled': 'true'
        })
        self._add_bool_prop(aggregate, 'ResultCollector.error_logging', False)
        self._add_obj_prop(aggregate, 'saveConfig')
        ET.SubElement(parent, 'hashTree')
    
    def _add_obj_prop(self, parent: ET.Element, name: str) -> None:
        """Add saveConfig object property."""
        obj = ET.SubElement(parent, 'objProp')
        ET.SubElement(obj, 'name').text = name
        value = ET.SubElement(obj, 'value', {'class': 'SampleSaveConfiguration'})
        
        for prop in ['time', 'latency', 'timestamp', 'success', 'label', 
                     'code', 'message', 'threadName', 'dataType', 'encoding',
                     'assertions', 'subresults', 'responseData', 'samplerData',
                     'xml', 'fieldNames', 'responseHeaders', 'requestHeaders',
                     'responseDataOnError', 'saveAssertionResultsFailureMessage',
                     'assertionsResultsToSave', 'bytes', 'sentBytes', 'url',
                     'threadCounts', 'idleTime', 'connectTime']:
            ET.SubElement(value, prop).text = 'true' if prop in [
                'time', 'latency', 'timestamp', 'success', 'label', 
                'code', 'message', 'threadName', 'bytes', 'sentBytes',
                'url', 'threadCounts', 'connectTime'
            ] else 'false'
    
    def _add_string_prop(self, parent: ET.Element, name: str, value: str) -> None:
        """Add a string property element."""
        prop = ET.SubElement(parent, 'stringProp', {'name': name})
        prop.text = value
    
    def _add_bool_prop(self, parent: ET.Element, name: str, value: bool) -> None:
        """Add a boolean property element."""
        prop = ET.SubElement(parent, 'boolProp', {'name': name})
        prop.text = str(value).lower()
    
    def _add_int_prop(self, parent: ET.Element, name: str, value: int) -> None:
        """Add an integer property element."""
        prop = ET.SubElement(parent, 'intProp', {'name': name})
        prop.text = str(value)


class APISpecWatcher:
    """
    Watches API spec files for changes and regenerates JMX files.
    
    WHAT: File system monitor that detects changes to OpenAPI specifications
    WHY: Enables automatic JMX regeneration without manual intervention
    HOW: Uses MD5 hash comparison to detect file modifications every 5 seconds
    """
    
    def __init__(self, spec_dir: str, output_dir: str, config: Optional[TestPlanConfig] = None):
        self.spec_dir = Path(spec_dir)
        self.output_dir = Path(output_dir)
        self.config = config or TestPlanConfig()
        self.file_hashes: Dict[str, str] = {}
        
        self.output_dir.mkdir(parents=True, exist_ok=True)
    
    def get_file_hash(self, filepath: Path) -> str:
        """Calculate MD5 hash of a file."""
        with open(filepath, 'rb') as f:
            return hashlib.md5(f.read()).hexdigest()
    
    def get_spec_files(self) -> List[Path]:
        """Get all OpenAPI spec files in the directory."""
        spec_files = []
        for ext in ['*.yaml', '*.yml', '*.json']:
            spec_files.extend(self.spec_dir.glob(ext))
        return list(set(spec_files))
    
    def generate_for_spec(self, spec_path: Path) -> str:
        """Generate JMX file for a single spec."""
        generator = JMXGenerator(self.config)
        generator.parse_openapi_spec(str(spec_path))
        
        output_name = spec_path.stem + '.jmx'
        output_path = self.output_dir / output_name
        
        generator.generate_jmx(str(output_path))
        return str(output_path)
    
    def check_and_regenerate(self) -> List[str]:
        """
        Check for changes and regenerate JMX files as needed.
        
        WHAT: Scans spec directory and regenerates JMX for changed files
        WHY: Keeps JMX files in sync with API specifications
        HOW: Compares current file hash with stored hash to detect changes
        """
        generated = []
        current_files = set()
        
        for spec_path in self.get_spec_files():
            current_files.add(str(spec_path))
            current_hash = self.get_file_hash(spec_path)
            
            if str(spec_path) not in self.file_hashes or \
               self.file_hashes[str(spec_path)] != current_hash:
                
                print(f"[CHANGE] Detected change in: {spec_path.name}")
                try:
                    output = self.generate_for_spec(spec_path)
                    generated.append(output)
                    self.file_hashes[str(spec_path)] = current_hash
                    print(f"[OK] Generated: {output}")
                except Exception as e:
                    print(f"[ERROR] Failed to generate JMX for {spec_path.name}: {str(e)}")
        
        deleted = set(self.file_hashes.keys()) - current_files
        for filepath in deleted:
            del self.file_hashes[filepath]
            jmx_name = Path(filepath).stem + '.jmx'
            jmx_path = self.output_dir / jmx_name
            if jmx_path.exists():
                jmx_path.unlink()
                print(f"[DELETED] Removed: {jmx_path}")
        
        return generated
    
    def run_once(self) -> List[str]:
        """Run a single check and generate."""
        return self.check_and_regenerate()
    
    def watch(self, interval: int = 5) -> None:
        """
        Continuously watch for changes.
        
        WHAT: Runs indefinitely, checking for file changes at specified interval
        WHY: Provides real-time synchronization between specs and JMX files
        HOW: Loops with sleep, calling check_and_regenerate each cycle
        """
        import time
        
        print(f"[WATCHING] {self.spec_dir} for changes...")
        print(f"[OUTPUT] Output directory: {self.output_dir}")
        print(f"[INTERVAL] Check interval: {interval}s")
        print("Press Ctrl+C to stop.\n")
        
        self.check_and_regenerate()
        
        try:
            while True:
                time.sleep(interval)
                self.check_and_regenerate()
        except KeyboardInterrupt:
            print("\n[STOP] Stopping watcher...")


def main():
    """
    Main entry point for the JMX Generator.
    
    WHAT: Parses command-line arguments and runs appropriate mode
    WHY: Provides flexible CLI interface for different use cases
    HOW: Uses argparse to handle single file, directory, and watch modes
    """
    parser = argparse.ArgumentParser(
        description='Generate JMeter test plans from OpenAPI specifications'
    )
    
    parser.add_argument('--spec', '-s', help='Path to OpenAPI specification file')
    parser.add_argument('--spec-dir', '-d', help='Directory containing OpenAPI specifications')
    parser.add_argument('--output', '-o', help='Output JMX file path')
    parser.add_argument('--output-dir', help='Output directory for generated JMX files')
    parser.add_argument('--watch', '-w', action='store_true', help='Watch for changes and regenerate')
    parser.add_argument('--interval', '-i', type=int, default=5, help='Watch interval in seconds (default: 5)')
    parser.add_argument('--threads', '-t', type=int, default=10, help='Number of threads (default: 10)')
    parser.add_argument('--ramp-up', '-r', type=int, default=60, help='Ramp-up period in seconds (default: 60)')
    parser.add_argument('--duration', type=int, default=300, help='Test duration in seconds (default: 300)')
    parser.add_argument('--config', '-c', help='Path to configuration file (YAML)')
    
    args = parser.parse_args()
    
    config = TestPlanConfig()
    if args.config:
        with open(args.config, 'r', encoding='utf-8') as f:
            config_data = yaml.safe_load(f)
            config = TestPlanConfig(**config_data)
    
    if args.threads:
        config.num_threads = args.threads
    if args.ramp_up:
        config.ramp_up_period = args.ramp_up
    if args.duration:
        config.duration = args.duration
    
    if args.spec:
        if not args.output:
            args.output = Path(args.spec).stem + '.jmx'
        
        generator = JMXGenerator(config)
        generator.parse_openapi_spec(args.spec)
        output = generator.generate_jmx(args.output)
        print(f"[OK] Generated: {output}")
        return
    
    if args.spec_dir:
        if not args.output_dir:
            args.output_dir = 'generated-jmx'
        
        watcher = APISpecWatcher(args.spec_dir, args.output_dir, config)
        
        if args.watch:
            watcher.watch(args.interval)
        else:
            generated = watcher.run_once()
            if generated:
                print(f"\n[DONE] Generated {len(generated)} JMX file(s)")
            else:
                print("No spec files found or no changes detected.")
        return
    
    parser.print_help()


if __name__ == '__main__':
    main()