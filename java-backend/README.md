# Java Backend - Numerical Methods Calculator

## Overview
This Java Spring Boot backend provides REST API endpoints for numerical computation methods. It runs independently from the Python FastAPI backend and can be accessed from the same frontend.

## Architecture
- **Framework**: Spring Boot 3.2.0
- **Java Version**: 21
- **Build Tool**: Maven
- **Default Port**: 8080 (configurable in `application.properties`)

## Project Structure
```
java-backend/
├── pom.xml                         # Maven configuration
├── src/
│   ├── main/
│   │   ├── java/com/numerical/calculator/
│   │   │   ├── NumericalMethodsApplication.java    # Main Spring Boot application
│   │   │   ├── config/
│   │   │   │   └── CorsConfig.java                 # CORS configuration
│   │   │   ├── controller/
│   │   │   │   ├── JacobiController.java           # Jacobi method REST API
│   │   │   │   ├── RegulaFalsiController.java      # Regula-Falsi REST API
│   │   │   │   └── FiniteDifferenceController.java # Finite difference REST API
│   │   │   ├── model/
│   │   │   │   ├── JacobiRequest.java              # Jacobi request DTO
│   │   │   │   ├── RegulaFalsiRequest.java         # Regula-Falsi request DTO
│   │   │   │   ├── FiniteDifferenceRequest.java    # Finite difference request DTO
│   │   │   │   └── NumericalResponse.java          # Unified response DTO
│   │   │   └── service/
│   │   │       ├── JacobiService.java              # Jacobi computation service
│   │   │       ├── RegulaFalsiService.java         # Regula-Falsi computation service
│   │   │       └── FiniteDifferenceService.java    # Finite difference computation service
│   │   └── resources/
│   │       └── application.properties              # Application configuration
│   └── test/
│       └── java/com/numerical/calculator/          # Unit tests (to be added)
└── target/                                         # Compiled classes (generated)
```

## API Endpoints

All endpoints are prefixed with `/api` and support CORS from `localhost:8000`.

### 1. Jacobi Method
**Endpoint**: `POST /api/jacobi`

**Request Body**:
```json
{
  "matrixA": [[4, 1, 1], [1, 5, 2], [1, 2, 3]],
  "vectorB": [2, -6, -4],
  "initialGuess": [0, 0, 0],
  "maxIterations": 100,
  "tolerance": 0.000001
}
```

**Response**:
```json
{
  "success": true,
  "result": [1.0000, -2.0000, 1.0000],
  "message": "Converged after 15 iterations",
  "iterations": 15,
  "error": 0.0000008,
  "iterationLog": [...]
}
```

### 2. Regula-Falsi Method
**Endpoint**: `POST /api/regula-falsi`

**Request Body**:
```json
{
  "function": "x**3 - 2*x - 5",
  "a": 2,
  "b": 3,
  "maxIterations": 100,
  "tolerance": 0.000001
}
```

**Response**:
```json
{
  "success": true,
  "result": 2.094551,
  "message": "Converged after 8 iterations",
  "iterations": 8,
  "error": 0.0000005,
  "iterationLog": [...]
}
```

### 3. Finite Difference Methods
**Endpoints**: 
- `POST /api/finite-difference/forward`
- `POST /api/finite-difference/backward`
- `POST /api/finite-difference/central`

**Request Body**:
```json
{
  "function": "x**2 + 3*x + 2",
  "xValues": [1.0, 2.0, 3.0],
  "order": 1,
  "stepSize": 0.01
}
```

**Response**:
```json
{
  "success": true,
  "result": [
    {"x": 1.0, "derivative": 5.01, "order": 1},
    {"x": 2.0, "derivative": 7.01, "order": 1},
    {"x": 3.0, "derivative": 9.01, "order": 1}
  ],
  "message": "Forward difference computed for 3 point(s)"
}
```

### Health Check Endpoints
- `GET /api/jacobi/health`
- `GET /api/regula-falsi/health`
- `GET /api/finite-difference/health`

## Building and Running

### Prerequisites
- Java 21 or higher
- Maven 3.6+

### Build the Project
```bash
cd java-backend
mvn clean install
```

### Run the Application
```bash
mvn spring-boot:run
```

Or run the compiled JAR:
```bash
java -jar target/numerical-methods-calculator-0.0.1-SNAPSHOT.jar
```

### Configuration
Edit `src/main/resources/application.properties` to change:
- Server port (default: 8080)
- Algorithm parameters (max iterations, tolerance, step size)
- Logging levels

## Dual Backend Architecture

This Java backend works alongside the Python FastAPI backend:

1. **Python Backend** (port 8000): Original implementation with HTML templates
2. **Java Backend** (port 8080): REST API only, same functionality

### Frontend Integration
The Python frontend can be updated to select which backend to use:

```html
<select id="backend-selector">
  <option value="http://localhost:8000">Python Backend</option>
  <option value="http://localhost:8080">Java Backend</option>
</select>
```

JavaScript can dynamically switch API endpoints based on selection.

## Dependencies
- **Spring Boot Starter Web**: REST API framework
- **Spring Boot Starter Validation**: Request validation
- **Spring Boot DevTools**: Development hot-reload
- **Lombok**: Reduce boilerplate code
- **Nashorn Script Engine**: JavaScript evaluation for mathematical functions

## Error Handling
All services return `NumericalResponse` objects with:
- `success`: boolean indicating if computation succeeded
- `result`: computation result (can be number, array, or object)
- `message`: human-readable status message
- `error`: error value (for iterative methods)
- `iterations`: number of iterations performed
- `iterationLog`: detailed log of each iteration

## Testing
Unit tests can be added to `src/test/java/com/numerical/calculator/`.

Run tests:
```bash
mvn test
```

## CORS Configuration
The `CorsConfig.java` allows requests from:
- http://localhost:8000
- http://127.0.0.1:8000
- http://0.0.0.0:8000

For production, restrict origins in `CorsConfig.java`.

## Future Enhancements
- Add comprehensive unit tests
- Implement additional numerical methods (Newton-Raphson, Simpson's rule, etc.)
- Add API documentation with Swagger/OpenAPI
- Implement request caching for performance
- Add authentication/authorization
- Database integration for result storage
