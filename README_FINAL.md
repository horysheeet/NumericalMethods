# 🔢 Numerical Methods Hybrid System

[![Python CI](https://github.com/horysheeet/numerical-methods-hybrid-system/actions/workflows/python-ci.yml/badge.svg)](https://github.com/horysheeet/numerical-methods-hybrid-system/actions/workflows/python-ci.yml)
[![Java CI](https://github.com/horysheeet/numerical-methods-hybrid-system/actions/workflows/java-ci.yml/badge.svg)](https://github.com/horysheeet/numerical-methods-hybrid-system/actions/workflows/java-ci.yml)
[![Deploy](https://github.com/horysheeet/numerical-methods-hybrid-system/actions/workflows/deploy.yml/badge.svg)](https://github.com/horysheeet/numerical-methods-hybrid-system/actions/workflows/deploy.yml)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![Java Version](https://img.shields.io/badge/java-21%2B-orange.svg)](https://www.oracle.com/java/technologies/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A production-ready web application for solving numerical analysis problems with **dual-backend architecture**. Choose between **Python FastAPI** or **Java Spring Boot** backends, both providing identical functionality through RESTful APIs with a responsive **HTML+CSS** frontend.

## 🌐 Live Deployments

| Service | URL | Status |
|---------|-----|--------|
| **Python Backend** | [numerical-methods-python.onrender.com](https://numerical-methods-python.onrender.com) | 🟢 Live |
| **Java Backend** | [numerical-methods-java.onrender.com](https://numerical-methods-java.onrender.com) | 🟢 Live |
| **Documentation** | [horysheeet.github.io/numerical-methods-hybrid-system](https://horysheeet.github.io/numerical-methods-hybrid-system) | 🟢 Live |

> **Note**: Free tier backends may take 30-60 seconds to wake up on first request.

---

## 📋 Table of Contents

- [Features](#-features)
- [Architecture](#-architecture)
- [Quick Start](#-quick-start)
- [Running Locally](#-running-locally)
- [API Documentation](#-api-documentation)
- [Deployment](#-deployment)
- [CI/CD Pipeline](#-cicd-pipeline)
- [Testing](#-testing)
- [Contributing](#-contributing)
- [License](#-license)

---

## ✨ Features

### 🧮 5 Numerical Methods Implemented

1. **Jacobi Iterative Method** - Solve systems of linear equations Ax = b
2. **Regula-Falsi Method** - Find roots of equations using false position
3. **Forward Finite Difference** - Numerical differentiation (forward)
4. **Backward Finite Difference** - Numerical differentiation (backward)
5. **Central Finite Difference** - Most accurate differentiation (central)

### 🚀 Key Capabilities

- ✅ **Dual Backend Architecture** - Python (port 8000) + Java (port 8080)
- ✅ **Interactive Web Interface** - Responsive HTML+CSS UI
- ✅ **RESTful APIs** - JSON endpoints for all methods (both backends)
- ✅ **Detailed Logging** - Iteration-by-iteration convergence tracking
- ✅ **Error Handling** - Comprehensive validation and error messages
- ✅ **Configuration System** - Centralized config for both backends
- ✅ **Full Test Coverage** - 40+ unit tests (Python)
- ✅ **Production Ready** - Deployed and live on Render
- ✅ **CI/CD Pipeline** - Automated testing and deployment
- ✅ **CORS Enabled** - Cross-origin requests supported

---

## 🏗️ Architecture

### System Overview

```
                    ┌─────────────────────┐
                    │   Web Browser       │
                    │   (Frontend UI)     │
                    └──────────┬──────────┘
                               │
                ┌──────────────┴──────────────┐
                │                             │
                ▼                             ▼
    ┌─────────────────────┐       ┌─────────────────────┐
    │  Python Backend     │       │  Java Backend       │
    │  FastAPI            │       │  Spring Boot        │
    │  Port 8000          │       │  Port 8080          │
    ├─────────────────────┤       ├─────────────────────┤
    │ • HTML Templates    │       │ • REST API Only     │
    │ • REST API          │       │ • Health Checks     │
    │ • 5 Methods         │       │ • 5 Methods         │
    └─────────────────────┘       └─────────────────────┘
```

### Technology Stack

| Component | Python Backend | Java Backend |
|-----------|---------------|--------------|
| **Framework** | FastAPI 0.122.0 | Spring Boot 3.2.0 |
| **Language** | Python 3.13.5 | Java 21 |
| **Server** | Uvicorn | Embedded Tomcat |
| **Validation** | Pydantic | Jakarta Bean Validation |
| **Build Tool** | pip | Maven |
| **Testing** | pytest | JUnit (planned) |
| **Deployment** | Render | Render |

---

## 🚀 Quick Start

### Prerequisites

**For Python Backend:**
- Python 3.8 or higher
- pip package manager

**For Java Backend:**
- Java 21 or higher
- Maven 3.6+

### Installation

```bash
# Clone the repository
git clone https://github.com/horysheeet/numerical-methods-hybrid-system.git
cd numerical-methods-hybrid-system

# Python setup
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/Mac
pip install -r requirements.txt

# Java setup
cd java-backend
mvn clean install
cd ..
```

---

## 💻 Running Locally

### Option 1: Automated Startup (Both Backends)

**Windows:**
```powershell
.\start-dual-backend.ps1
```

**Linux/Mac:**
```bash
./start-dual-backend.sh  # Create this script if needed
```

### Option 2: Manual Startup

**Terminal 1 - Python Backend:**
```bash
# Windows
.venv\Scripts\activate
python -m uvicorn main:app --reload

# Linux/Mac
source .venv/bin/activate
uvicorn main:app --reload
```
Access: http://localhost:8000

**Terminal 2 - Java Backend:**
```bash
cd java-backend
mvn spring-boot:run
```
Access: http://localhost:8080

### Option 3: Using Docker

**Python Backend:**
```bash
docker build -t numerical-methods-python .
docker run -p 8000:8000 numerical-methods-python
```

**Java Backend:**
```bash
cd java-backend
docker build -t numerical-methods-java .
docker run -p 8080:8080 numerical-methods-java
```

---

## 📡 API Documentation

### Python Backend Endpoints

**Base URL:** `http://localhost:8000` (local) | `https://numerical-methods-python.onrender.com` (prod)

#### Web Pages
- `GET /` - Home page
- `GET /jacobi` - Jacobi method interface
- `GET /regula-falsi` - Regula-Falsi interface
- `GET /forward-fd` - Forward difference interface
- `GET /backward-fd` - Backward difference interface
- `GET /center-fd` - Central difference interface

#### REST API
- `POST /api/jacobi` - Jacobi computation
- `POST /api/regula-falsi` - Root finding
- `POST /api/forward-fd` - Forward differentiation
- `POST /api/backward-fd` - Backward differentiation
- `POST /api/center-fd` - Central differentiation

### Java Backend Endpoints

**Base URL:** `http://localhost:8080` (local) | `https://numerical-methods-java.onrender.com` (prod)

#### REST API
- `POST /api/jacobi` - Jacobi computation
- `POST /api/regula-falsi` - Root finding
- `POST /api/finite-difference/forward` - Forward differentiation
- `POST /api/finite-difference/backward` - Backward differentiation
- `POST /api/finite-difference/central` - Central differentiation

#### Health Checks
- `GET /api/jacobi/health`
- `GET /api/regula-falsi/health`
- `GET /api/finite-difference/health`

### Example Request (Jacobi Method)

**Request:**
```bash
curl -X POST https://numerical-methods-python.onrender.com/api/jacobi \
  -H "Content-Type: application/json" \
  -d '{
    "matrixA": [[4, 1, 1], [1, 5, 2], [1, 2, 3]],
    "vectorB": [2, -6, -4],
    "maxIterations": 100,
    "tolerance": 0.000001
  }'
```

**Response:**
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

---

## 🌍 Deployment

### Deploying to Render (Recommended - Free Tier)

Both backends are configured for automatic deployment to Render.

#### Step 1: Create Render Account
1. Sign up at [render.com](https://render.com)
2. Connect your GitHub account

#### Step 2: Deploy Python Backend
1. Click "New +" → "Web Service"
2. Connect repository: `numerical-methods-hybrid-system`
3. Settings:
   - **Name**: `numerical-methods-python`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
   - **Plan**: `Free`
4. Click "Create Web Service"

#### Step 3: Deploy Java Backend
1. Click "New +" → "Web Service"
2. Connect repository: `numerical-methods-hybrid-system`
3. Settings:
   - **Name**: `numerical-methods-java`
   - **Root Directory**: `java-backend`
   - **Environment**: `Java`
   - **Build Command**: `mvn clean install -DskipTests`
   - **Start Command**: `java -Dserver.port=$PORT -jar target/*.jar`
   - **Plan**: `Free`
4. Click "Create Web Service"

#### Step 4: Enable Auto-Deploy
Both services will automatically deploy on push to `main` branch.

### Alternative Free Deployment Options

<details>
<summary><strong>Railway</strong></summary>

```bash
# Install Railway CLI
npm install -g @railway/cli

# Login
railway login

# Deploy Python backend
railway init
railway up

# Deploy Java backend
cd java-backend
railway init
railway up
```
</details>

<details>
<summary><strong>Fly.io</strong></summary>

```bash
# Install Fly CLI
# See: https://fly.io/docs/hands-on/install-flyctl/

# Python backend
flyctl launch --name numerical-methods-python
flyctl deploy

# Java backend
cd java-backend
flyctl launch --name numerical-methods-java
flyctl deploy
```
</details>

---

## 🔄 CI/CD Pipeline

### GitHub Actions Workflows

The project includes three automated workflows:

#### 1. Python CI (`python-ci.yml`)
- **Triggers**: Push to `main`, PRs affecting Python files
- **Actions**:
  - Test on Python 3.9, 3.10, 3.11, 3.12, 3.13
  - Run linting (flake8)
  - Execute tests (pytest)
  - Generate coverage report
  - Security checks (bandit, safety)

#### 2. Java CI (`java-ci.yml`)
- **Triggers**: Push to `main`, PRs affecting Java files
- **Actions**:
  - Test on Java 17, 21
  - Build with Maven
  - Run tests
  - Generate coverage
  - Code quality checks (Checkstyle, SpotBugs)

#### 3. Deployment (`deploy.yml`)
- **Triggers**: Push to `main`, manual dispatch
- **Actions**:
  - Deploy Python backend to Render
  - Deploy Java backend to Render
  - Deploy documentation to GitHub Pages

### Setting Up CI/CD

1. **Enable GitHub Actions**:
   - Go to repository → Settings → Actions → General
   - Allow all actions

2. **Add Secrets** (if needed):
   - `RENDER_API_KEY`: Your Render API key (optional, Render auto-deploys from GitHub)

3. **Enable GitHub Pages**:
   - Settings → Pages
   - Source: GitHub Actions

---

## 🧪 Testing

### Python Tests

```bash
# Run all tests
pytest test_numerical_methods.py -v

# With coverage
pytest test_numerical_methods.py -v --cov=. --cov-report=html

# View coverage
open htmlcov/index.html  # or start htmlcov/index.html on Windows
```

**Coverage**: 40+ tests, 90%+ code coverage

### Java Tests

```bash
cd java-backend
mvn test

# With coverage
mvn test jacoco:report
```

### Manual API Testing

**Using cURL:**
```bash
# Test Python backend
curl http://localhost:8000/api/jacobi \
  -X POST -H "Content-Type: application/json" \
  -d '{"matrixA":[[4,1,1],[1,5,2],[1,2,3]],"vectorB":[2,-6,-4]}'

# Test Java backend
curl http://localhost:8080/api/jacobi \
  -X POST -H "Content-Type: application/json" \
  -d '{"matrixA":[[4,1,1],[1,5,2],[1,2,3]],"vectorB":[2,-6,-4]}'
```

---

## 📚 Documentation

- **[Quick Start Guide](QUICKSTART_DUAL_BACKEND.md)** - Get started in minutes
- **[Integration Guide](DUAL_BACKEND_INTEGRATION.md)** - Dual backend architecture
- **[Java Backend Docs](java-backend/README.md)** - Spring Boot implementation
- **[Deployment Guide](DEPLOYMENT_GUIDE.md)** - Deploy to various platforms
- **[Contributing Guide](CONTRIBUTING.md)** - How to contribute
- **[Project Summary](PROJECT_COMPLETE.md)** - Complete overview

---

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Development Workflow

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests (`pytest` for Python, `mvn test` for Java)
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

### Areas for Contribution

- Add more numerical methods
- Improve frontend UI/UX
- Add Java unit tests
- Enhance documentation
- Performance optimizations
- Additional deployment platforms

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 🔗 Links

- **GitHub Repository**: https://github.com/horysheeet/numerical-methods-hybrid-system
- **Python Backend (Live)**: https://numerical-methods-python.onrender.com
- **Java Backend (Live)**: https://numerical-methods-java.onrender.com
- **Documentation Site**: https://horysheeet.github.io/numerical-methods-hybrid-system
- **Issue Tracker**: https://github.com/horysheeet/numerical-methods-hybrid-system/issues

---

## 📊 Project Statistics

| Metric | Count |
|--------|-------|
| **Total Files** | 50+ |
| **Lines of Code** | ~6,000+ |
| **Python Files** | 18 |
| **Java Files** | 15 |
| **Test Cases** | 40+ |
| **Documentation Files** | 10 |
| **Supported Methods** | 5 |

---

## 🙏 Acknowledgments

- FastAPI for the excellent Python web framework
- Spring Boot for the robust Java framework
- Render for free tier hosting
- GitHub for CI/CD infrastructure

---

## 📞 Support

For questions or issues:

1. Check the [documentation](https://horysheeet.github.io/numerical-methods-hybrid-system)
2. Review [existing issues](https://github.com/horysheeet/numerical-methods-hybrid-system/issues)
3. Open a [new issue](https://github.com/horysheeet/numerical-methods-hybrid-system/issues/new)

---

**Built with ❤️ using Python FastAPI and Java Spring Boot**

**Happy Computing! 🔢**
