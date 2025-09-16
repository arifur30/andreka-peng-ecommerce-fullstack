# Andreka - Fashion E-Commerce Platform

A modern, full-featured fashion e-commerce website built with Django, featuring SSLCOMMERZ payment integration, a Vogue-inspired blog, and comprehensive user management.

## 🌟 Features

### 🛍️ E-Commerce Core
- **Product Catalog**: Browse fashion items with detailed product pages
- **Shopping Cart**: Add/remove items with real-time updates
- **User Authentication**: Registration, login, and profile management
- **Order Management**: Complete order tracking and history
- **Payment Integration**: SSLCOMMERZ payment gateway with success/failure handling

### 💳 Payment System
- **SSLCOMMERZ Integration**: Secure payment processing
- **Multiple Payment Methods**: Credit cards, mobile banking
- **Order Confirmation**: Automatic email notifications
- **Cart Management**: Automatic cart clearing after successful orders
- **Order History**: Complete order tracking in user profiles

### 📝 Fashion Blog
- **Vogue-Inspired Design**: Magazine-style layout
- **Content Management**: Admin panel for blog posts
- **Categories**: Fashion, Trends, Lifestyle, Beauty, Events, Designer Spotlight, Sustainability
- **Featured Posts**: Highlighted content sections
- **Image Galleries**: Multiple images per blog post
- **Social Sharing**: Built-in sharing buttons
- **Responsive Design**: Mobile-optimized reading experience

### 🏢 Services Page
- **Professional Showcase**: Company services and capabilities
- **Quality Assurance**: Product quality demonstration
- **Customer Reviews**: Testimonials and feedback
- **Community Impact**: Social responsibility highlights
- **Technology Features**: AI recommendations, mobile app, security

### 👤 User Management
- **Profile System**: Complete user profiles with avatars
- **Address Management**: Multiple shipping addresses
- **Order History**: Detailed order tracking
- **Dashboard**: User-specific dashboard with statistics

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Django 3.1+
- SQLite (default) or PostgreSQL/MySQL

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd andreka
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   Create a `.env` file with your SSLCOMMERZ credentials:
   ```env
   SSLCOMMERZ_STORE_ID=your_store_id
   SSLCOMMERZ_STORE_PASSWORD=your_store_password
   SSLCOMMERZ_SANDBOX_MODE=True
   ```

4. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **Create sample blog posts**
   ```bash
   python manage.py create_sample_blog_posts
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   - Website: http://127.0.0.1:8000/
   - Admin Panel: http://127.0.0.1:8000/admin/

## 📁 Project Structure

```
andreka/
├── andreka/                 # Django project settings
│   ├── settings.py          # Main settings file
│   ├── urls.py             # URL configuration
│   └── wsgi.py             # WSGI configuration
├── andrekaApp/              # Main Django app
│   ├── models.py           # Database models
│   ├── views.py            # View functions
│   ├── urls.py             # App URL patterns
│   ├── admin.py            # Admin panel configuration
│   ├── sslcommerz_service.py # Payment gateway service
│   └── management/         # Custom management commands
├── templates/              # HTML templates
│   ├── base.html           # Base template
│   ├── blog/               # Blog templates
│   ├── profile/            # User profile templates
│   └── registration/       # Auth templates
├── static/                 # Static files
│   ├── css/                # Stylesheets
│   ├── js/                 # JavaScript files
│   ├── images/             # Images and icons
│   └── blog/               # Blog-specific assets
└── media/                  # User-uploaded files
    ├── products/           # Product images
    └── profile_pictures/   # User avatars
```

## 🔧 Configuration

### SSLCOMMERZ Setup
1. Get your credentials from SSLCOMMERZ
2. Update `settings.py` with your credentials:
   ```python
   SSLCOMMERZ_STORE_ID = 'your_store_id'
   SSLCOMMERZ_STORE_PASSWORD = 'your_store_password'
   SSLCOMMERZ_SANDBOX_MODE = True  # Set to False for production
   ```

### Database Configuration
The project uses SQLite by default. For production, configure PostgreSQL or MySQL in `settings.py`.

### Static Files
For production, run:
```bash
python manage.py collectstatic
```

## 📱 Pages & Features

### Main Pages
- **Home**: Product showcase and featured items
- **Collection**: Product catalog with filtering
- **Blog**: Fashion blog with categories
- **Services**: Company services and capabilities
- **About**: Company information
- **Contact**: Contact form and information

### User Features
- **Registration/Login**: User authentication
- **Profile**: User dashboard and settings
- **Cart**: Shopping cart management
- **Checkout**: Secure payment process
- **Order History**: Complete order tracking

### Admin Features
- **Product Management**: Add/edit products
- **Order Management**: View and manage orders
- **Blog Management**: Create and edit blog posts
- **User Management**: User administration
- **Payment Tracking**: Payment status monitoring

## 🎨 Design Features

### Responsive Design
- Mobile-first approach
- Tablet and desktop optimized
- Touch-friendly interface

### Modern UI/UX
- Clean, minimalist design
- Fashion-forward aesthetics
- Intuitive navigation
- Fast loading times

### Blog Design
- Vogue-inspired layout
- Magazine-style typography
- Image galleries
- Social sharing integration

## 🔒 Security Features

- **CSRF Protection**: Cross-site request forgery protection
- **Secure Payments**: SSLCOMMERZ secure payment processing
- **User Authentication**: Django's built-in auth system
- **Input Validation**: Form validation and sanitization
- **File Upload Security**: Secure file handling

## 📊 Management Commands

### Available Commands
- `create_sample_blog_posts`: Creates sample blog content
- `create_sample_post`: Creates a single blog post

### Usage
```bash
python manage.py create_sample_blog_posts
python manage.py create_sample_post
```

## 🚀 Deployment

### Production Checklist
1. Set `DEBUG = False` in settings
2. Configure production database
3. Set up static file serving
4. Configure SSLCOMMERZ production credentials
5. Set up email backend for notifications
6. Configure domain and SSL certificates

### Environment Variables
```env
DEBUG=False
SECRET_KEY=your_secret_key
SSLCOMMERZ_STORE_ID=your_production_store_id
SSLCOMMERZ_STORE_PASSWORD=your_production_password
SSLCOMMERZ_SANDBOX_MODE=False
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

For support and questions:
- Create an issue in the repository
- Contact the development team
- Check the documentation

## 🔄 Version History

- **v1.0.0**: Initial release with basic e-commerce features
- **v1.1.0**: Added SSLCOMMERZ payment integration
- **v1.2.0**: Implemented fashion blog system
- **v1.3.0**: Added services page and enhanced UI

## 📞 Contact

**Andreka Fashion**
- Email: info@andreka.com
- Website: https://andreka.com
- Phone: +8801878125712

---

Built with ❤️ using Django and modern web technologies.
