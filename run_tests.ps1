# Quick Test Script
# This script runs all tests to verify the installation

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Running Numerical Methods Tests" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

Write-Host "Installing test dependencies..." -ForegroundColor Yellow

# Choose Python launcher: try 'python', then 'py -3'
$pythonCmd = $null
if (Get-Command python -ErrorAction SilentlyContinue) {
    $pythonCmd = "python"
} elseif (Get-Command py -ErrorAction SilentlyContinue) {
    $pythonCmd = "py -3"
}

if (-not $pythonCmd) {
    Write-Host "ERROR: Python not found on PATH. Please install Python 3.8+ and ensure it's available as 'python' or 'py' in your PATH." -ForegroundColor Red
    Write-Host "Visit https://python.org/downloads or use winget: 'winget install Python.Python.3'" -ForegroundColor Yellow
    exit 1
}

# Use the chosen launcher to run pip (ensures we invoke the same Python interpreter)
& $pythonCmd -m pip install --upgrade pip -q
& $pythonCmd -m pip install -r requirements.txt -q
& $pythonCmd -m pip install -r requirements-dev.txt -q

Write-Host ""
Write-Host "Running tests..." -ForegroundColor Yellow
Write-Host ""

& $pythonCmd -m pytest test_numerical_methods.py -v --tb=short

if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "========================================" -ForegroundColor Green
    Write-Host "  ✓ All Tests Passed!" -ForegroundColor Green
    Write-Host "========================================" -ForegroundColor Green
} else {
    Write-Host ""
    Write-Host "========================================" -ForegroundColor Red
    Write-Host "  ✗ Some Tests Failed" -ForegroundColor Red
    Write-Host "========================================" -ForegroundColor Red
}
