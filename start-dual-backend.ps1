# Dual Backend Startup Script
# This script starts both Python and Java backends in separate windows

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Numerical Methods Calculator" -ForegroundColor Cyan
Write-Host "  Dual Backend Startup" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check if Python virtual environment exists
if (-Not (Test-Path ".venv\Scripts\python.exe")) {
    Write-Host "[ERROR] Python virtual environment not found!" -ForegroundColor Red
    Write-Host "Please run: python -m venv .venv" -ForegroundColor Yellow
    Write-Host "Then: .venv\Scripts\activate" -ForegroundColor Yellow
    Write-Host "And: pip install -r requirements.txt" -ForegroundColor Yellow
    exit 1
}

# Check if Java backend is built
if (-Not (Test-Path "java-backend\target\classes")) {
    Write-Host "[WARN] Java backend not built. Building now..." -ForegroundColor Yellow
    Set-Location java-backend
    mvn clean install -DskipTests
    if ($LASTEXITCODE -ne 0) {
        Write-Host "[ERROR] Java backend build failed!" -ForegroundColor Red
        Set-Location ..
        exit 1
    }
    Set-Location ..
    Write-Host "[SUCCESS] Java backend built successfully!" -ForegroundColor Green
}

Write-Host ""
Write-Host "Starting backends..." -ForegroundColor Cyan
Write-Host ""

# Start Python backend in new window
Write-Host "[1/2] Starting Python Backend (Port 8000)..." -ForegroundColor Green
Start-Process powershell -ArgumentList @"
-NoExit
-Command
Write-Host '========================================' -ForegroundColor Cyan;
Write-Host '  Python Backend (FastAPI)' -ForegroundColor Cyan;
Write-Host '  Port: 8000' -ForegroundColor Cyan;
Write-Host '========================================' -ForegroundColor Cyan;
Write-Host '';
Set-Location '$PWD';
.\.venv\Scripts\activate;
Write-Host 'Starting FastAPI server...' -ForegroundColor Green;
python -m uvicorn main:app --reload
"@

Start-Sleep -Seconds 2

# Start Java backend in new window
Write-Host "[2/2] Starting Java Backend (Port 8080)..." -ForegroundColor Green
Start-Process powershell -ArgumentList @"
-NoExit
-Command
Write-Host '========================================' -ForegroundColor Cyan;
Write-Host '  Java Backend (Spring Boot)' -ForegroundColor Cyan;
Write-Host '  Port: 8080' -ForegroundColor Cyan;
Write-Host '========================================' -ForegroundColor Cyan;
Write-Host '';
Set-Location '$PWD\java-backend';
Write-Host 'Starting Spring Boot server...' -ForegroundColor Green;
mvn spring-boot:run
"@

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Both backends are starting!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Python Backend:  http://localhost:8000" -ForegroundColor Yellow
Write-Host "Java Backend:    http://localhost:8080" -ForegroundColor Yellow
Write-Host ""
Write-Host "Wait a few seconds for both servers to initialize..." -ForegroundColor Gray
Write-Host "Check the new windows for status and logs." -ForegroundColor Gray
Write-Host ""
Write-Host "Press any key to exit this launcher..." -ForegroundColor Gray
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
