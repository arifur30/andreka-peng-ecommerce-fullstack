# Cart System Fix - Step by Step Guide

## ✅ **Issues Fixed:**

1. **CSRF Token Problem**: Fixed JavaScript CSRF token handling
2. **Error Handling**: Improved error messages and debugging
3. **Template Issues**: Updated all templates with proper CSRF handling

## 📋 **Step-by-Step Instructions:**

### **Step 1: Restart Your Development Server**
```bash
# Stop the current server (Ctrl+C)
# Then restart it
cd andreka
python manage.py runserver
```

### **Step 2: Clear Browser Cache**
- Press `Ctrl + F5` to hard refresh the page
- Or clear your browser cache completely

### **Step 3: Test Cart Functionality**

#### **Test 1: Add to Cart from Homepage**
1. Go to `http://localhost:8000/`
2. Click the shopping cart icon on any product
3. You should see a green notification: "Product name added to cart"
4. Check the cart icon in the header - it should show a red badge with the number

#### **Test 2: Add to Cart from Product Detail Page**
1. Click on any product to go to its detail page
2. Change the quantity if desired
3. Click "Add to Cart" button
4. You should see the success notification

#### **Test 3: View Cart**
1. Click the cart icon in the header
2. You should see all added items
3. Test quantity controls (+ and - buttons)
4. Test remove button

### **Step 4: Debugging (If Still Not Working)**

#### **Check Browser Console:**
1. Press `F12` to open Developer Tools
2. Go to "Console" tab
3. Try adding to cart
4. Look for any error messages

#### **Check Network Tab:**
1. In Developer Tools, go to "Network" tab
2. Try adding to cart
3. Look for the `add-to-cart/` request
4. Check if it returns status 200 or an error

#### **Common Issues and Solutions:**

**Issue 1: "CSRF token not found"**
- **Solution**: Refresh the page completely (Ctrl+F5)

**Issue 2: "Network Error"**
- **Solution**: Check if Django server is running on port 8000

**Issue 3: "Product not found"**
- **Solution**: Make sure you have products in your database

**Issue 4: "Permission denied"**
- **Solution**: Check if you're logged in (cart works for both logged-in and guest users)

### **Step 5: Verify Database**

#### **Check if Products Exist:**
```bash
cd andreka
python manage.py shell
```

In the shell:
```python
from andrekaApp.models import Product
print(Product.objects.count())  # Should be > 0
print(Product.objects.filter(is_available=True).count())  # Should be > 0
```

#### **Check Cart Data:**
```python
from andrekaApp.models import Cart, CartItem
print(Cart.objects.count())
print(CartItem.objects.count())
```

### **Step 6: Test Complete Flow**

1. **Add Multiple Items**: Add different products to cart
2. **Check Cart Page**: Go to `/cart/` and verify items are there
3. **Update Quantities**: Use + and - buttons
4. **Remove Items**: Test the remove button
5. **Proceed to Checkout**: Click "Proceed to Checkout" button

## 🔧 **Technical Details of Fixes:**

### **1. CSRF Token Fix**
- Added `<meta name="csrf-token" content="{{ csrf_token }}">` to base template
- Updated JavaScript to get CSRF token from meta tag
- Added proper error handling for missing CSRF token

### **2. Error Handling Improvements**
- Added better error messages
- Added HTTP status code checking
- Added proper exception handling

### **3. Template Updates**
- Fixed `index.html` cart functionality
- Fixed `sproduct.html` cart functionality  
- Fixed `cart.html` update/remove functionality
- Updated `base.html` with CSRF meta tag

## 🚨 **If Cart Still Doesn't Work:**

### **Check These Files:**
1. Make sure `andrekaApp/urls.py` has the cart URLs
2. Make sure `andrekaApp/views.py` has the cart views
3. Make sure `models.py` has Cart and CartItem models

### **Run These Commands:**
```bash
# Check for any Python errors
python manage.py check

# Check if migrations are applied
python manage.py showmigrations

# Apply any pending migrations
python manage.py migrate
```

### **Test with Sample Data:**
```bash
python manage.py shell
```

```python
from andrekaApp.models import Product, Cart, CartItem
from django.contrib.auth.models import User

# Create a test product if none exist
if Product.objects.count() == 0:
    Product.objects.create(
        name="Test Product",
        slug="test-product",
        description="Test description",
        price=29.99,
        stock=10,
        category="test",
        is_available=True
    )
    print("Test product created")

# Check cart functionality
cart = Cart.objects.create()
print(f"Cart created: {cart.id}")
```

## 📞 **Still Having Issues?**

If the cart still doesn't work after following these steps:

1. **Check Browser Console** for JavaScript errors
2. **Check Django Logs** in the terminal where you're running the server
3. **Try Different Browser** to rule out browser-specific issues
4. **Check Network Tab** to see if requests are being made

The cart system should now work properly! The main issue was the CSRF token handling in JavaScript, which has been fixed.

