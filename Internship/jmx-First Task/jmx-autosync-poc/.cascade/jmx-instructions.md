# JMX Generation Instructions for Cascade AI

This document teaches Cascade how to generate valid JMeter test plans from OpenAPI specifications.

## Overview

When asked to generate JMX files, you should:
1. Read the OpenAPI spec from `api-specs/` directory
2. Parse all endpoints, parameters, and request bodies
3. Generate valid JMX XML following the structure below
4. Save to `performance-tests/` directory

## JMX File Structure

```xml
<?xml version="1.0" encoding="UTF-8"?>
<jmeterTestPlan version="1.2" properties="5.0" jmeter="5.6.3">
  <hashTree>
    <TestPlan guiclass="TestPlanGui" testclass="TestPlan" testname="[API_NAME] Performance Tests">
      <!-- Test plan properties -->
    </TestPlan>
    <hashTree>
      <!-- User Defined Variables -->
      <Arguments>...</Arguments>
      <hashTree/>
      
      <!-- HTTP Request Defaults -->
      <ConfigTestElement>...</ConfigTestElement>
      <hashTree/>
      
      <!-- HTTP Header Manager -->
      <HeaderManager>...</HeaderManager>
      <hashTree/>
      
      <!-- Cookie Manager -->
      <CookieManager>...</CookieManager>
      <hashTree/>
      
      <!-- Thread Groups (one per tag) -->
      <ThreadGroup testname="[TAG_NAME] Tests">...</ThreadGroup>
      <hashTree>
        <!-- HTTP Samplers -->
        <HTTPSamplerProxy>...</HTTPSamplerProxy>
        <hashTree>
          <!-- Assertions -->
          <ResponseAssertion>...</ResponseAssertion>
          <hashTree/>
        </hashTree>
        <!-- Think Time -->
        <UniformRandomTimer>...</UniformRandomTimer>
        <hashTree/>
      </hashTree>
      
      <!-- Listeners -->
      <ResultCollector>...</ResultCollector>
      <hashTree/>
    </hashTree>
  </hashTree>
</jmeterTestPlan>
```

## Step-by-Step Generation

### Step 1: Extract from OpenAPI Spec

```yaml
# From the spec, extract:
info.title → Test Plan name
servers[0].url → Protocol, host, port, basePath
paths → List of endpoints
tags → Thread group names
```

### Step 2: Create User Defined Variables

Variables to include:
- `SERVER` - hostname from servers[0].url
- `PORT` - port from servers[0].url
- `PROTOCOL` - http or https
- `BASE_PATH` - path portion of URL
- `THREADS` - default 10
- `RAMP_UP` - default 60
- `DURATION` - default 300
- `THINK_TIME_MIN` - default 1000
- `THINK_TIME_MAX` - default 3000
- `AUTH_TOKEN` - empty, set at runtime

### Step 3: Create HTTP Request Defaults

```xml
<ConfigTestElement guiclass="HttpDefaultsGui" testclass="ConfigTestElement" testname="HTTP Request Defaults" enabled="true">
  <stringProp name="HTTPSampler.domain">${SERVER}</stringProp>
  <stringProp name="HTTPSampler.port">${PORT}</stringProp>
  <stringProp name="HTTPSampler.protocol">${PROTOCOL}</stringProp>
  <stringProp name="HTTPSampler.contentEncoding">UTF-8</stringProp>
</ConfigTestElement>
```

### Step 4: Create Thread Groups

For each unique tag in the OpenAPI spec:
```xml
<ThreadGroup guiclass="ThreadGroupGui" testclass="ThreadGroup" testname="[TAG] Tests" enabled="true">
  <stringProp name="ThreadGroup.num_threads">${THREADS}</stringProp>
  <stringProp name="ThreadGroup.ramp_time">${RAMP_UP}</stringProp>
  <boolProp name="ThreadGroup.scheduler">true</boolProp>
  <stringProp name="ThreadGroup.duration">${DURATION}</stringProp>
</ThreadGroup>
```

