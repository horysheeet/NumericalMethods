#!/bin/bash

# GitHub Repository Upload Script
# This script initializes a git repository and prepares it for upload to GitHub

echo "========================================="
echo "  Numerical Methods Calculator"
echo "  GitHub Repository Initialization"
echo "========================================="
echo ""

# Step 1: Initialize Git repository
echo "Step 1: Initializing Git repository..."
git init
if [ $? -ne 0 ]; then
    echo "❌ Error: Failed to initialize Git repository"
    exit 1
fi
echo "✅ Git repository initialized"
echo ""

# Step 2: Add all files
echo "Step 2: Adding files to Git..."
git add .
if [ $? -ne 0 ]; then
    echo "❌ Error: Failed to add files"
    exit 1
fi
echo "✅ Files added to staging area"
echo ""

# Step 3: Create initial commit
echo "Step 3: Creating initial commit..."
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

if [ $? -ne 0 ]; then
    echo "❌ Error: Failed to create commit"
    exit 1
fi
echo "✅ Initial commit created"
echo ""

# Step 4: Set default branch to main
echo "Step 4: Setting default branch to 'main'..."
git branch -M main
if [ $? -ne 0 ]; then
    echo "❌ Error: Failed to rename branch"
    exit 1
fi
echo "✅ Default branch set to 'main'"
echo ""

# Step 5: Instructions for adding remote
echo "========================================="
echo "  Next Steps:"
echo "========================================="
echo ""
echo "Repository: https://github.com/horysheeet/NumericalMethods"
echo ""
echo "1. Add the remote repository:"
echo "   git remote add origin https://github.com/horysheeet/NumericalMethods.git"
echo ""
echo "2. Push to GitHub:"
echo "   git push -u origin main"
echo ""
echo "Note: If the repository already has commits, you may need to:"
echo "   git pull origin main --rebase"
echo "   git push -u origin main"
echo ""
echo "========================================="
echo "  Repository Statistics:"
echo "========================================="

# Count files
total_files=$(git ls-files | wc -l)
python_files=$(git ls-files | grep '\.py$' | wc -l)
html_files=$(git ls-files | grep '\.html$' | wc -l)
css_files=$(git ls-files | grep '\.css$' | wc -l)

echo "Total files tracked: $total_files"
echo "Python files: $python_files"
echo "HTML templates: $html_files"
echo "CSS files: $css_files"
echo ""

# Show git status
echo "Current Git status:"
git status
echo ""

echo "========================================="
echo "  Optional: Add Repository Topics"
echo "========================================="
echo ""
echo "On GitHub, add these topics to your repository:"
echo "  - python"
echo "  - fastapi"
echo "  - numerical-methods"
echo "  - numerical-analysis"
echo "  - scientific-computing"
echo "  - web-application"
echo "  - calculator"
echo "  - education"
echo ""

echo "✅ Repository prepared for GitHub upload!"
echo "Follow the steps above to complete the upload."
