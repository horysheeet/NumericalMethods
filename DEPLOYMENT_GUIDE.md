# 🌐 Deploy Your Numerical Methods Calculator Online

## ✅ What's Been Added

I've added deployment configuration for your project:

1. **Dockerfile** - For containerized deployment
2. **render.yaml** - One-click deployment to Render
3. **GitHub Pages workflow** - Info page on GitHub Pages

## 🚀 Deploy Options

### Option 1: Render (Recommended - FREE & Easy)

**Render** provides free hosting with auto-deployment from GitHub.

#### Steps:

1. **Go to Render**: https://render.com
2. **Sign up** with your GitHub account
3. **Click "New +"** → **"Web Service"**
4. **Connect repository**: Select `horysheeet/NumericalMethods`
5. **Configure**:
   - **Name**: `numerical-methods-calculator`
   - **Environment**: `Docker`
   - **Plan**: `Free`
6. **Click "Create Web Service"**
7. **Wait 2-3 minutes** for deployment

Your app will be live at: `https://numerical-methods-calculator.onrender.com`

**Note**: Free tier spins down after 15 min of inactivity (wakes up in ~30 sec on first request)

---

### Option 2: Railway (FREE Credit)

**Railway** offers $5 free credit/month.

#### Steps:

1. **Go to Railway**: https://railway.app
2. **Login** with GitHub
3. **New Project** → **Deploy from GitHub repo**
4. **Select**: `horysheeet/NumericalMethods`
5. **Add variables** (Railway auto-detects Python):
   - Railway will automatically build from Dockerfile
6. **Deploy**

Your app will be live at: `https://numerical-methods-calculator.up.railway.app`

---

### Option 3: Fly.io (FREE Tier)

**Fly.io** provides fast global deployment.

#### Steps:

1. **Install flyctl**: 
   ```bash
   # Windows (PowerShell)
   iwr https://fly.io/install.ps1 -useb | iex
   ```

2. **Login**:
   ```bash
   fly auth login
   ```

3. **Deploy**:
   ```bash
   cd "D:\Numerical Methods"
   fly launch
   # Follow prompts, select region, confirm Dockerfile
   ```

Your app will be live at: `https://numerical-methods-calculator.fly.dev`

---

### Option 4: Vercel (Serverless)

**Vercel** offers free tier with serverless Python.

#### Steps:

1. **Go to Vercel**: https://vercel.com
2. **Import** your GitHub repository
3. Vercel will auto-detect Python and deploy

---

## 📄 GitHub Pages (Info Page Only)

I've also set up a GitHub Pages deployment that shows:
- Project information
- Deployment options
- Quick start guide
- Links to all platforms

### Enable GitHub Pages:

1. Go to: https://github.com/horysheeet/NumericalMethods/settings/pages
2. Under **Source**, select: `GitHub Actions`
3. The workflow will run automatically

Your info page will be at: **https://horysheeet.github.io/NumericalMethods**

## ⚡ Quick Start (Recommended Path)

```bash
# 1. Go to Render.com
# 2. Sign in with GitHub
# 3. Click "New +" → "Web Service"
# 4. Select your repo: horysheeet/NumericalMethods
# 5. Choose Docker environment
# 6. Click Create (FREE plan)
# 7. Done! Your app will be live in 3 minutes
```

## 🔗 URLs After Deployment

Once deployed, your calculator will be accessible at:
- **Render**: `https://numerical-methods-calculator.onrender.com`
- **Railway**: `https://numerical-methods-calculator.up.railway.app`
- **Fly.io**: `https://numerical-methods-calculator.fly.dev`
- **GitHub Pages** (info only): `https://horysheeet.github.io/NumericalMethods`

## 📊 What Gets Deployed

Your deployed app will include:
- ✅ All 5 numerical methods
- ✅ Interactive web interface
- ✅ RESTful API endpoints
- ✅ API documentation at `/docs`
- ✅ Full functionality with iteration tracking

## 💡 Tips

- **Free tiers** may have cold starts (15-30 seconds on first request)
- **Render** is easiest - one-click deploy
- **Railway** has better uptime on free tier
- **Fly.io** has fastest global performance
- All options auto-redeploy when you push to GitHub

## 🎯 Next Steps

1. Choose a platform (I recommend **Render** for easiest setup)
2. Follow the steps above
3. Share your live URL!
4. Optional: Update README.md with your live demo link

---

**Your app is ready to go live!** 🚀
