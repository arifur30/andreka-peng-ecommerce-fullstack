# Andreka & Peng - E-commerce Django Project

A modern e-commerce website built with Django featuring user authentication, product catalog, shopping cart functionality, and a beautiful responsive design.

## 🚀 Features

- **User Authentication System**
  - User registration and login
  - Protected dashboard for logged-in users
  - Secure logout functionality
  - Password management

- **E-commerce Functionality**
  - Product catalog with sneakers showcase
  - Product detail pages
  - Shopping cart system
  - Order placement workflow
  - Contact form

- **Modern UI/UX**
  - Responsive design for all devices
  - Beautiful card-based layouts
  - Custom styling with CSS
  - Interactive elements with JavaScript
  - Professional color scheme

## 📁 Project Structure

```
andreka/
├── andreka/                 # Django project settings
│   ├── __init__.py
│   ├── settings.py         # Project configuration
│   ├── urls.py            # Main URL routing
│   ├── wsgi.py
│   └── asgi.py
├── andrekaApp/             # Main application
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py            # App URL patterns
│   └── views.py           # View functions
├── templates/              # HTML templates
│   ├── index.html         # Homepage
│   ├── contact.html       # Contact page
│   ├── sneakers.html      # Product catalog
│   ├── sproduct.html      # Product details
│   ├── cart.html          # Shopping cart
│   ├── orderplaced.html   # Order confirmation
│   ├── button.html        # Button demo
│   ├── dashboard.html     # User dashboard
│   └── registration/      # Auth templates
│       ├── login.html
│       └── signup.html
├── static/                # Static assets
│   ├── style.css         # Main stylesheet
│   ├── auth.css          # Authentication styles
│   ├── contact.css       # Contact page styles
│   ├── cart.css          # Cart page styles
│   ├── orderPlaced.css   # Order confirmation styles
│   ├── style_sneakers.css # Product catalog styles
│   ├── script.js         # JavaScript functionality
│   ├── *.png, *.jpg      # Product images
│   ├── *.ico             # Favicons
│   └── pay/              # Payment images
├── db.sqlite3            # SQLite database
└── manage.py             # Django management script
```

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Installation Steps

1. **Clone or navigate to the project directory**
   ```bash
   cd "e:\django project\andreka"
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   # source venv/bin/activate  # On macOS/Linux
   ```

3. **Install Django**
   ```bash
   pip install django
   ```

4. **Run database migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Start the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Open your browser and go to `http://127.0.0.1:8000/`
   - Admin panel: `http://127.0.0.1:8000/admin/`

## 🎯 Available Pages & URLs

| URL | Page | Description |
|-----|------|-------------|
| `/` | Home | Main landing page with product showcase |
| `/contact/` | Contact | Contact form and information |
| `/sneakers/` | Product Catalog | Browse available sneakers |
| `/product/` | Product Details | Individual product information |
| `/cart/` | Shopping Cart | View and manage cart items |
| `/order-placed/` | Order Confirmation | Order completion page |
| `/button/` | Button Demo | Interactive button examples |
| `/signup/` | User Registration | Create new user account |
| `/accounts/login/` | User Login | Sign in to existing account |
| `/accounts/logout/` | User Logout | Sign out of account |
| `/dashboard/` | User Dashboard | Protected user area |

## 🔐 User Authentication

The project includes a complete user authentication system:

- **Registration**: Users can create new accounts via `/signup/`
- **Login**: Existing users can sign in via `/accounts/login/`
- **Dashboard**: Protected area accessible only to logged-in users
- **Logout**: Secure logout functionality
- **Redirects**: Automatic redirects after login/logout actions

### Authentication Settings
- Login redirect: `/dashboard/`
- Logout redirect: `/` (homepage)
- Login URL: `/accounts/login/`

## 🎨 Styling & Design

The project features a cohesive design system:

- **Color Palette**: Warm, earthy tones with professional gradients
- **Typography**: Montserrat font family for modern readability
- **Layout**: Card-based design with subtle shadows and rounded corners
- **Responsive**: Mobile-first approach with flexible layouts
- **Interactive**: Hover effects and smooth transitions

## 🗄️ Database

The project uses SQLite as the default database, which includes:

- Django's built-in User model for authentication
- Automatic migrations for user management
- No additional models currently defined (ready for expansion)

## 🚀 Development

### Key Django Features Used

- **Static Files**: Properly configured static file serving
- **Templates**: Django template system with template tags
- **URL Routing**: Clean URL patterns with named routes
- **Views**: Function-based views for all pages
- **Authentication**: Django's built-in auth system
- **Forms**: UserCreationForm for registration

### Adding New Features

1. **New Pages**: Add views in `andrekaApp/views.py` and URLs in `andrekaApp/urls.py`
2. **New Models**: Define in `andrekaApp/models.py` and run migrations
3. **New Templates**: Add HTML files in `templates/` directory
4. **New Styles**: Add CSS files in `static/` directory

## 📱 Browser Support

- Chrome (recommended)
- Firefox
- Safari
- Edge
- Mobile browsers (responsive design)

## 🔧 Configuration

### Environment Variables
No environment variables are currently required. The project uses Django's default settings for development.

### Static Files
Static files are configured to be served from the `static/` directory and are properly linked in templates using Django's `{% static %}` template tag.

## 📝 License

This project is for educational and development purposes.

## 🤝 Contributing

This is a personal project, but suggestions and improvements are welcome!

## 📞 Support

For questions or issues, please refer to the Django documentation or create an issue in the project repository.

---

**Built with ❤️ using Django**
