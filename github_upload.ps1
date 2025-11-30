# GitHub Repository Upload Script (PowerShell)
# This script initializes a git repository and prepares it for upload to GitHub

Write-Host "=========================================" -ForegroundColor Cyan
Write-Host "  Numerical Methods Calculator" -ForegroundColor Cyan
Write-Host "  GitHub Repository Initialization" -ForegroundColor Cyan
Write-Host "=========================================" -ForegroundColor Cyan
Write-Host ""

# Step 1: Initialize Git repository
Write-Host "Step 1: Initializing Git repository..." -ForegroundColor Yellow
git init
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Error: Failed to initialize Git repository" -ForegroundColor Red
    exit 1
}
Write-Host "✅ Git repository initialized" -ForegroundColor Green
Write-Host ""

# Step 2: Add all files
Write-Host "Step 2: Adding files to Git..." -ForegroundColor Yellow
git add .
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Error: Failed to add files" -ForegroundColor Red
    exit 1
}
Write-Host "✅ Files added to staging area" -ForegroundColor Green
Write-Host ""

# Step 3: Create initial commit
Write-Host "Step 3: Creating initial commit..." -ForegroundColor Yellow
git commit -m "Initial commit: Numerical Methods Calculator v1.0.0

- Implemented 5 numerical methods (Jacobi, Regula-Falsi, Forward/Backward/Central FD)
- FastAPI backend with async support
- HTML+CSS responsive web interface
- RESTful API endpoints
- Comprehensive test suite (40+ tests)
- Professional documentation
- CI/CD with GitHub Actions
- MIT License

Repository: https://github.com/horysheeet/NumericalMethods"

if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Error: Failed to create commit" -ForegroundColor Red
    exit 1
}
Write-Host "✅ Initial commit created" -ForegroundColor Green
Write-Host ""

# Step 4: Set default branch to main
Write-Host "Step 4: Setting default branch to 'main'..." -ForegroundColor Yellow
git branch -M main
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Error: Failed to rename branch" -ForegroundColor Red
    exit 1
}
Write-Host "✅ Default branch set to 'main'" -ForegroundColor Green
Write-Host ""

# Step 5: Instructions for adding remote
Write-Host "=========================================" -ForegroundColor Cyan
Write-Host "  Next Steps:" -ForegroundColor Cyan
Write-Host "=========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Repository: https://github.com/horysheeet/NumericalMethods" -ForegroundColor Cyan
Write-Host ""
Write-Host "1. Add the remote repository:" -ForegroundColor White
Write-Host "   git remote add origin https://github.com/horysheeet/NumericalMethods.git" -ForegroundColor Yellow
Write-Host ""
Write-Host "2. Push to GitHub:" -ForegroundColor White
Write-Host "   git push -u origin main" -ForegroundColor Yellow
Write-Host ""
Write-Host "Note: If the repository already has commits, you may need to:" -ForegroundColor Gray
Write-Host "   git pull origin main --rebase" -ForegroundColor Yellow
Write-Host "   git push -u origin main" -ForegroundColor Yellow
Write-Host ""

# Repository Statistics
Write-Host "=========================================" -ForegroundColor Cyan
Write-Host "  Repository Statistics:" -ForegroundColor Cyan
Write-Host "=========================================" -ForegroundColor Cyan

$totalFiles = (git ls-files).Count
$pythonFiles = (git ls-files | Select-String -Pattern '\.py$').Count
$htmlFiles = (git ls-files | Select-String -Pattern '\.html$').Count
$cssFiles = (git ls-files | Select-String -Pattern '\.css$').Count

Write-Host "Total files tracked: $totalFiles" -ForegroundColor White
Write-Host "Python files: $pythonFiles" -ForegroundColor White
Write-Host "HTML templates: $htmlFiles" -ForegroundColor White
Write-Host "CSS files: $cssFiles" -ForegroundColor White
Write-Host ""

# Show git status
Write-Host "Current Git status:" -ForegroundColor Yellow
git status
Write-Host ""

# Optional topics
Write-Host "=========================================" -ForegroundColor Cyan
Write-Host "  Optional: Add Repository Topics" -ForegroundColor Cyan
Write-Host "=========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "On GitHub, add these topics to your repository:" -ForegroundColor White
Write-Host "  - python" -ForegroundColor Gray
Write-Host "  - fastapi" -ForegroundColor Gray
Write-Host "  - numerical-methods" -ForegroundColor Gray
Write-Host "  - numerical-analysis" -ForegroundColor Gray
Write-Host "  - scientific-computing" -ForegroundColor Gray
Write-Host "  - web-application" -ForegroundColor Gray
Write-Host "  - calculator" -ForegroundColor Gray
Write-Host "  - education" -ForegroundColor Gray
Write-Host ""

Write-Host "✅ Repository prepared for GitHub upload!" -ForegroundColor Green
Write-Host "Follow the steps above to complete the upload." -ForegroundColor White
