# Dual Backend Integration Guide

## Overview
The Numerical Methods Calculator now features a **dual-backend architecture**:

1. **Python Backend** (FastAPI) - Original implementation
2. **Java Backend** (Spring Boot) - New parallel implementation

Both backends provide identical functionality for all 5 numerical methods.

## Architecture Diagram

```
┌─────────────────────────────────────────────────┐
│           Frontend (HTML + CSS)                 │
│        (Served by Python FastAPI)               │
└───────────────────┬─────────────────────────────┘
                    │
        ┌───────────┴──────────┐
        │                      │
        ▼                      ▼
┌───────────────┐      ┌──────────────┐
│ Python Backend│      │ Java Backend │
│  (FastAPI)    │      │ (Spring Boot)│
│  Port: 8000   │      │  Port: 8080  │
├───────────────┤      ├──────────────┤
│ • Jacobi      │      │ • Jacobi     │
│ • Regula-Falsi│      │ • Regula-Falsi│
│ • Forward FD  │      │ • Forward FD │
│ • Backward FD │      │ • Backward FD│
│ • Central FD  │      │ • Central FD │
└───────────────┘      └──────────────┘
```

## Backend Comparison

| Feature | Python Backend | Java Backend |
|---------|---------------|--------------|
| Framework | FastAPI 0.122.0 | Spring Boot 3.2.0 |
| Language | Python 3.13.5 | Java 21 |
| Port | 8000 | 8080 |
| Templates | ✅ Jinja2 | ❌ API only |
| REST API | ✅ | ✅ |
| CORS | ✅ | ✅ |
| Validation | ✅ Pydantic | ✅ Jakarta Bean Validation |
| Hot Reload | ✅ Uvicorn | ✅ Spring DevTools |

## Running Both Backends

### Python Backend
```bash
# Terminal 1
cd "d:\Numerical Methods"
.venv\Scripts\activate
python -m uvicorn main:app --reload
```
Access at: http://localhost:8000

### Java Backend
```bash
# Terminal 2
cd "d:\Numerical Methods\java-backend"
mvn spring-boot:run
```
Access at: http://localhost:8080

## API Endpoint Mapping

### Python Endpoints (FastAPI)
- `POST http://localhost:8000/api/jacobi`
- `POST http://localhost:8000/api/regula-falsi`
- `POST http://localhost:8000/api/forward-fd`
- `POST http://localhost:8000/api/backward-fd`
- `POST http://localhost:8000/api/center-fd`

### Java Endpoints (Spring Boot)
- `POST http://localhost:8080/api/jacobi`
- `POST http://localhost:8080/api/regula-falsi`
- `POST http://localhost:8080/api/finite-difference/forward`
- `POST http://localhost:8080/api/finite-difference/backward`
- `POST http://localhost:8080/api/finite-difference/central`

## Request/Response Format

Both backends use **identical JSON request/response formats** for compatibility.

### Example: Jacobi Method

**Request** (same for both):
```json
{
  "matrixA": [[4, 1, 1], [1, 5, 2], [1, 2, 3]],
  "vectorB": [2, -6, -4],
  "initialGuess": [0, 0, 0],
  "maxIterations": 100,
  "tolerance": 0.000001
}
```

**Response** (same structure):
```json
{
  "success": true,
  "result": [1.0, -2.0, 1.0],
  "message": "Converged after 15 iterations",
  "iterations": 15,
  "error": 0.0000008,
  "iterationLog": [...]
}
```

## Frontend Integration (Future Enhancement)

To allow users to choose backends dynamically:

### Option 1: JavaScript Backend Selector
Add to templates:
```html
<div class="backend-selector">
  <label>Backend:</label>
  <select id="backend-choice">
    <option value="python">Python (FastAPI)</option>
    <option value="java">Java (Spring Boot)</option>
  </select>
</div>

<script>
  document.getElementById('backend-choice').addEventListener('change', function() {
    const backend = this.value;
    const apiUrl = backend === 'python' 
      ? 'http://localhost:8000/api/jacobi'
      : 'http://localhost:8080/api/jacobi';
    
    // Update form action or fetch URL
    document.querySelector('form').action = apiUrl;
  });
</script>
```

### Option 2: Environment Variable
Set backend preference in `config.json`:
```json
{
  "preferred_backend": "java",
  "python_backend_url": "http://localhost:8000",
  "java_backend_url": "http://localhost:8080"
}
```

## Configuration Files

### Python Configuration
**File**: `config.json`
```json
{
  "jacobi": {
    "max_iterations": 100,
    "tolerance": 1e-6
  },
  "regula_falsi": {
    "max_iterations": 100,
    "tolerance": 1e-6
  },
  "finite_difference": {
    "step_size": 0.01
  }
}
```

