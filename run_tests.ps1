# Quick Test Script
# This script runs all tests to verify the installation

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Running Numerical Methods Tests" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

Write-Host "Installing test dependencies..." -ForegroundColor Yellow
pip install pytest numpy -q

Write-Host ""
Write-Host "Running tests..." -ForegroundColor Yellow
Write-Host ""

pytest test_numerical_methods.py -v --tb=short

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
