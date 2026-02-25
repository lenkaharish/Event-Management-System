# Django Event Management System - Deployment Guide

## ⚠️ Important: Netlify Static Hosting Limitations

**Netlify's static hosting does NOT support Django by default.** This is a server-side Python framework that requires a runtime environment.

### Why "Page Not Found" on Netlify?

1. **Netlify serves static files only** - It doesn't run Python code
2. **No Django app execution** - Routes aren't processed by Django
3. **Default 404 page** - Netlify returns its own 404 for any missing files
4. **Missing Python runtime** - Netlify Functions require additional setup

---

## ✅ Recommended Deployment Solutions

### **Option 1: Railway (Recommended for Django) ⭐**

**Best for:** Full Django support with minimal configuration

#### Steps:
1. **Create Railway account:** https://railway.app
2. **Connect GitHub repository**
3. **Railway auto-detects Django with requirements.txt**
4. **Set environment variables:**
   - `SECRET_KEY`: Your secure key
   - `DEBUG`: `False`
   - `ALLOWED_HOSTS`: Your Railway domain

#### Command to deploy:
```bash
# Just push to GitHub, Railway deploys automatically
git push origin main
```

**Pros:**
- ✅ Free tier available ($5/month credit)
- ✅ Auto-detects Django
- ✅ PostgreSQL support
- ✅ Environment variables management
- ✅ Automatic HTTPS
- ✅ GitHub integration

---

### **Option 2: Render (Good Django Alternative)**

**Best for:** Reliable Django hosting with good free tier

#### Steps:
1. **Go to:** https://render.com
2. **Create new Web Service**
3. **Connect GitHub repo**
4. **Select Python 3.11**
5. **Build command:** `pip install -r requirements.txt && python manage.py migrate`
6. **Start command:** `gunicorn event_project.wsgi:application`

#### Environment variables:
```
SECRET_KEY=your-secret-key
DEBUG=False
ALLOWED_HOSTS=*.render.com,yourdomain.com
DATABASE_URL=postgresql://...
```

**Pros:**
- ✅ Generous free tier
- ✅ PostgreSQL database included
- ✅ Environment management
- ✅ Easy GitHub sync

---

### **Option 3: Heroku (Classic, Still Good)**

**Best for:** Quick deployment with minimal setup

```bash
# Install Heroku CLI
# heroku login
# heroku create your-app-name
# heroku addons:create heroku-postgresql:hobby-dev
# git push heroku main
```

**Note:** Heroku's free tier is limited; it's now a paid service.

---

### **Option 4: PythonAnywhere**

**Best for:** Simple hosting without infrastructure knowledge

1. **Sign up:** https://www.pythonanywhere.com
2. **Upload your code**
3. **Configure WSGI application**
4. **Set environment variables**

**Pros:**
- ✅ Django-specific hosting
- ✅ Beginner-friendly
- ✅ Free tier available
- ✅ Interactive console

---

### **Option 5: AWS/DigitalOcean/Linode (Self-Managed)**

**Best for:** Large-scale production with full control

Requires:
- Server setup (EC2, Droplet, etc.)
- Nginx/Apache configuration
- Gunicorn/uWSGI setup
- SSL certificate
- Database management

---

## 🚀 Step-by-Step: Deploy to Railway (Fastest)

### 1. **Update settings.py for production:**

Already done! Your settings now use environment variables.

### 2. **Ensure requirements.txt is complete:**

```bash
pip freeze > requirements.txt
```

### 3. **Create .env file (for local testing):**

```
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=*.railway.app,localhost
DATABASE_URL=sqlite:///db.sqlite3
```

### 4. **Create Procfile (for Heroku/Render):**

```
web: gunicorn event_project.wsgi:application
release: python manage.py migrate
```

### 5. **Push to GitHub:**

```bash
git add .
git commit -m "Ready for production deployment"
git push origin main
```

### 6. **Connect to Railway:**
- Go to railway.app
- Click "New Project"
- Select "GitHub Repo"
- Choose your repository
- Railway auto-deploys!

### 7. **Set Environment Variables in Railway:**

```
SECRET_KEY=django-insecure-_ez%7#97mc+qm$vp=y*u=koj4q5pidv#31c1orxj5olp6e6w(6
DEBUG=False
ALLOWED_HOSTS=*.railway.app
```

---

## 📊 Comparison Table

| Service | Free Tier | Setup | Django Support | Database | Recommendation |
|---------|-----------|-------|-----------------|----------|-----------------|
| **Railway** | $5/month | Auto | ⭐⭐⭐ | Yes | **Best** |
| **Render** | Generous | Auto | ⭐⭐⭐ | Yes | Good |
| **Heroku** | Limited | Auto | ⭐⭐⭐ | Yes | Paid |
| **PythonAnywhere** | Yes | Manual | ⭐⭐ | Yes | Beginner |
| **AWS** | Limited | Hard | ⭐⭐⭐ | Yes | Enterprise |
| **Netlify** | Yes | N/A | ❌ | No | **DON'T USE** |

---

## ❌ Why NOT Netlify?

```
❌ No Python runtime (static hosting only)
❌ Netlify Functions too complex for full Django
❌ Database connectivity issues
❌ Session management problems
❌ Static files serving limitations
❌ Every route returns 404 without backend
```

---

## ✅ What You Have Now

Your Django project is **production-ready**:
- ✅ Environment variable support for `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS`
- ✅ CSRF trusted origins configured
- ✅ Security headers set up
- ✅ Static files collection ready
- ✅ Media files handling
- ✅ CSS selector issues fixed
- ✅ Database migrations ready

---

## 🔧 Common Issues After Deployment

### Static files not loading
```bash
python manage.py collectstatic --noinput
```

### 500 Error
Check logs:
```bash
# Railway
railway logs

# Render  
tail -f logs
```

### Database migration issues
```bash
python manage.py migrate --run-syncdb
```

### ALLOWED_HOSTS error
Update environment variable to include your deployment domain.

---

## 📞 Support Resources

- **Django Deployment:** https://docs.djangoproject.com/en/6.0/howto/deployment/
- **Railway Docs:** https://docs.railway.app
- **Render Docs:** https://render.com/docs
- **Heroku Docs:** https://devcenter.heroku.com

---

## 🎯 Next Steps

1. **Choose a hosting service** (Railway recommended)
2. **Create account** and connect GitHub
3. **Set environment variables**
4. **Deploy** with `git push`
5. **Test** your application
6. **Monitor** logs for errors

Your application will now work correctly with a proper Python runtime! 🚀
