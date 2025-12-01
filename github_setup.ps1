# GitHub Repository Setup and Push Script
# This script creates a new GitHub repository and pushes all code

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  GitHub Repository Setup" -ForegroundColor Cyan
Write-Host "  numerical-methods-hybrid-system" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check if gh CLI is installed
if (-Not (Get-Command gh -ErrorAction SilentlyContinue)) {
    Write-Host "[ERROR] GitHub CLI (gh) is not installed!" -ForegroundColor Red
    Write-Host "Please install it from: https://cli.github.com/" -ForegroundColor Yellow
    Write-Host "Or use: winget install --id GitHub.cli" -ForegroundColor Yellow
    exit 1
}

# Check if user is authenticated
$authStatus = gh auth status 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "[INFO] Not authenticated with GitHub. Logging in..." -ForegroundColor Yellow
    gh auth login
    if ($LASTEXITCODE -ne 0) {
        Write-Host "[ERROR] GitHub authentication failed!" -ForegroundColor Red
        exit 1
    }
}

Write-Host "[SUCCESS] GitHub CLI is ready!" -ForegroundColor Green
Write-Host ""

# Repository details
$repoName = "numerical-methods-hybrid-system"
$repoDescription = "Production-ready numerical methods calculator with dual backend (Python FastAPI + Java Spring Boot)"
$repoVisibility = "public"

Write-Host "[INFO] Repository Name: $repoName" -ForegroundColor Cyan
Write-Host "[INFO] Description: $repoDescription" -ForegroundColor Cyan
Write-Host "[INFO] Visibility: $repoVisibility" -ForegroundColor Cyan
Write-Host ""

# Ask for confirmation
$confirmation = Read-Host "Create new GitHub repository? (yes/no)"
if ($confirmation -ne "yes") {
    Write-Host "[CANCELLED] Repository creation cancelled." -ForegroundColor Yellow
    exit 0
}

# Create GitHub repository
Write-Host ""
Write-Host "[1/6] Creating GitHub repository..." -ForegroundColor Green
gh repo create $repoName --$repoVisibility --description "$repoDescription" --source=. --remote=origin-new

if ($LASTEXITCODE -ne 0) {
    Write-Host "[ERROR] Failed to create repository!" -ForegroundColor Red
    Write-Host "The repository might already exist. Checking..." -ForegroundColor Yellow
    
    # Check if repo exists
    $repoCheck = gh repo view "horysheeet/$repoName" 2>&1
    if ($LASTEXITCODE -eq 0) {
        Write-Host "[INFO] Repository already exists! Adding as remote..." -ForegroundColor Yellow
        git remote add origin-new "https://github.com/horysheeet/$repoName.git" 2>&1
    } else {
        Write-Host "[ERROR] Could not create or find repository!" -ForegroundColor Red
        exit 1
    }
}

Write-Host "[SUCCESS] Repository created/found!" -ForegroundColor Green
Write-Host ""

# Stage all files
Write-Host "[2/6] Staging all files..." -ForegroundColor Green
git add -A

if ($LASTEXITCODE -ne 0) {
    Write-Host "[ERROR] Failed to stage files!" -ForegroundColor Red
    exit 1
}

Write-Host "[SUCCESS] Files staged!" -ForegroundColor Green
Write-Host ""

# Commit changes
Write-Host "[3/6] Creating commit..." -ForegroundColor Green
$commitMessage = @"
feat: Complete dual backend implementation with CI/CD

- Add Java Spring Boot backend (port 8080)
- Implement all 5 numerical methods in Java
- Add REST controllers with validation
- Create comprehensive documentation
- Add CI/CD workflows (Python, Java, Deploy)
- Configure Render deployment for both backends
- Add Dockerfiles for containerization
- Update .gitignore for Java/Maven
- Create deployment automation scripts
- Add health check endpoints
- Configure CORS for cross-origin requests
- Add complete API documentation
- Create GitHub Pages documentation site

This commit establishes a production-ready dual backend system
with automated testing, deployment, and comprehensive documentation.
"@

git commit -m "$commitMessage"

if ($LASTEXITCODE -ne 0) {
    Write-Host "[WARN] No changes to commit or commit failed" -ForegroundColor Yellow
}

Write-Host "[SUCCESS] Commit created!" -ForegroundColor Green
Write-Host ""

# Create main branch if not exists
Write-Host "[4/6] Ensuring main branch exists..." -ForegroundColor Green
$currentBranch = git branch --show-current

if ($currentBranch -ne "main") {
    Write-Host "[INFO] Current branch: $currentBranch" -ForegroundColor Yellow
    Write-Host "[INFO] Creating/switching to main branch..." -ForegroundColor Yellow
    
    git checkout -b main 2>&1
    if ($LASTEXITCODE -ne 0) {
        git checkout main 2>&1
    }
}

Write-Host "[SUCCESS] On main branch!" -ForegroundColor Green
Write-Host ""

# Push to new repository
Write-Host "[5/6] Pushing to GitHub..." -ForegroundColor Green
Write-Host "This may take a moment..." -ForegroundColor Gray

git push -u origin-new main --force

if ($LASTEXITCODE -ne 0) {
    Write-Host "[ERROR] Failed to push to GitHub!" -ForegroundColor Red
    Write-Host "Trying alternative method..." -ForegroundColor Yellow
    
    git push -u origin-new main 2>&1
    
    if ($LASTEXITCODE -ne 0) {
        Write-Host "[ERROR] Push failed! Please check your credentials and try manually." -ForegroundColor Red
        exit 1
    }
}

Write-Host "[SUCCESS] Code pushed to GitHub!" -ForegroundColor Green
Write-Host ""

# Set repository topics
Write-Host "[6/6] Adding repository topics..." -ForegroundColor Green
gh repo edit "horysheeet/$repoName" --add-topic "numerical-methods,python,java,fastapi,spring-boot,rest-api,dual-backend,calculator,mathematics,algorithms"

Write-Host "[SUCCESS] Topics added!" -ForegroundColor Green
Write-Host ""

# Display summary
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Setup Complete!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Repository URL:" -ForegroundColor Yellow
Write-Host "https://github.com/horysheeet/$repoName" -ForegroundColor White
Write-Host ""
Write-Host "Next Steps:" -ForegroundColor Yellow
Write-Host "1. Go to https://render.com and deploy both backends" -ForegroundColor White
Write-Host "2. Enable GitHub Pages in repository settings" -ForegroundColor White
Write-Host "3. Update README.md with actual deployment URLs" -ForegroundColor White
Write-Host "4. Set up GitHub Secrets for CI/CD (if needed)" -ForegroundColor White
Write-Host ""
Write-Host "Documentation:" -ForegroundColor Yellow
Write-Host "- README.md - Main documentation" -ForegroundColor White
Write-Host "- QUICKSTART_DUAL_BACKEND.md - Quick start guide" -ForegroundColor White
Write-Host "- DEPLOYMENT_GUIDE.md - Deployment instructions" -ForegroundColor White
Write-Host ""
Write-Host "Happy coding! 🚀" -ForegroundColor Green