### Java Configuration
**File**: `java-backend/src/main/resources/application.properties`
```properties
server.port=8080
numerical.jacobi.max-iterations=100
numerical.jacobi.tolerance=0.000001
numerical.regula-falsi.max-iterations=100
numerical.regula-falsi.tolerance=0.000001
numerical.finite-difference.default-step=0.01
```

## CORS Configuration

### Python CORS (main.py)
```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### Java CORS (CorsConfig.java)
```java
registry.addMapping("/api/**")
    .allowedOrigins("http://localhost:8000")
    .allowedMethods("GET", "POST", "PUT", "DELETE", "OPTIONS")
    .allowCredentials(true);
```

## Testing Both Backends

### Using cURL

**Python Backend:**
```bash
curl -X POST http://localhost:8000/api/jacobi \
  -H "Content-Type: application/json" \
  -d '{"matrixA":[[4,1,1],[1,5,2],[1,2,3]],"vectorB":[2,-6,-4]}'
```

**Java Backend:**
```bash
curl -X POST http://localhost:8080/api/jacobi \
  -H "Content-Type: application/json" \
  -d '{"matrixA":[[4,1,1],[1,5,2],[1,2,3]],"vectorB":[2,-6,-4]}'
```

### Using Python requests
```python
import requests

# Test Python backend
python_response = requests.post(
    "http://localhost:8000/api/jacobi",
    json={
        "matrixA": [[4, 1, 1], [1, 5, 2], [1, 2, 3]],
        "vectorB": [2, -6, -4]
    }
)

# Test Java backend
java_response = requests.post(
    "http://localhost:8080/api/jacobi",
    json={
        "matrixA": [[4, 1, 1], [1, 5, 2], [1, 2, 3]],
        "vectorB": [2, -6, -4]
    }
)

print("Python Result:", python_response.json())
print("Java Result:", java_response.json())
```

## Troubleshooting

### Port Conflicts
If port 8080 is already in use, change in `application.properties`:
```properties
server.port=8081
```

### CORS Errors
Ensure both backends allow requests from each other:
- Python allows Java: Already configured
- Java allows Python: Check `CorsConfig.java`

### Maven Build Issues
```bash
# Clean and rebuild
cd java-backend
mvn clean install -DskipTests
```

### Dependency Issues
**Python:**
```bash
pip install -r requirements.txt
```

**Java:**
```bash
mvn dependency:resolve
```

## Performance Comparison

Run benchmarks to compare performance:

```python
import time
import requests

def benchmark(url, payload, runs=100):
    times = []
    for _ in range(runs):
        start = time.time()
        requests.post(url, json=payload)
        times.append(time.time() - start)
    return sum(times) / len(times)

payload = {
    "matrixA": [[4, 1, 1], [1, 5, 2], [1, 2, 3]],
    "vectorB": [2, -6, -4]
}

python_avg = benchmark("http://localhost:8000/api/jacobi", payload)
java_avg = benchmark("http://localhost:8080/api/jacobi", payload)

print(f"Python Backend: {python_avg*1000:.2f}ms")
print(f"Java Backend: {java_avg*1000:.2f}ms")
```

## Deployment Considerations

### Docker Deployment
Both backends can run in separate containers:

**Python Dockerfile** (already exists):
```dockerfile
FROM python:3.13
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

**Java Dockerfile** (to be created):
```dockerfile
FROM openjdk:21-jdk-slim
WORKDIR /app
COPY java-backend/target/*.jar app.jar
EXPOSE 8080
CMD ["java", "-jar", "app.jar"]
```

### Docker Compose
```yaml
version: '3.8'
services:
  python-backend:
    build: .
    ports:
      - "8000:8000"
  
  java-backend:
    build:
      context: .
      dockerfile: java-backend/Dockerfile
    ports:
      - "8080:8080"
```

## Advantages of Dual Backend

1. **Language Diversity**: Developers can work in their preferred language
2. **Performance Testing**: Compare Python vs Java performance
3. **Redundancy**: Fallback if one backend fails
4. **Learning**: Study implementation differences
5. **Scalability**: Load balance between backends

## Future Enhancements

- [ ] Add backend health monitoring dashboard
- [ ] Implement load balancing between backends
- [ ] Add Redis caching layer for both backends
- [ ] Create unified configuration service
- [ ] Add API gateway (e.g., Kong, API Gateway)
- [ ] Implement request tracing across backends
- [ ] Add comprehensive integration tests
- [ ] Create frontend backend selector UI
- [ ] Add authentication/authorization
- [ ] Implement result comparison tool

## Conclusion

The dual-backend architecture provides flexibility, redundancy, and learning opportunities while maintaining API compatibility. Both backends can be used independently or together based on requirements.
