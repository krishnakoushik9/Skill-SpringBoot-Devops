# JMX Auto-Sync Project Context

## Project Overview
This project automatically generates JMeter (.jmx) performance test files from OpenAPI specifications. The goal is to keep performance tests synchronized with API definitions with zero manual effort.

## Available APIs in This POC

### 1. User Service (user-service.yaml)
- **Port:** 8081
- **Endpoints:** 13
- **Tags:** Users, Authentication, Profile
- **Key Operations:**
  - User CRUD operations
  - Login/Logout/Token refresh
  - Profile management
  - Password reset

### 2. Order Service (order-service.yaml)
- **Port:** 8082
- **Endpoints:** 12
- **Tags:** Orders, OrderItems, OrderStatus
- **Key Operations:**
  - Order creation and management
  - Order item management
  - Status tracking and history
  - Order cancellation

### 3. Product Service (product-service.yaml)
- **Port:** 8083
- **Endpoints:** 13
- **Tags:** Products, Categories, Inventory
- **Key Operations:**
  - Product catalog CRUD
  - Category management
  - Inventory tracking

### 4. Payment Service (payment-service.yaml)
- **Port:** 8084
- **Endpoints:** 13
- **Tags:** Payments, Refunds, PaymentMethods
- **Key Operations:**
  - Payment processing
  - Refund management
  - Saved payment methods

## How to Use

### Generate JMX for a single API:
```
Generate JMX for user-service.yaml
```

### Generate JMX for all APIs:
```
Sync all performance tests
```

### Generate with custom settings:
```
Generate JMX for order-service.yaml with 50 threads
```

## File Locations
- **API Specs:** `api-specs/*.yaml`
- **Generated JMX:** `performance-tests/*.jmx`
- **Configuration:** `.windsurf/jmx-config.yaml`
- **Python Script:** `scripts/jmx_generator.py`

## JMX Generation Rules
1. Each API spec generates one JMX file
2. Endpoints are grouped by OpenAPI tags into Thread Groups
3. Request bodies use examples from OpenAPI spec
4. Path parameters become JMeter variables (e.g., {userId} → ${USERID})
5. Response code assertions are added automatically
6. Think time is added between requests

## Quick Commands Reference
| Command | Description |
|---------|-------------|
| "generate jmx for [file]" | Generate JMX for specific API |
| "sync all" | Regenerate all JMX files |
| "generate with N threads" | Override thread count |
| "use staging profile" | Apply staging configuration |
