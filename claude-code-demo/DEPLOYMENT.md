# 🚀 Deployment Guide - PDF Merger

This guide will help you deploy your Flask PDF Merger application to the web so it can be accessed from anywhere!

## 🌟 **Option 1: Railway (Recommended - Free & Easy)**

Railway is perfect for Flask apps with a generous free tier.

### Steps:

1. **Create Railway Account**
   - Go to [railway.app](https://railway.app)
   - Sign up with GitHub

2. **Deploy Your App**
   ```bash
   # Install Railway CLI
   npm install -g @railway/cli
   
   # Login to Railway
   railway login
   
   # Initialize and deploy
   railway init
   railway up
   ```

3. **Your app will be live at**: `https://your-app-name.railway.app`

---

## 🌟 **Option 2: Render (Free Tier Available)**

Render offers a free tier for web services.

### Steps:

1. **Create Render Account**
   - Go to [render.com](https://render.com)
   - Sign up with GitHub

2. **Connect Your Repository**
   - Connect your GitHub repository
   - Choose "Web Service"
   - Set build command: `pip install -r requirements.txt`
   - Set start command: `python app.py`

3. **Your app will be live at**: `https://your-app-name.onrender.com`

---

## 🌟 **Option 3: Heroku (Paid)**

Heroku is a popular platform for web apps.

### Steps:

1. **Create Heroku Account**
   - Go to [heroku.com](https://heroku.com)
   - Sign up

2. **Deploy via CLI**
   ```bash
   # Install Heroku CLI
   # Download from: https://devcenter.heroku.com/articles/heroku-cli
   
   # Login
   heroku login
   
   # Create app
   heroku create your-pdf-merger-app
   
   # Deploy
   git add .
   git commit -m "Initial deployment"
   git push heroku main
   ```

3. **Your app will be live at**: `https://your-pdf-merger-app.herokuapp.com`

---

## 🌟 **Option 4: PythonAnywhere (Free Tier)**

Great for Python web apps.

### Steps:

1. **Create PythonAnywhere Account**
   - Go to [pythonanywhere.com](https://pythonanywhere.com)
   - Sign up for free account

2. **Upload Your Code**
   - Upload your files via the web interface
   - Or use Git to clone your repository

3. **Configure Web App**
   - Go to "Web" tab
   - Add new web app
   - Choose "Flask" and Python 3.9
   - Set source code directory
   - Set WSGI configuration file

4. **Your app will be live at**: `https://yourusername.pythonanywhere.com`

---

## 🌟 **Option 5: Vercel (Free Tier)**

Vercel is great for static sites and serverless functions.

### Steps:

1. **Create Vercel Account**
   - Go to [vercel.com](https://vercel.com)
   - Sign up with GitHub

2. **Deploy**
   - Import your GitHub repository
   - Vercel will auto-detect Flask
   - Deploy automatically

3. **Your app will be live at**: `https://your-app-name.vercel.app`

---

## 🔧 **Pre-Deployment Checklist**

Before deploying, make sure:

- ✅ All files are committed to Git
- ✅ `requirements.txt` is up to date
- ✅ `Procfile` exists (for Railway/Heroku)
- ✅ `runtime.txt` exists (for Railway/Heroku)
- ✅ App uses environment variables for port/host
- ✅ Debug mode is disabled in production

---

## 🌐 **Custom Domain (Optional)**

After deployment, you can add a custom domain:

1. **Buy a domain** (GoDaddy, Namecheap, etc.)
2. **Configure DNS** to point to your hosting provider
3. **Add domain** in your hosting platform settings

---

## 📱 **Testing Your Deployed App**

After deployment:

1. **Test file upload** - Upload a small PDF
2. **Test drag & drop** - Arrange files
3. **Test PDF merging** - Merge files and download
4. **Test on mobile** - Check responsive design
5. **Test different browsers** - Chrome, Firefox, Safari

---

## 🛠 **Troubleshooting**

### Common Issues:

1. **"Application Error"**
   - Check logs in your hosting platform
   - Ensure all dependencies are in `requirements.txt`

2. **"Port already in use"**
   - Use environment variables for port (already configured)

3. **"File upload not working"**
   - Check file size limits
   - Ensure upload folder has write permissions

4. **"PDF merge fails"**
   - Check if PyPDF2 is properly installed
   - Test with smaller files first

---

## 🎉 **Congratulations!**

Once deployed, your PDF Merger will be accessible to anyone with an internet connection!

**Share your app URL**: `https://your-app-name.railway.app`

---

## 📊 **Monitoring & Analytics**

Consider adding:
- Google Analytics for usage tracking
- Error monitoring (Sentry)
- Performance monitoring

---

**Happy Deploying! 🚀✨** 