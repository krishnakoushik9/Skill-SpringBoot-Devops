# 🚀 JMX Auto-Sync: Step-by-Step Implementation Guide

## Prerequisites Checklist

Before starting, ensure you have:

- [x] **Windsurf IDE** installed
- [x] **JMeter 5.x** installed
- [x] **Python 3.8+** installed (for fallback script)
- [x] **PyYAML** Python package (`pip install pyyaml`)

---

## 📁 Step 1: Set Up the Project

### 1.1 Extract the Project

```bash
# Extract the POC zip file
unzip jmx-autosync-poc.zip -d jmx-autosync-poc
cd jmx-autosync-poc
```

### 1.2 Verify Project Structure

```
jmx-autosync-poc/
├── .windsurfrules              # Main Windsurf configuration
├── .windsurf/
│   ├── memories.md             # Project context for Cascade
│   └── jmx-config.yaml         # Test generation settings
├── .cascade/
│   └── jmx-instructions.md     # JMX generation instructions
├── api-specs/                  # Your OpenAPI specifications
│   ├── user-service.yaml       # User management API
│   ├── order-service.yaml      # Order management API
│   ├── product-service.yaml    # Product catalog API
│   └── payment-service.yaml    # Payment processing API
├── performance-tests/          # Generated JMX files (output)
├── scripts/
│   └── jmx_generator.py        # Python generator (fallback)
└── docs/                       # Documentation
```

### 1.3 Install Python Dependency

```bash
pip install pyyaml
```

---

## 🌊 Step 2: Open in Windsurf

### 2.1 Launch Windsurf

```bash
# Navigate to project directory
cd jmx-autosync-poc

# Open in Windsurf
windsurf .
```

### 2.2 Verify Cascade Recognition

When Windsurf opens, Cascade should recognize the project configuration.

**Check for:**
- Cascade reads `.windsurfrules`
- Project context loaded from `.windsurf/memories.md`
- JMX instructions loaded from `.cascade/jmx-instructions.md`

---

## 💬 Step 3: Generate Your First JMX File

### 3.1 Using Natural Language (Primary Method)

In the Windsurf chat panel, type:

```
Generate JMX for user-service.yaml
```

**Expected Response from Cascade:**
```
🔄 Generating JMX for user-service.yaml...

Reading OpenAPI specification...
✓ Found 13 endpoints across 3 tags

Generating JMeter test plan...
✓ Created Thread Groups: Users, Authentication, Profile
✓ Added HTTP Samplers for all endpoints
✓ Added response assertions
✓ Configured think times

✅ Generated: performance-tests/user-service.jmx

Summary:
├── Thread Groups: 3
├── HTTP Requests: 13
├── Assertions: 13
└── Variables: SERVER, PORT, AUTH_TOKEN, USERID
```

### 3.2 Alternative: Using Python Script

If Cascade isn't available, use the command line:

```bash
python scripts/jmx_generator.py \
    --spec api-specs/user-service.yaml \
    --output performance-tests/user-service.jmx
```

---

## 🔄 Step 4: Generate All JMX Files

### 4.1 Sync All APIs

In Windsurf chat:

```
Sync all performance tests
```

Or using Python:

```bash
python scripts/jmx_generator.py \
    --spec-dir api-specs \
    --output-dir performance-tests
```

**Expected Output:**
```
✅ Generated: performance-tests/user-service.jmx
✅ Generated: performance-tests/order-service.jmx
✅ Generated: performance-tests/product-service.jmx
✅ Generated: performance-tests/payment-service.jmx

📊 Generated 4 JMX files
```

### 4.2 Verify Generated Files

```bash
ls -la performance-tests/
```

You should see:
```
user-service.jmx
order-service.jmx
product-service.jmx
payment-service.jmx
```

---

## 🧪 Step 5: Run JMeter Tests

### 5.1 Open in JMeter GUI (for debugging)

```bash
# Open specific test
jmeter -t performance-tests/user-service.jmx
```

### 5.2 Run in Non-GUI Mode (for actual testing)

```bash
# Basic run
jmeter -n -t performance-tests/user-service.jmx -l results.jtl

# With HTML report
jmeter -n -t performance-tests/user-service.jmx \
    -l results.jtl \
    -e -o html-report/
```

### 5.3 Run with Custom Parameters

```bash
# Override server and threads at runtime
jmeter -n -t performance-tests/user-service.jmx \
    -JSERVER=staging-api.example.com \
    -JPORT=443 \
    -JPROTOCOL=https \
    -JTHREADS=50 \
    -JDURATION=600 \
    -Jauth.token=your_bearer_token_here \
    -l results.jtl
```

---

## ⚡ Step 6: Test Auto-Detection (Key Feature!)

### 6.1 Modify an API Spec

1. Open `api-specs/user-service.yaml` in Windsurf
2. Add a new endpoint:

```yaml
  /users/{userId}/settings:
    get:
      operationId: getUserSettings
      summary: Get user settings
      tags:
        - Profile
      parameters:
        - name: userId
          in: path
          required: true
          schema:
            type: string
            format: uuid
      responses:
        '200':
          description: Settings retrieved
```

3. **Save the file** (Ctrl+S / Cmd+S)

### 6.2 Observe Cascade Response

Cascade should prompt:

