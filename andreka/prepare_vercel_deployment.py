#!/usr/bin/env python
"""
Vercel Deployment Helper Script
Run this script to prepare your Django project for Vercel deployment
"""

import os
import sys
import subprocess
from pathlib import Path

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e.stderr}")
        return None

def check_requirements():
    """Check if required files exist"""
    required_files = [
        'vercel.json',
        'requirements.txt',
        'api/index.py',
        'andreka/settings_vercel.py'
    ]
    
    missing_files = []
    for file in required_files:
        if not Path(file).exists():
            missing_files.append(file)
    
    if missing_files:
        print(f"❌ Missing required files: {', '.join(missing_files)}")
        return False
    
    print("✅ All required files present")
    return True

def collect_static_files():
    """Collect static files for production"""
    return run_command(
        "python manage.py collectstatic --noinput",
        "Collecting static files"
    )

def run_migrations():
    """Run database migrations"""
    return run_command(
        "python manage.py migrate",
        "Running database migrations"
    )

def create_sample_data():
    """Create sample blog posts"""
    return run_command(
        "python manage.py create_sample_blog_posts",
        "Creating sample blog posts"
    )

def main():
    """Main deployment preparation function"""
    print("🚀 Andreka Vercel Deployment Preparation")
    print("=" * 50)
    
    # Check if we're in the right directory
    if not Path('manage.py').exists():
        print("❌ Please run this script from the andreka project root directory")
        sys.exit(1)
    
    # Check requirements
    if not check_requirements():
        print("❌ Please ensure all required files are present")
        sys.exit(1)
    
    # Set environment variables for production
    os.environ['DJANGO_SETTINGS_MODULE'] = 'andreka.settings_vercel'
    
    # Run deployment steps
    steps = [
        ("Collecting static files", collect_static_files),
        ("Running migrations", run_migrations),
        ("Creating sample data", create_sample_data),
    ]
    
    for step_name, step_func in steps:
        print(f"\n📋 {step_name}")
        result = step_func()
        if result is None:
            print(f"❌ {step_name} failed. Please check the error above.")
            sys.exit(1)
    
    print("\n🎉 Deployment preparation completed successfully!")
    print("\n📋 Next steps:")
    print("1. Push your code to GitHub")
    print("2. Connect your repository to Vercel")
    print("3. Configure environment variables in Vercel dashboard")
    print("4. Add PostgreSQL addon")
    print("5. Deploy!")
    print("\n📖 See VERCEL_DEPLOYMENT_GUIDE.md for detailed instructions")

if __name__ == "__main__":
    main()
