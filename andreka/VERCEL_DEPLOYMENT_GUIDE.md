# 🚀 Deploying Andreka to Vercel - Complete Guide

This guide will help you deploy your Andreka fashion e-commerce website to Vercel.

## 📋 Prerequisites

1. **Vercel Account**: Sign up at [vercel.com](https://vercel.com)
2. **GitHub Account**: Your code should be in a GitHub repository
3. **PostgreSQL Database**: Vercel provides PostgreSQL addon
4. **SSLCOMMERZ Production Credentials**: Get your live credentials

## 🔧 Step 1: Prepare Your Project

### 1.1 Update Settings for Production

The project includes a production-ready settings file (`settings_vercel.py`) with:
- PostgreSQL database configuration
- Static files handling with WhiteNoise
- Security settings
- Environment variable support

### 1.2 Required Files Created

✅ `vercel.json` - Vercel configuration
✅ `requirements.txt` - Python dependencies
✅ `api/index.py` - WSGI entry point
✅ `settings_vercel.py` - Production settings

## 🌐 Step 2: Deploy to Vercel

### 2.1 Connect GitHub Repository

1. Go to [vercel.com/dashboard](https://vercel.com/dashboard)
2. Click "New Project"
3. Import your GitHub repository
4. Select the `andreka` folder as the root directory

### 2.2 Configure Environment Variables

In Vercel dashboard, go to Settings → Environment Variables and add:

```env
# Django Settings
SECRET_KEY=your-super-secret-key-here
DEBUG=False
DJANGO_SETTINGS_MODULE=andreka.settings_vercel

# Database (Vercel PostgreSQL)
DATABASE_NAME=your-db-name
DATABASE_USER=your-db-user
DATABASE_PASSWORD=your-db-password
DATABASE_HOST=your-db-host
DATABASE_PORT=5432

# SSLCOMMERZ Production
SSLCOMMERZ_STORE_ID=your-production-store-id
SSLCOMMERZ_STORE_PASSWORD=your-production-password
SSLCOMMERZ_SANDBOX_MODE=False

# Email (Optional)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password

# Domain (Optional)
DOMAIN=your-domain.com
```

### 2.3 Build Configuration

Vercel will automatically detect the Python project and use the `vercel.json` configuration.

## 🗄️ Step 3: Set Up Database

### 3.1 Add PostgreSQL Addon

1. In Vercel dashboard, go to your project
2. Click "Storage" tab
3. Add "PostgreSQL" addon
4. Note the connection details

### 3.2 Run Migrations

After deployment, you'll need to run migrations. You can do this by:

1. **Using Vercel CLI** (Recommended):
   ```bash
   npm i -g vercel
   vercel login
   vercel env pull .env.local
   vercel --prod
   ```

2. **Using Django Management Commands**:
   Create a simple script to run migrations via Vercel Functions.

## 📁 Step 4: Handle Static Files

### 4.1 Collect Static Files

The project is configured to use WhiteNoise for static file serving. Static files will be automatically collected during build.

### 4.2 Media Files

For media files (user uploads), consider using:
- **Vercel Blob Storage** (Recommended)
- **AWS S3**
- **Cloudinary**

## 🔐 Step 5: Security Configuration

### 5.1 Update Secret Key

Generate a new secret key:
```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

### 5.2 SSLCOMMERZ Production Setup

1. Get production credentials from SSLCOMMERZ
2. Update environment variables
3. Test payment flow in production

## 🚀 Step 6: Deploy

### 6.1 Automatic Deployment

Once configured, Vercel will automatically deploy on every push to your main branch.

### 6.2 Manual Deployment

```bash
# Install Vercel CLI
npm i -g vercel

# Login to Vercel
vercel login

# Deploy
vercel --prod
```

## 🔧 Step 7: Post-Deployment Setup

### 7.1 Create Superuser

You'll need to create a superuser for admin access. You can do this by:

1. **Using Vercel CLI**:
   ```bash
   vercel env pull .env.local
   python manage.py createsuperuser
   ```

2. **Using Django Shell**:
   Create a management command to create superuser programmatically.

### 7.2 Create Sample Data

```bash
python manage.py create_sample_blog_posts
```

## 📊 Step 8: Monitoring & Analytics

### 8.1 Vercel Analytics

Enable Vercel Analytics in your dashboard for:
- Performance monitoring
- User analytics
- Error tracking

### 8.2 Database Monitoring

Monitor your PostgreSQL database through Vercel dashboard.

## 🛠️ Troubleshooting

### Common Issues:

1. **Static Files Not Loading**:
   - Ensure WhiteNoise is properly configured
   - Check STATIC_ROOT and STATICFILES_DIRS

2. **Database Connection Issues**:
   - Verify environment variables
   - Check PostgreSQL addon status

3. **Media Files Not Working**:
   - Configure external storage (Vercel Blob, S3, etc.)
   - Update MEDIA_URL and MEDIA_ROOT

4. **SSLCOMMERZ Issues**:
   - Verify production credentials
   - Check SSLCOMMERZ_SANDBOX_MODE setting

### Debug Mode:

For debugging, temporarily set:
```env
DEBUG=True
```

## 📱 Step 9: Custom Domain (Optional)

### 9.1 Add Custom Domain

1. Go to Vercel dashboard → Settings → Domains
2. Add your domain
3. Update DNS records as instructed

### 9.2 SSL Certificate

Vercel automatically provides SSL certificates for custom domains.

## 🔄 Step 10: Continuous Deployment

### 10.1 GitHub Integration

- Every push to main branch triggers deployment
- Preview deployments for pull requests
- Automatic rollback on deployment failures

### 10.2 Environment Management

- Production: `main` branch
- Staging: `develop` branch (optional)
- Preview: Pull requests

## 📈 Performance Optimization

### 10.1 Caching

- Vercel Edge Network
- Static file caching
- Database query optimization

### 10.2 CDN

- Global CDN for static files
- Image optimization
- Automatic compression

## 🆘 Support & Resources

### Documentation:
- [Vercel Django Guide](https://vercel.com/docs/frameworks/django)
- [Django Deployment Checklist](https://docs.djangoproject.com/en/stable/howto/deployment/checklist/)

### Community:
- Vercel Discord
- Django Forum
- Stack Overflow

## 🎉 Success Checklist

- [ ] Repository connected to Vercel
- [ ] Environment variables configured
- [ ] PostgreSQL database set up
- [ ] Migrations run successfully
- [ ] Static files serving correctly
- [ ] SSLCOMMERZ production credentials configured
- [ ] Custom domain added (optional)
- [ ] SSL certificate active
- [ ] Admin user created
- [ ] Sample data loaded
- [ ] Payment flow tested
- [ ] Analytics enabled

---

**Your Andreka fashion e-commerce website is now live on Vercel!** 🎉

For any issues, check the Vercel deployment logs and Django error logs.
