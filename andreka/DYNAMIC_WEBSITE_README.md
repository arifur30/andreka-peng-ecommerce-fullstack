# Andreka & Peng - Dynamic E-commerce Website

## Overview
This Django-based e-commerce website has been updated to be fully dynamic with database connectivity. All products are now stored in the database and can be managed through the admin interface.

## Key Features Implemented

### 1. Dynamic Product Management
- **Database-driven products**: All products are now stored in the database using the `Product` model
- **Dynamic product details**: Product detail pages (`sproduct.html`) now fetch data from the database
- **Product slugs**: Each product has a unique slug for SEO-friendly URLs
- **Stock management**: Products include stock levels and availability status
- **Pricing**: Support for original price and discounted price display

### 2. Enhanced Collection Page
- **New collection page**: Created `collection.html` with interactive styles matching the homepage
- **Responsive design**: Grid layout that adapts to different screen sizes
- **Interactive elements**: Hover effects, smooth transitions, and modern UI
- **Product cards**: Beautiful product cards with overlay effects and discount badges
- **Stock indicators**: Shows stock warnings and out-of-stock status

### 3. Improved Navigation
- **Direct collection link**: Removed dropdown menu, Collection now links directly to the collection page
- **Consistent navbar**: All pages now use the base template with consistent navigation
- **Active page highlighting**: Current page is highlighted in the navigation

### 4. Admin Interface Enhancements
- **Enhanced Product Admin**: Improved admin interface for managing products
- **Bulk editing**: Can edit multiple product fields directly from the list view
- **Better organization**: Products organized with fieldsets for easier management
- **Search and filtering**: Enhanced search and filter capabilities

### 5. Sample Data Management
- **Management command**: Created `add_sample_products` command to populate the database
- **Sample products**: 8 sample products with realistic data and images
- **Easy setup**: Run `python manage.py add_sample_products` to add sample data

## File Structure Changes

### New Files Created:
- `templates/collection.html` - New collection page with interactive styles
- `management/commands/add_sample_products.py` - Command to add sample products
- `static/products/` - Directory for product images

### Modified Files:
- `models.py` - Enhanced Product model (already existed)
- `views.py` - Updated collection view to use new template
- `admin.py` - Enhanced admin interface for all models
- `sproduct.html` - Now extends base template and is fully dynamic
- `base.html` - Updated navbar with direct collection link

## Database Models

### Product Model
```python
class Product(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    original_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    image = models.ImageField(upload_to='products/')
    category = models.CharField(max_length=100)
    stock = models.IntegerField(default=0)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

## How to Use

### 1. Adding New Products
You can add new products in two ways:

#### Through Admin Interface:
1. Go to `/admin/` (login required)
2. Navigate to "Products" under "AndrekaApp"
3. Click "Add Product"
4. Fill in all required fields
5. Upload an image to `static/products/` directory
6. Save the product

#### Through Management Command:
1. Edit `management/commands/add_sample_products.py`
2. Add your product data to the `products_data` list
3. Run `python manage.py add_sample_products`

### 2. Managing Existing Products
- **Edit products**: Use the admin interface to modify product details
- **Bulk operations**: Select multiple products and edit them simultaneously
- **Stock management**: Update stock levels and availability status
- **Pricing**: Set original and discounted prices

### 3. Collection Page Features
- **Responsive grid**: Automatically adjusts to screen size
- **Hover effects**: Interactive product cards with smooth animations
- **Discount badges**: Automatically calculates and displays discount percentages
- **Stock warnings**: Shows low stock and out-of-stock indicators
- **Quick view**: Hover to see product details

## URL Structure

- `/` - Homepage with featured products
- `/collection/` - Collection page with all products
- `/product/<slug>/` - Individual product detail page
- `/admin/` - Admin interface for managing products
- `/contact/` - Contact page
- `/cart/` - Shopping cart
- `/profile/` - User profile management

## Technical Features

### Dynamic Content
- All product information is fetched from the database
- Product images are served from the `static/products/` directory
- Related products are automatically suggested based on category
- Stock levels are checked and displayed dynamically

### SEO Optimization
- Product URLs use slugs for better SEO
- Meta information is dynamically generated
- Clean, semantic HTML structure

### Performance
- Optimized database queries
- Image optimization and responsive loading
- Efficient template rendering

## Setup Instructions

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

3. **Create superuser**:
   ```bash
   python manage.py createsuperuser
   ```

4. **Add sample products**:
   ```bash
   python manage.py add_sample_products
   ```

5. **Run the server**:
   ```bash
   python manage.py runserver
   ```

6. **Access the website**:
   - Main site: `http://localhost:8000/`
   - Admin: `http://localhost:8000/admin/`

## Future Enhancements

- Shopping cart functionality
- User authentication and profiles
- Order management system
- Payment integration
- Product reviews and ratings
- Advanced search and filtering
- Wishlist functionality
- Email notifications

## Support

For any issues or questions, please check the Django documentation or contact the development team.
