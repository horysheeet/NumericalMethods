# Manual GitHub Repository Setup Script
# This script prepares the repository for pushing to GitHub

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Numerical Methods Hybrid System Setup" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Step 1: Stage all files
Write-Host "[1/6] Staging all files..." -ForegroundColor Yellow
git add .

if ($LASTEXITCODE -eq 0) {
    Write-Host "Files staged successfully" -ForegroundColor Green
} else {
    Write-Host "Error staging files" -ForegroundColor Red
    exit 1
}

# Step 2: Commit changes
Write-Host ""
Write-Host "[2/6] Committing changes..." -ForegroundColor Yellow
git commit -m "Complete Dual Backend Implementation with CI/CD" -m "Features: Python FastAPI backend, Java Spring Boot backend, Docker containerization, GitHub Actions CI/CD, automated deployment to Render" -m "Technologies: Python 3.13, Java 21, FastAPI, Spring Boot, Docker, GitHub Actions" -m "Numerical Methods: Jacobi, Regula-Falsi, Finite Difference methods"

if ($LASTEXITCODE -eq 0) {
    Write-Host "Changes committed successfully" -ForegroundColor Green
} else {
    Write-Host "Error committing changes" -ForegroundColor Red
    exit 1
}

# Step 3: Create main branch
Write-Host ""
Write-Host "[3/6] Creating main branch..." -ForegroundColor Yellow
git checkout -b main 2>$null

if ($LASTEXITCODE -eq 0) {
    Write-Host "Main branch created" -ForegroundColor Green
} else {
    Write-Host "Already on main branch or branch exists" -ForegroundColor Green
}

# Step 4: Instructions for creating GitHub repository
Write-Host ""
Write-Host "[4/6] Next Steps - Create GitHub Repository" -ForegroundColor Cyan
Write-Host "==========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Please follow these steps to create the repository on GitHub:" -ForegroundColor White
Write-Host ""
Write-Host "1. Go to: https://github.com/new" -ForegroundColor Yellow
Write-Host "2. Repository name: numerical-methods-hybrid-system" -ForegroundColor Yellow
Write-Host "3. Description: Numerical Methods Calculator with Dual Backend (Python FastAPI + Java Spring Boot)" -ForegroundColor Yellow
Write-Host "4. Visibility: Public" -ForegroundColor Yellow
Write-Host "5. DO NOT initialize with README, .gitignore, or license (we already have them)" -ForegroundColor Red
Write-Host "6. Click Create repository" -ForegroundColor Yellow
Write-Host ""
Write-Host "Press Enter after you have created the repository..." -ForegroundColor Green
$null = Read-Host

# Step 5: Add remote and push
Write-Host ""
Write-Host "[5/6] Configuring remote and pushing..." -ForegroundColor Yellow
Write-Host ""
Write-Host "Enter your GitHub username: " -ForegroundColor Cyan -NoNewline
$username = Read-Host

$repoUrl = "https://github.com/$username/numerical-methods-hybrid-system.git"

# Remove existing origin if it exists
git remote remove origin 2>$null

# Add new origin
git remote add origin $repoUrl
Write-Host "Remote added: $repoUrl" -ForegroundColor Green

# Push to main
Write-Host ""
Write-Host "Pushing to GitHub..." -ForegroundColor Yellow
git push -u origin main

if ($LASTEXITCODE -eq 0) {
    Write-Host "Successfully pushed to GitHub!" -ForegroundColor Green
} else {
    Write-Host "Error pushing to GitHub" -ForegroundColor Red
    Write-Host "You may need to authenticate. Try running:" -ForegroundColor Yellow
    Write-Host "git push -u origin main" -ForegroundColor Yellow
    exit 1
}

# Step 6: Final instructions
Write-Host ""
Write-Host "[6/6] Final Steps" -ForegroundColor Cyan
Write-Host "=================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Repository created and pushed successfully!" -ForegroundColor Green
Write-Host ""
Write-Host "Next steps:" -ForegroundColor White
Write-Host ""
Write-Host "1. Deploy to Render:" -ForegroundColor Yellow
Write-Host "   - Go to https://render.com" -ForegroundColor White
Write-Host "   - Sign in with GitHub" -ForegroundColor White
Write-Host "   - Click New + > Web Service" -ForegroundColor White
Write-Host "   - Connect your repository: $username/numerical-methods-hybrid-system" -ForegroundColor White
Write-Host "   - Select Docker environment" -ForegroundColor White
Write-Host "   - Render will automatically detect render.yaml and deploy both backends" -ForegroundColor White
Write-Host ""
Write-Host "2. Enable GitHub Pages:" -ForegroundColor Yellow
Write-Host "   - Go to: https://github.com/$username/numerical-methods-hybrid-system/settings/pages" -ForegroundColor White
Write-Host "   - Source: GitHub Actions" -ForegroundColor White
Write-Host "   - Wait for deployment (check Actions tab)" -ForegroundColor White
Write-Host ""
Write-Host "3. Monitor Deployments:" -ForegroundColor Yellow
Write-Host "   - GitHub Actions: https://github.com/$username/numerical-methods-hybrid-system/actions" -ForegroundColor White
Write-Host "   - Render Dashboard: https://dashboard.render.com" -ForegroundColor White
Write-Host ""
Write-Host "Repository URL: https://github.com/$username/numerical-methods-hybrid-system" -ForegroundColor Cyan
Write-Host ""
Write-Host "Setup complete! Your project is now live on GitHub!" -ForegroundColor Green
Write-Host ""
