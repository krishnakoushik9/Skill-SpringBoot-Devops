# 🌊 JMX Auto-Sync POC

> **Automatically generate JMeter performance tests from OpenAPI specifications using Windsurf + Cascade AI**

## 🎯 What This POC Demonstrates

1. **Natural Language JMX Generation** - Tell Cascade "Generate JMX for user-service.yaml"
2. **Auto-Detection** - Save an API spec → Cascade offers to regenerate tests
3. **Multiple APIs** - 4 sample microservice APIs ready to test
4. **Production-Ready JMX** - Generated tests include assertions, think times, and reports

## 📁 Included APIs

| Service | Port | Endpoints | Description |
|---------|------|-----------|-------------|
| User Service | 8081 | 13 | User management & authentication |
| Order Service | 8082 | 12 | Order processing & tracking |
| Product Service | 8083 | 13 | Product catalog & inventory |
| Payment Service | 8084 | 13 | Payment processing & refunds |

**Total: 51 API endpoints → 4 JMX test plans**

## ⚡ Quick Start

```bash
# 1. Extract and enter project
cd jmx-autosync-poc

# 2. Open in Windsurf
windsurf .

# 3. Ask Cascade to generate tests
#    Type in chat: "Generate JMX for user-service.yaml"

# 4. Run the generated test
jmeter -t performance-tests/user-service.jmx
```

## 📖 Documentation

- **[IMPLEMENTATION_GUIDE.md](IMPLEMENTATION_GUIDE.md)** - Detailed step-by-step instructions
- **[docs/](docs/)** - Technical documentation and presentation

## 💬 Cascade Commands

| Command | Action |
|---------|--------|
| `Generate JMX for [file].yaml` | Create JMX for specific API |
| `Sync all performance tests` | Generate JMX for all APIs |
| `Generate with 50 threads` | Custom thread count |
| `Use staging profile` | Apply environment settings |

## 🔄 Auto-Detection

1. Edit any file in `api-specs/`
2. Save the file
3. Cascade prompts: "API changed! Regenerate JMX?"
4. Say "yes" → Tests updated automatically

## 📊 Generated JMX Features

- ✅ Thread Groups organized by API tags
- ✅ HTTP Samplers for all endpoints
- ✅ Request bodies from OpenAPI examples
- ✅ Path parameter variables (${USERID}, etc.)
- ✅ Response code assertions
- ✅ Think times between requests
- ✅ Summary and Aggregate reports

## 🛠️ Fallback: Python Script

```bash
# Single file
python scripts/jmx_generator.py --spec api-specs/user-service.yaml --output performance-tests/user-service.jmx

# All files
python scripts/jmx_generator.py --spec-dir api-specs --output-dir performance-tests

# Watch mode
python scripts/jmx_generator.py --spec-dir api-specs --output-dir performance-tests --watch
```

## 📋 Prerequisites

- Windsurf IDE
- JMeter 5.x
- Python 3.8+ with PyYAML (`pip install pyyaml`)

## 📄 License

MIT License - Use freely for your projects!
