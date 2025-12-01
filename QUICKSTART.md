# ⚡ Quick Start - Deploy in 10 Minutes

This is the **fastest way** to get your Numerical Methods Hybrid System live on the internet.

## 🎯 What You'll Get

- ✅ GitHub repository: `numerical-methods-hybrid-system`
- ✅ Python backend live on Render
- ✅ Java backend live on Render
- ✅ Documentation site on GitHub Pages
- ✅ Automated CI/CD pipeline
- ✅ All for **$0/month** (free tier)

---

## 📝 Prerequisites (2 minutes)

1. **GitHub account** → [Sign up](https://github.com/signup) (free)
2. **Render account** → [Sign up](https://render.com) (free, use GitHub login)

That's it! No credit card needed.

---

## 🚀 Step-by-Step Deployment

### Step 1: Push to GitHub (3 minutes)

Open PowerShell in your project folder:

```powershell
# Run the setup script
.\setup_github_manual.ps1
```

**What it does:**
- Commits all your code
- Guides you to create the repository
- Pushes everything to GitHub

**Follow the prompts:**
1. When asked, go to https://github.com/new
2. Name: `numerical-methods-hybrid-system`
3. **Keep it Public**
4. **Don't** add README/license (we have them)
5. Click "Create repository"
6. Return to PowerShell and press Enter
7. Enter your GitHub username
8. Done! ✅

---

### Step 2: Deploy to Render (4 minutes)

1. **Go to:** https://render.com
2. **Sign in** with GitHub
3. **Click:** "New +" → "Web Service"
4. **Find:** `numerical-methods-hybrid-system`
5. **Click:** "Connect"

🎉 **That's it!** Render detects `render.yaml` and deploys both backends automatically.

**Wait 3-4 minutes** for:
- Python backend to build and deploy
- Java backend to build and deploy

---

### Step 3: Enable GitHub Pages (1 minute)

1. **Go to:** `https://github.com/YOUR_USERNAME/numerical-methods-hybrid-system/settings/pages`
2. **Source:** Select "GitHub Actions"
3. **Wait** 2 minutes for deployment

---

### Step 4: Get Your URLs (1 minute)

#### Python Backend:
```
https://numerical-methods-python.onrender.com
```

#### Java Backend:
```
https://numerical-methods-java.onrender.com
```

#### Documentation:
```
https://YOUR_USERNAME.github.io/numerical-methods-hybrid-system
```

---

## ✅ Verify It Works

### Test Python Backend:

```bash
curl https://numerical-methods-python.onrender.com/
```

Expected response:
```json
{
  "message": "Numerical Methods Calculator API",
  "status": "running",
  "version": "1.0.0"
}
```

### Test Java Backend:

```bash
curl https://numerical-methods-java.onrender.com/api/jacobi/health
```

Expected response:
```json
{
  "status": "UP"
}
```

---

## 🎉 You're Live!

Your application is now deployed with:

✅ **Python FastAPI** backend  
✅ **Java Spring Boot** backend  
✅ **Automated CI/CD** (tests run on every push)  
✅ **Free hosting** (Render + GitHub Pages)  
✅ **HTTPS** enabled  
✅ **Auto-deploy** on git push  

---

## 📱 Next Steps

### Update README with Live URLs

Edit `README.md` and add your actual URLs:

```markdown
## 🌐 Live Demo

- **Python Backend:** https://numerical-methods-python.onrender.com
- **Java Backend:** https://numerical-methods-java.onrender.com
- **Documentation:** https://YOUR_USERNAME.github.io/numerical-methods-hybrid-system
```

Then:
```powershell
git add README.md
git commit -m "Add live deployment URLs"
git push
```

### Add Repository Topics

On GitHub, add these topics to your repository:
- `python`
- `java`
- `fastapi`
- `spring-boot`
- `docker`
- `numerical-methods`
- `calculator`
- `dual-backend`

---

## ⚠️ Important Notes

### Free Tier Limitations

**Render Free Tier:**
- Apps sleep after 15 minutes of inactivity
- First request may take 30-60 seconds to "wake up"
- This is **normal behavior** for free tier

**To keep apps awake (optional):**
1. Upgrade to Render Starter ($7/month per service)
2. Or use UptimeRobot to ping every 10 minutes

### CI/CD

Every time you push code:
1. GitHub Actions runs tests
2. If tests pass, Render auto-deploys
3. Your changes go live automatically

---

## 🆘 Troubleshooting

### "Command 'gh' not found"
✅ **No problem!** The `setup_github_manual.ps1` script doesn't need gh CLI.

### "Git push failed"
```powershell
# Configure Git
git config --global user.name "Your Name"
git config --global user.email "your@email.com"

# Try again
git push -u origin main
```

### "Render build failed"
1. Check logs in Render dashboard
2. Most common: wrong file paths
3. Solution: Check `render.yaml` paths match your structure

### "GitHub Pages not showing"
1. Wait 3-5 minutes after enabling
2. Check Actions tab for deployment status
3. Hard refresh browser (Ctrl+Shift+R)

---

## 📞 Need Help?

- 📖 **Full Guide:** See `DEPLOYMENT_COMPLETE_GUIDE.md`
- 🐛 **Issues:** Open issue on GitHub
- 💬 **Questions:** GitHub Discussions

---

## 🏁 Summary

| Step | Time | Status |
|------|------|--------|
| 1. Push to GitHub | 3 min | ⏳ |
| 2. Deploy to Render | 4 min | ⏳ |
| 3. Enable GitHub Pages | 1 min | ⏳ |
| 4. Verify & Test | 2 min | ⏳ |
| **Total** | **10 min** | 🚀 |

---

**Ready? Let's go!** Run this command:

```powershell
.\setup_github_manual.ps1
```

🎯 **Your numerical methods calculator will be live in 10 minutes!**
