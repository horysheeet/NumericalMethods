# Numerical Methods Calculator - Quick Start Guide (Dual Backend)

This guide helps you run the Numerical Methods Calculator with both Python and Java backends.

## Prerequisites Check

### Python Backend
- ✅ Python 3.8+ installed
- ✅ Virtual environment created (`.venv`)
- ✅ Dependencies installed (`requirements.txt`)

### Java Backend
- ✅ Java 21+ installed
- ✅ Maven 3.6+ installed
- ✅ Java backend built (`mvn clean install`)

## Quick Start (Both Backends)

### Option 1: Automated Startup (Recommended)

Run the dual backend startup script:

```powershell
.\start-dual-backend.ps1
```

This will:
1. Check prerequisites
2. Build Java backend if needed
3. Start Python backend in a new window (port 8000)
4. Start Java backend in a new window (port 8080)

### Option 2: Manual Startup

**Terminal 1 - Python Backend:**
```powershell
cd "d:\Numerical Methods"
.venv\Scripts\activate
python -m uvicorn main:app --reload
```

**Terminal 2 - Java Backend:**
```powershell
cd "d:\Numerical Methods\java-backend"
mvn spring-boot:run
```

## Accessing the Application

### Web Interface (Python)
Open browser: **http://localhost:8000**

This serves the HTML+CSS frontend with all 5 numerical methods.

### API Endpoints

#### Python Backend (Port 8000)
- `POST http://localhost:8000/api/jacobi`
- `POST http://localhost:8000/api/regula-falsi`
- `POST http://localhost:8000/api/forward-fd`
- `POST http://localhost:8000/api/backward-fd`
- `POST http://localhost:8000/api/center-fd`

#### Java Backend (Port 8080)
- `POST http://localhost:8080/api/jacobi`
- `POST http://localhost:8080/api/regula-falsi`
- `POST http://localhost:8080/api/finite-difference/forward`
- `POST http://localhost:8080/api/finite-difference/backward`
- `POST http://localhost:8080/api/finite-difference/central`

## Testing the APIs

### Using cURL

**Python Backend:**
```bash
curl -X POST http://localhost:8000/api/jacobi ^
  -H "Content-Type: application/json" ^
  -d "{\"matrixA\":[[4,1,1],[1,5,2],[1,2,3]],\"vectorB\":[2,-6,-4]}"
```

**Java Backend:**
```bash
curl -X POST http://localhost:8080/api/jacobi ^
  -H "Content-Type: application/json" ^
  -d "{\"matrixA\":[[4,1,1],[1,5,2],[1,2,3]],\"vectorB\":[2,-6,-4]}"
```

### Using Python
```python
import requests

# Python backend
response_py = requests.post(
    "http://localhost:8000/api/jacobi",
    json={
        "matrixA": [[4, 1, 1], [1, 5, 2], [1, 2, 3]],
        "vectorB": [2, -6, -4]
    }
)
print("Python:", response_py.json())

# Java backend
response_java = requests.post(
    "http://localhost:8080/api/jacobi",
    json={
        "matrixA": [[4, 1, 1], [1, 5, 2], [1, 2, 3]],
        "vectorB": [2, -6, -4]
    }
)
print("Java:", response_java.json())
```

## Troubleshooting

### Port Already in Use

**Python (8000):**
```powershell
# Find process
Get-Process -Id (Get-NetTCPConnection -LocalPort 8000).OwningProcess

# Kill process
Stop-Process -Id <PID>
```

**Java (8080):**
```powershell
# Find process
Get-Process -Id (Get-NetTCPConnection -LocalPort 8080).OwningProcess

# Kill process
Stop-Process -Id <PID>
```

### Virtual Environment Not Found

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

### Java Build Errors

```powershell
cd java-backend
mvn clean install -U
```

### Dependencies Not Installed

**Python:**
```powershell
pip install -r requirements.txt
```

**Java:**
```powershell
cd java-backend
mvn dependency:resolve
```

## Configuration

### Python Configuration
Edit `config.json`:
```json
{
  "jacobi": {
    "max_iterations": 100,
    "tolerance": 0.000001
  }
}
```

### Java Configuration
Edit `java-backend/src/main/resources/application.properties`:
```properties
server.port=8080
numerical.jacobi.max-iterations=100
numerical.jacobi.tolerance=0.000001
```

## Stopping the Servers

### If started with `start-dual-backend.ps1`:
- Close both PowerShell windows

### If started manually:
- Press `Ctrl+C` in each terminal

## Next Steps

- Read [README.md](README.md) for detailed documentation
- See [DUAL_BACKEND_INTEGRATION.md](DUAL_BACKEND_INTEGRATION.md) for integration guide
- Check [java-backend/README.md](java-backend/README.md) for Java backend details
- Run tests: `pytest test_numerical_methods.py`

## Support

For issues or questions:
1. Check the documentation in this repository
2. Review the error logs in the terminal windows
3. Open an issue on GitHub

Happy Computing! 🔢