```
🔄 API Specification Changed!

I detected changes to user-service.yaml.

Would you like me to regenerate the JMX performance test file?

Say "yes" or "regenerate" to update the tests.
```

### 6.3 Confirm Regeneration

Type:
```
yes
```

Cascade regenerates `user-service.jmx` with the new endpoint.

---

## 🎛️ Step 7: Customize Test Configuration

### 7.1 Change Default Settings

Edit `.windsurf/jmx-config.yaml`:

```yaml
execution:
  threads: 25         # Increase from 10
  duration: 600       # Increase from 300
```

### 7.2 Generate with Custom Settings

```
Generate JMX for order-service.yaml with 100 threads and 10 minute duration
```

### 7.3 Use Profiles

```
Generate JMX for payment-service.yaml using load profile
```

This applies the `load` profile from config:
- 100 threads
- 600 second duration
- Production server settings

---

## 📊 Step 8: View Generated Test Structure

### 8.1 Open in JMeter

```bash
jmeter -t performance-tests/order-service.jmx
```

### 8.2 Expected Structure

```
📁 Order Service Performance Tests
├── 📋 User Defined Variables
│   ├── SERVER = localhost
│   ├── PORT = 8082
│   ├── THREADS = 10
│   └── AUTH_TOKEN = ${__P(auth.token,)}
├── ⚙️ HTTP Request Defaults
├── 📨 HTTP Header Manager
├── 🍪 HTTP Cookie Manager
├── 📁 Orders Tests (Thread Group)
│   ├── 🌐 List orders (GET)
│   ├── 🌐 Create new order (POST)
│   ├── 🌐 Get order details (GET)
│   ├── 🌐 Update order (PATCH)
│   ├── 🌐 Cancel order (POST)
│   └── ⏱️ Think Time
├── 📁 OrderItems Tests (Thread Group)
│   ├── 🌐 Get order items (GET)
│   ├── 🌐 Add item to order (POST)
│   ├── 🌐 Remove item from order (DELETE)
│   └── ⏱️ Think Time
├── 📁 OrderStatus Tests (Thread Group)
│   ├── 🌐 Get order status (GET)
│   ├── 🌐 Update order status (PUT)
│   ├── 🌐 Get order history (GET)
│   └── ⏱️ Think Time
├── 📊 Summary Report
└── 📊 Aggregate Report
```

---

## 🔧 Step 9: Advanced Usage

### 9.1 Watch Mode (Continuous Sync)

```bash
python scripts/jmx_generator.py \
    --spec-dir api-specs \
    --output-dir performance-tests \
    --watch
```

This continuously monitors API specs and regenerates JMX on any change.

### 9.2 Add Your Own API

1. Copy your OpenAPI spec to `api-specs/`:
   ```bash
   cp /path/to/my-api.yaml api-specs/
   ```

2. Generate JMX:
   ```
   Generate JMX for my-api.yaml
   ```

### 9.3 Bulk Commands

```
# Generate all with custom threads
Generate all JMX files with 50 threads

# List all APIs
Show all API specs and endpoints
```

---

## ✅ Step 10: Verify Everything Works

### 10.1 Complete Workflow Test

1. **Generate:** `Generate JMX for all APIs`
2. **Verify:** Check `performance-tests/` has 4 JMX files
3. **Modify:** Add endpoint to any API spec
4. **Auto-detect:** Cascade prompts for regeneration
5. **Run:** Execute test in JMeter
6. **Report:** View HTML report

### 10.2 Checklist

- [ ] Windsurf opens project correctly
- [ ] Cascade responds to "generate jmx" commands
- [ ] JMX files are created in `performance-tests/`
- [ ] Auto-detection triggers on API spec save
- [ ] JMeter opens generated JMX without errors
- [ ] Tests run successfully (even if API isn't running)

---

## 🆘 Troubleshooting

### Issue: Cascade doesn't respond

**Solution:** Ensure `.windsurfrules` is in project root and Windsurf is restarted.

### Issue: JMX file has XML errors

**Solution:** Use Python script as fallback:
```bash
python scripts/jmx_generator.py --spec api-specs/[file].yaml --output test.jmx
```

### Issue: JMeter shows "Server not found"

**Expected!** The generated tests point to localhost by default. Either:
- Run your actual API server
- Update SERVER variable to point to real server
- Use JMeter to just validate the test structure

### Issue: Auto-detection not working

**Solution:** 
1. Check file is saved in `api-specs/` directory
2. Verify file extension is `.yaml` or `.yml`
3. Restart Windsurf

---

## 🎯 Quick Reference

| Task | Command |
|------|---------|
| Generate single JMX | `Generate JMX for [filename].yaml` |
| Generate all JMX | `Sync all performance tests` |
| Custom threads | `Generate JMX for [file] with 50 threads` |
| Use profile | `Generate JMX using staging profile` |
| List APIs | `Show all API specs` |

---

## 📚 Next Steps

1. **Integrate with CI/CD:** Add JMX generation to your build pipeline
2. **Connect to real APIs:** Update SERVER variables to point to actual services
3. **Add authentication:** Set AUTH_TOKEN for protected endpoints
4. **Customize assertions:** Add response time thresholds
5. **Create data files:** Add CSV data for parameterized testing

---

**Congratulations!** 🎉 You now have automated JMX generation from OpenAPI specs!
