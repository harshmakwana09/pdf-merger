# 📚 GitHub Setup Guide for Beginners

**Step-by-step guide to upload your PDF Merger to GitHub**

## 🚀 **Step 1: Create GitHub Account**

1. Go to [github.com](https://github.com)
2. Click "Sign up"
3. Create your account

## 🚀 **Step 2: Create New Repository**

1. **Click the "+" icon** in the top right
2. **Select "New repository"**
3. **Repository name**: `pdf-merger` (or any name you like)
4. **Description**: `A beautiful Flask web app for merging PDF files`
5. **Make it Public** (so others can see it)
6. **Don't initialize** with README (we already have one)
7. **Click "Create repository"**

## 🚀 **Step 3: Upload Your Code**

### **Option A: Using GitHub Desktop (Easiest for Beginners)**

1. **Download GitHub Desktop** from [desktop.github.com](https://desktop.github.com)
2. **Install and sign in** with your GitHub account
3. **Clone your repository**:
   - Click "Clone a repository from the Internet"
   - Select your `pdf-merger` repository
   - Choose a local path (like `C:\Users\HARSH\pdf-merger`)
   - Click "Clone"

4. **Copy your files**:
   - Copy ALL files from `C:\Users\HARSH\claude-code-demo\` to your new folder
   - **EXCEPT** the `uploads/` folder (don't copy that)

5. **Commit and push**:
   - Open GitHub Desktop
   - You'll see all your files listed
   - Write a commit message: `"Initial commit - PDF Merger Flask app"`
   - Click "Commit to main"
   - Click "Push origin"

### **Option B: Using Command Line**

1. **Open Command Prompt** in your project folder:
   ```bash
   cd C:\Users\HARSH\claude-code-demo
   ```

2. **Initialize Git**:
   ```bash
   git init
   git add .
   git commit -m "Initial commit - PDF Merger Flask app"
   ```

3. **Connect to GitHub**:
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/pdf-merger.git
   git branch -M main
   git push -u origin main
   ```

## 📁 **Files to Upload (Important!)**

**✅ Upload these files:**
- `app.py`
- `requirements.txt`
- `Procfile`
- `runtime.txt`
- `README.md`
- `DEPLOYMENT.md`
- `QUICK_DEPLOY.md`
- `GITHUB_SETUP.md`
- `.gitignore`
- `templates/` folder (with all HTML files)

**❌ DON'T upload:**
- `uploads/` folder (temporary files)
- Any `.pdf` files
- `__pycache__/` folders

## 🎯 **Step 4: Verify Your Repository**

1. **Go to your GitHub repository**
2. **You should see all your files** listed
3. **Click on files** to view them
4. **Your repository is ready!** 🎉

## 🔗 **Your Repository URL**

Your repository will be at:
`https://github.com/YOUR_USERNAME/pdf-merger`

## 📋 **What Each File Does**

- **`app.py`** - Main Flask application
- **`requirements.txt`** - Python packages needed
- **`Procfile`** - Tells deployment platforms how to run your app
- **`runtime.txt`** - Specifies Python version
- **`README.md`** - Project description and instructions
- **`templates/`** - HTML files for the website
- **`.gitignore`** - Tells Git which files to ignore

## 🌟 **Next Steps**

After uploading to GitHub:

1. **Deploy to Railway** (see `QUICK_DEPLOY.md`)
2. **Share your repository** with others
3. **Add collaborators** if you want help
4. **Create issues** for bugs or features

## 🆘 **Need Help?**

- **GitHub Help**: [help.github.com](https://help.github.com)
- **GitHub Desktop**: [desktop.github.com](https://desktop.github.com)
- **Git Cheat Sheet**: [education.github.com/git-cheat-sheet-education.pdf](https://education.github.com/git-cheat-sheet-education.pdf)

---

**🎉 Congratulations! Your PDF Merger is now on GitHub!** 