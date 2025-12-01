# 🚀 Complete Deployment Guide

This guide will walk you through deploying the Numerical Methods Hybrid System to production.

## 📋 Table of Contents

1. [Prerequisites](#prerequisites)
2. [GitHub Repository Setup](#github-repository-setup)
3. [Deploy to Render](#deploy-to-render)
4. [Enable GitHub Pages](#enable-github-pages)
5. [Verify Deployments](#verify-deployments)
6. [Troubleshooting](#troubleshooting)

---

## Prerequisites

✅ **Required:**
- Git installed
- GitHub account
- Render account (free tier available at https://render.com)

✅ **Verified:**
- ✓ Python backend tested locally
- ✓ Java backend tested locally
- ✓ Docker configurations ready
- ✓ CI/CD workflows configured
- ✓ All tests passing

---

## GitHub Repository Setup

### Step 1: Run the Setup Script

Open PowerShell in the project directory and run:

```powershell
.\setup_github_manual.ps1
```

This script will:
- ✓ Stage all files
- ✓ Commit changes with detailed message
- ✓ Create main branch
- ✓ Guide you through creating the repository
- ✓ Push code to GitHub

### Step 2: Create Repository on GitHub

When prompted by the script:

1. Go to: **https://github.com/new**
2. **Repository name:** `numerical-methods-hybrid-system`
3. **Description:** `Numerical Methods Calculator with Dual Backend (Python FastAPI + Java Spring Boot)`
4. **Visibility:** Public ✓
5. **DO NOT** check:
   - ❌ Add a README file
   - ❌ Add .gitignore
   - ❌ Choose a license
   
   (We already have these files!)

6. Click **"Create repository"**

### Step 3: Complete the Push

After creating the repository:
- Return to PowerShell
- Press Enter when prompted
- Enter your GitHub username
- The script will push all code to GitHub

---

## Deploy to Render

### Option 1: Using render.yaml (Recommended)

1. **Go to Render:** https://render.com
2. **Sign In:** Use GitHub authentication
3. **Create New Web Service:**
   - Click **"New +"** → **"Web Service"**
4. **Connect Repository:**
   - Search for `numerical-methods-hybrid-system`
   - Click **"Connect"**
5. **Render will auto-detect render.yaml** and deploy both backends!

### Option 2: Manual Deployment

#### Python Backend:

1. **New Web Service**
2. **Configuration:**
   ```
   Name: numerical-methods-python
   Environment: Docker
   Region: Choose closest to you
   Branch: main
   Root Directory: .
   ```
3. **Click "Create Web Service"**

#### Java Backend:

1. **New Web Service**
2. **Configuration:**
   ```
   Name: numerical-methods-java
   Environment: Docker
   Region: Choose closest to you
   Branch: main
   Root Directory: java-backend
   ```
3. **Click "Create Web Service"**

### What Happens Next:

- 🐳 Render builds Docker images
- 📦 Installs dependencies
- 🚀 Starts services
- 🔗 Provides public URLs
- ⏱️ Takes 3-5 minutes for first deployment

---

## Enable GitHub Pages

### Step 1: Go to Repository Settings

Navigate to:
```
https://github.com/YOUR_USERNAME/numerical-methods-hybrid-system/settings/pages
```

### Step 2: Configure GitHub Pages

1. **Source:** Select **"GitHub Actions"**
2. **Wait** for the deployment workflow to complete
3. **Check** the Actions tab for progress

### Step 3: Access Documentation Site

Your documentation will be available at:
```
https://YOUR_USERNAME.github.io/numerical-methods-hybrid-system/
```

---

## Verify Deployments

### 1. Check GitHub Actions

Go to: `https://github.com/YOUR_USERNAME/numerical-methods-hybrid-system/actions`

✅ Verify these workflows are passing:
- Python CI
- Java CI
- Deploy to Production

### 2. Check Render Dashboard

Go to: `https://dashboard.render.com`

✅ Verify both services are running:
- numerical-methods-python
- numerical-methods-java

### 3. Test Endpoints

Once deployed, test these endpoints:

#### Python Backend:
```bash
# Health check
curl https://YOUR-PYTHON-APP.onrender.com/

# Jacobi method
curl -X POST https://YOUR-PYTHON-APP.onrender.com/api/jacobi \
  -H "Content-Type: application/json" \
  -d '{"matrix": [[4,1],[1,3]], "b": [1,2], "tolerance": 0.001}'
```

#### Java Backend:
```bash
# Health check
curl https://YOUR-JAVA-APP.onrender.com/api/jacobi/health

# Jacobi method
curl -X POST https://YOUR-JAVA-APP.onrender.com/api/jacobi/solve \
  -H "Content-Type: application/json" \
  -d '{"matrix": [[4,1],[1,3]], "constants": [1,2], "tolerance": 0.001}'
```

---

## Troubleshooting

### Issue: Git push fails with authentication error

**Solution:**
```powershell
# Configure Git credentials
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Try push again
git push -u origin main
```

If still failing, use GitHub Desktop or authenticate via browser.

### Issue: Render build fails

**Check:**
1. Build logs in Render dashboard
2. Dockerfile syntax
3. Dependencies in requirements.txt or pom.xml

**Common Fixes:**
- Ensure Python version matches (3.13)
- Ensure Java version matches (21)
- Check memory limits (default: 512MB free tier)

### Issue: GitHub Actions workflow fails

**Check:**
1. Actions tab for error messages
2. YAML syntax in workflow files
3. Permissions in repository settings

**Fix:**
```powershell
# Validate YAML locally
cat .github/workflows/python-ci.yml

# Re-commit if needed
git add .github/workflows/
git commit -m "Fix workflow syntax"
git push
```

### Issue: GitHub Pages not enabled

**Solution:**
1. Go to Settings → Pages
2. Select source: "GitHub Actions"
3. Wait for workflow to complete
4. Refresh after 2-3 minutes

### Issue: Render free tier spins down

**Expected Behavior:**
- Free tier apps sleep after 15 minutes of inactivity
- First request may take 30-60 seconds to wake up
- This is normal for free tier

**Solution (if needed):**
- Upgrade to paid plan ($7/month per service)
- Or use UptimeRobot to ping every 10 minutes

---

## Post-Deployment

### Update README with Live URLs

Once deployed, update `README.md` with actual URLs:

```markdown
## 🌐 Live Demo

- **Python Backend:** https://numerical-methods-python.onrender.com
- **Java Backend:** https://numerical-methods-java.onrender.com
- **Documentation:** https://YOUR_USERNAME.github.io/numerical-methods-hybrid-system
```

Commit and push:
```powershell
git add README.md
git commit -m "Update README with live deployment URLs"
git push
```

---

## Monitoring

### GitHub Actions
- View workflow runs: `Actions` tab
- Check test results
- Monitor deployment status

### Render Dashboard
- View logs: Click service → Logs tab
- Monitor performance
- Check resource usage

### Health Checks
Set up monitoring (optional):
- UptimeRobot: https://uptimerobot.com
- Better Uptime: https://betteruptime.com
- Pingdom: https://www.pingdom.com

---

## CI/CD Pipeline

### Automatic Deployments

Every push to `main` branch triggers:

1. **Python CI:**
   - Linting (flake8, black, isort)
   - Testing (pytest)
   - Security checks (bandit, safety)

2. **Java CI:**
   - Building (Maven)
   - Testing (JUnit)
   - Code quality (Checkstyle, SpotBugs)

3. **Deployment:**
   - Render auto-deploys both backends
   - GitHub Pages updates documentation

### Manual Deployment

Trigger manually from GitHub:
1. Go to Actions tab
2. Select "Deploy to Production"
3. Click "Run workflow"
4. Select branch: main
5. Click "Run workflow"

---

## Cost Breakdown

### Free Tier Limits

**Render (FREE):**
- 750 hours/month per service
- 512 MB RAM
- Shared CPU
- Services sleep after 15 min inactivity
- **Cost: $0/month**

**GitHub (FREE):**
- Unlimited public repositories
- 2000 CI/CD minutes/month
- GitHub Pages hosting
- **Cost: $0/month**

### Paid Options (Optional)

**Render Starter ($7/month per service):**
- 24/7 uptime (no sleeping)
- 512 MB RAM
- Shared CPU
- **Total: $14/month for both backends**

---

## Support

### Resources
- 📖 **Full Documentation:** README.md
- 🐛 **Report Issues:** GitHub Issues
- 💬 **Discussions:** GitHub Discussions
- 📧 **Contact:** Open an issue on GitHub

### Useful Links
- Render Docs: https://render.com/docs
- FastAPI Docs: https://fastapi.tiangolo.com
- Spring Boot Docs: https://spring.io/projects/spring-boot
- GitHub Actions Docs: https://docs.github.com/actions

---

## Success Checklist

Before considering deployment complete, verify:

- [ ] Code pushed to GitHub
- [ ] GitHub Actions workflows passing (Python CI, Java CI, Deploy)
- [ ] Python backend deployed and responding on Render
- [ ] Java backend deployed and responding on Render
- [ ] GitHub Pages documentation site live
- [ ] All API endpoints tested and working
- [ ] Health checks passing
- [ ] README updated with live URLs
- [ ] Repository topics added (python, java, fastapi, spring-boot, docker, numerical-methods)

---

## 🎉 Congratulations!

Your Numerical Methods Hybrid System is now live!

**Share your deployment:**
```
Repository: https://github.com/YOUR_USERNAME/numerical-methods-hybrid-system
Python API: https://numerical-methods-python.onrender.com
Java API: https://numerical-methods-java.onrender.com
Documentation: https://YOUR_USERNAME.github.io/numerical-methods-hybrid-system
```

Happy coding! 🚀