### Step 5: Create HTTP Samplers

For each endpoint in a tag:
```xml
<HTTPSamplerProxy guiclass="HttpTestSampleGui" testclass="HTTPSamplerProxy" testname="[SUMMARY] ([METHOD])" enabled="true">
  <stringProp name="HTTPSampler.path">${BASE_PATH}[PATH]</stringProp>
  <stringProp name="HTTPSampler.method">[METHOD]</stringProp>
  <!-- Add body for POST/PUT/PATCH -->
</HTTPSamplerProxy>
```

### Step 6: Handle Path Parameters

Convert OpenAPI path parameters to JMeter variables:
- `/users/{userId}` → `/users/${USERID}`
- `/orders/{orderId}/items/{itemId}` → `/orders/${ORDERID}/items/${ITEMID}`

### Step 7: Generate Request Bodies

For POST/PUT/PATCH requests with requestBody:
1. Use `example` if provided
2. Otherwise, generate from schema:
   - string → "sample_value"
   - string (email) → "test@example.com"
   - string (uuid) → "550e8400-e29b-41d4-a716-446655440000"
   - integer → 1
   - boolean → true
   - array → []

### Step 8: Add Assertions

For each sampler, add response code assertion:
```xml
<ResponseAssertion guiclass="AssertionGui" testclass="ResponseAssertion" testname="Response Code Assertion" enabled="true">
  <collectionProp name="Asserion.test_strings">
    <stringProp name="0">200</stringProp>
    <stringProp name="1">201</stringProp>
    <stringProp name="2">204</stringProp>
  </collectionProp>
  <stringProp name="Assertion.test_field">Assertion.response_code</stringProp>
  <intProp name="Assertion.test_type">40</intProp>
</ResponseAssertion>
```

### Step 9: Add Think Time

Between requests:
```xml
<UniformRandomTimer guiclass="UniformRandomTimerGui" testclass="UniformRandomTimer" testname="Think Time" enabled="true">
  <stringProp name="ConstantTimer.delay">${THINK_TIME_MIN}</stringProp>
  <stringProp name="RandomTimer.range">${__jexl3(${THINK_TIME_MAX} - ${THINK_TIME_MIN})}</stringProp>
</UniformRandomTimer>
```

### Step 10: Add Listeners

```xml
<ResultCollector guiclass="SummaryReport" testclass="ResultCollector" testname="Summary Report" enabled="true"/>
<ResultCollector guiclass="StatVisualizer" testclass="ResultCollector" testname="Aggregate Report" enabled="true"/>
```

## Quick Reference Table

| OpenAPI | JMeter |
|---------|--------|
| `info.title` | TestPlan name |
| `servers[0].url` | HTTP Defaults |
| `tags` | ThreadGroup names |
| `paths.{path}.{method}` | HTTPSamplerProxy |
| `parameters[in=query]` | HTTPArgument |
| `parameters[in=path]` | ${VARIABLE} in path |
| `requestBody.example` | Body data |
| `responses.2xx` | ResponseAssertion |

## Example Generation

Given `user-service.yaml`:
```yaml
paths:
  /users:
    get:
      tags: [Users]
      summary: List users
  /users/{userId}:
    get:
      tags: [Users]
      summary: Get user by ID
  /auth/login:
    post:
      tags: [Authentication]
      summary: User login
```

Generate `user-service.jmx` with:
- 2 Thread Groups: "Users Tests", "Authentication Tests"
- 3 HTTP Samplers
- Variables: SERVER, PORT, USERID, etc.

## Python Script Alternative

If complex generation is needed, use:
```bash
python scripts/jmx_generator.py --spec api-specs/[file].yaml --output performance-tests/[file].jmx
```

For all files:
```bash
python scripts/jmx_generator.py --spec-dir api-specs --output-dir performance-tests
```
