# 🧪 JMX Unit Test Generator

> **By:** Krishna | **Purpose:** Auto-generate JMeter tests from API specs

---

## What Does This Do?

Converts your **API documentation (YAML)** → **JMeter test files (JMX)**

```
api-specs/user-service.yaml  →  unit-tests/user-service-unit.jmx
```

No manual test writing needed! 🎉

---

## Unit Tests vs Performance Tests

| | Unit Tests | Performance Tests |
|--|------------|-------------------|
| **Script** | `jmx_unit.py` | `jmx_generator.py` |
| **Users** | 1 (isolated) | 10+ (concurrent) |
| **Runs** | Once | 5+ minutes |
| **Purpose** | "Does it work?" | "Can it handle load?" |

---

## Quick Commands

```bash
# Generate all unit tests
python3 scripts/jmx_unit.py --spec-dir api-specs --output-dir unit-tests

# Generate single file
python3 scripts/jmx_unit.py --spec api-specs/user-service.yaml

# Watch mode (auto-regenerate on file save)
python3 scripts/jmx_unit.py --spec-dir api-specs --output-dir unit-tests --watch
```

---

## 🤖 Automated Mode (Cron)

Tests regenerate **automatically every 5 minutes** via cron job.

```bash
# Check active crons
crontab -l

# View logs
tail -f /tmp/jmx_unit_cron.log

# Remove automation
crontab -r
```

**Just edit your YAML → Wait 5 min → JMX files update automatically!**

---

## Run Tests in JMeter

```bash
# GUI mode
jmeter -t unit-tests/user-service-unit.jmx

# Headless (CLI)
jmeter -n -t unit-tests/user-service-unit.jmx -l results.jtl
```

---
