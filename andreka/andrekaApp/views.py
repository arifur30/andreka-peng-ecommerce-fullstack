from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.admin.views.decorators import staff_member_required
from django.views.decorators.csrf import csrf_exempt
from .models import UserProfile, Order, OrderItem, Product, Cart, CartItem, Payment, BlogPost, BlogImage
from .sslcommerz_service import SSLCOMMERZPaymentService
import logging

logger = logging.getLogger(__name__)
import uuid
import json

# Create your views here.

def get_or_create_cart(request):
    """Get or create cart for user or session"""
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
    else:
        session_key = request.session.session_key
        if not session_key:
            request.session.create()
            session_key = request.session.session_key
        cart, created = Cart.objects.get_or_create(session_key=session_key)
    return cart

def collection_carousel(request):
    products = Product.objects.filter(is_available=True).order_by('-created_at')
    return render(request, 'collection.html', {'products': products})

@staff_member_required
def seed_products(request):
    products_data = [
        {
            'name': 'The Urban Nomad Trench',
            'slug': 'womens-trench-coat',
            'description': 'A classic, longline trench coat perfect for adding a sophisticated layer to any outfit. Its versatile design and neutral tone make it a timeless piece for both daily wear and travel.',
            'price': 189.99,
            'stock': 12,
            'category': 'womens-fashion',
            'is_available': True,
        },
        {
            'name': 'Metropolitan Chic Blazer',
            'slug': 'womens-camel-blazer',
            'description': 'A single-breasted blazer in a warm camel tone, ideal for creating a polished and professional look. It can be paired with matching trousers or worn as a standout piece over a simple dress.',
            'price': 115.50,
            'stock': 25,
            'category': 'womens-fashion',
            'is_available': True,
        },
        # Add more products here...
    ]
    
    for product_data in products_data:
        Product.objects.create(**product_data)
    
    messages.success(request, 'Products have been added successfully!')
    return redirect('admin:andrekaApp_product_changelist')

def index(request):
    products = Product.objects.filter(is_available=True).order_by('-created_at')[:8]  # Get latest 8 products
    return render(request, 'index.html', {'products': products})


def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')


def sneakers(request):
    products = Product.objects.filter(is_available=True, category='sneakers')
    return render(request, 'sneakers.html', {'products': products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_available=True)
    related_products = Product.objects.filter(category=product.category, is_available=True).exclude(id=product.id)[:4]
    return render(request, 'sproduct.html', {'product': product, 'related_products': related_products})




def order_placed(request):
    return render(request, 'orderplaced.html')


def button_demo(request):
    return render(request, 'button.html')


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


@login_required
def dashboard_view(request):
    return render(request, 'dashboard.html')


@login_required
def profile_view(request):
    """View user profile with all sections"""
    profile = get_object_or_404(UserProfile, user=request.user)
    orders = Order.objects.filter(user=request.user).order_by('-created_at')[:10]  # Last 10 orders
    
    context = {
        'profile': profile,
        'orders': orders,
    }
    return render(request, 'profile/profile.html', context)


@login_required
def edit_profile_view(request):
    """Edit user profile information"""
    profile = get_object_or_404(UserProfile, user=request.user)
    
    if request.method == 'POST':
        # Update user basic info
        request.user.first_name = request.POST.get('first_name', '')
        request.user.last_name = request.POST.get('last_name', '')
        request.user.email = request.POST.get('email', '')
        request.user.save()
        
        # Update profile info
        profile.phone_number = request.POST.get('phone_number', '')
        profile.date_of_birth = request.POST.get('date_of_birth') or None
        profile.gender = request.POST.get('gender', '')
        profile.save()
        
        messages.success(request, 'Personal information updated successfully!')
        return redirect('profile')
    
    context = {
        'profile': profile,
    }
    return render(request, 'profile/edit_profile.html', context)


@login_required
def edit_billing_view(request):
    """Edit billing information"""
    profile = get_object_or_404(UserProfile, user=request.user)
    
    if request.method == 'POST':
        profile.billing_first_name = request.POST.get('billing_first_name', '')
        profile.billing_last_name = request.POST.get('billing_last_name', '')
        profile.billing_email = request.POST.get('billing_email', '')
        profile.billing_phone = request.POST.get('billing_phone', '')
        profile.save()
        
        messages.success(request, 'Billing information updated successfully!')
        return redirect('profile')
    
    context = {
        'profile': profile,
    }
    return render(request, 'profile/edit_billing.html', context)


@login_required
def edit_address_view(request):
    """Edit address information"""
    profile = get_object_or_404(UserProfile, user=request.user)
    
    if request.method == 'POST':
        profile.address_line_1 = request.POST.get('address_line_1', '')
        profile.address_line_2 = request.POST.get('address_line_2', '')
        profile.city = request.POST.get('city', '')
        profile.state = request.POST.get('state', '')
        profile.postal_code = request.POST.get('postal_code', '')
        profile.country = request.POST.get('country', '')
        profile.save()
        
        messages.success(request, 'Address information updated successfully!')
        return redirect('profile')
    
    context = {
        'profile': profile,
    }
    return render(request, 'profile/edit_address.html', context)


@login_required
def order_history_view(request):
    """View complete order history"""
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    
    context = {
        'orders': orders,
    }
    return render(request, 'profile/order_history.html', context)


@login_required
def order_detail_view(request, order_id):
    """View detailed order information"""
    order = get_object_or_404(Order, id=order_id, user=request.user)
    
    context = {
        'order': order,
    }
    return render(request, 'profile/order_detail.html', context)

# Cart Views
@csrf_exempt
@require_POST
def add_to_cart(request):
    """Add product to cart - single quantity from index, custom quantity from product detail"""
    try:
        data = json.loads(request.body)
        product_id = data.get('product_id')
        quantity = int(data.get('quantity', 1))  # Default to 1 for index page
        
        product = get_object_or_404(Product, id=product_id, is_available=True)
        
        if quantity > product.stock:
            return JsonResponse({'success': False, 'message': 'Not enough stock available'})
        
        cart = get_or_create_cart(request)
        
        # Check if product already exists in cart
        cart_item, created = CartItem.objects.get_or_create(
            cart=cart,
            product=product,
            defaults={'quantity': quantity}
        )
        
        if not created:
            # If item exists, add to existing quantity
            cart_item.quantity += quantity
            if cart_item.quantity > product.stock:
                cart_item.quantity = product.stock
            cart_item.save()
        
        return JsonResponse({
            'success': True, 
            'message': f'{product.name} added to cart',
            'cart_total': cart.total_items,
            'cart_price': float(cart.total_price)
        })
        
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)})

@csrf_exempt
@require_POST
def update_cart_item(request):
    """Update cart item quantity"""
    try:
        data = json.loads(request.body)
        item_id = data.get('item_id')
        quantity = int(data.get('quantity', 1))
        
        cart_item = get_object_or_404(CartItem, id=item_id)
        
        if quantity <= 0:
            cart_item.delete()
        else:
            if quantity > cart_item.product.stock:
                return JsonResponse({'success': False, 'message': 'Not enough stock available'})
            cart_item.quantity = quantity
            cart_item.save()
        
        cart = cart_item.cart
        return JsonResponse({
            'success': True,
            'cart_total': cart.total_items,
            'cart_price': float(cart.total_price),
            'item_total': float(cart_item.total_price) if quantity > 0 else 0
        })
        
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)})

@csrf_exempt
@require_POST
def remove_from_cart(request):
    """Remove item from cart"""
    try:
        data = json.loads(request.body)
        item_id = data.get('item_id')
        
        cart_item = get_object_or_404(CartItem, id=item_id)
        cart = cart_item.cart
        cart_item.delete()
        
        return JsonResponse({
            'success': True,
            'cart_total': cart.total_items,
            'cart_price': float(cart.total_price)
        })
        
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)})

def cart_view(request):
    """Display cart page"""
    cart = get_or_create_cart(request)
    cart_items = cart.items.all()
    
    context = {
        'cart': cart,
        'cart_items': cart_items,
    }
    return render(request, 'cart.html', context)

def cart(request):
    return render(request, 'cart.html')

# Payment Views
@login_required
def checkout_view(request):
    """Display checkout page with payment options"""
    cart = get_or_create_cart(request)
    cart_items = cart.items.all()
    
    if not cart_items:
        messages.warning(request, 'Your cart is empty.')
        return redirect('cart')
    
    # Calculate total
    total_amount = sum(item.total_price for item in cart_items)
    
    context = {
        'cart': cart,
        'cart_items': cart_items,
        'total_amount': total_amount,
    }
    return render(request, 'checkout.html', context)

@login_required
@require_POST
def create_order(request):
    """Create order and redirect to payment"""
    try:
        cart = get_or_create_cart(request)
        cart_items = cart.items.all()
        
        if not cart_items:
            return JsonResponse({'success': False, 'message': 'Cart is empty'})
        
        # Get form data
        shipping_first_name = request.POST.get('shipping_first_name')
        shipping_last_name = request.POST.get('shipping_last_name')
        shipping_address_line_1 = request.POST.get('shipping_address_line_1')
        shipping_address_line_2 = request.POST.get('shipping_address_line_2', '')
        shipping_city = request.POST.get('shipping_city')
        shipping_state = request.POST.get('shipping_state')
        shipping_postal_code = request.POST.get('shipping_postal_code')
        shipping_country = request.POST.get('shipping_country')
        
        billing_first_name = request.POST.get('billing_first_name', shipping_first_name)
        billing_last_name = request.POST.get('billing_last_name', shipping_last_name)
        billing_address_line_1 = request.POST.get('billing_address_line_1', shipping_address_line_1)
        billing_address_line_2 = request.POST.get('billing_address_line_2', shipping_address_line_2)
        billing_city = request.POST.get('billing_city', shipping_city)
        billing_state = request.POST.get('billing_state', shipping_state)
        billing_postal_code = request.POST.get('billing_postal_code', shipping_postal_code)
        billing_country = request.POST.get('billing_country', shipping_country)
        
        payment_method = request.POST.get('payment_method')
        
        # Validate required fields
        required_fields = [
            shipping_first_name, shipping_last_name, shipping_address_line_1,
            shipping_city, shipping_state, shipping_postal_code, shipping_country
        ]
        
        if not all(required_fields):
            return JsonResponse({'success': False, 'message': 'Please fill all required fields'})
        
        # Calculate total amount
        total_amount = sum(item.total_price for item in cart_items)
        
        # Generate order number
        order_number = f"ORD_{uuid.uuid4().hex[:8].upper()}"
        
        # Create order
        order = Order.objects.create(
            user=request.user,
            order_number=order_number,
            total_amount=total_amount,
            shipping_first_name=shipping_first_name,
            shipping_last_name=shipping_last_name,
            shipping_address_line_1=shipping_address_line_1,
            shipping_address_line_2=shipping_address_line_2,
            shipping_city=shipping_city,
            shipping_state=shipping_state,
            shipping_postal_code=shipping_postal_code,
            shipping_country=shipping_country,
            billing_first_name=billing_first_name,
            billing_last_name=billing_last_name,
            billing_address_line_1=billing_address_line_1,
            billing_address_line_2=billing_address_line_2,
            billing_city=billing_city,
            billing_state=billing_state,
            billing_postal_code=billing_postal_code,
            billing_country=billing_country,
        )
        
        # Create order items
        for cart_item in cart_items:
            OrderItem.objects.create(
                order=order,
                product_name=cart_item.product.name,
                product_price=cart_item.product.price,
                quantity=cart_item.quantity
            )
        
        # Handle payment based on method
        if payment_method == 'sslcommerz':
            customer_email = request.POST.get('customer_email', order.user.email or 'arifafjr17@gmail.com')
            customer_phone = request.POST.get('customer_phone', '+8801878125712')
            
            return JsonResponse({
                'success': True,
                'order_id': order.id,
                'order_number': order_number,
                'payment_method': 'sslcommerz',
                'redirect_url': f'/payment/sslcommerz/create/{order.id}/?customer_email={customer_email}&customer_phone={customer_phone}'
            })
        elif payment_method == 'cash_on_delivery':
            # Create COD payment record
            Payment.objects.create(
                order=order,
                payment_id=f"COD_{order_number}",
                payment_method='cash_on_delivery',
                amount=total_amount,
                status='pending'
            )
            
            # Clear cart
            cart_items.delete()
            
            return JsonResponse({
                'success': True,
                'order_id': order.id,
                'order_number': order_number,
                'payment_method': 'cash_on_delivery',
                'redirect_url': f'/order/success/{order.id}/'
            })
        else:
            return JsonResponse({'success': False, 'message': 'Invalid payment method'})
            
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)})

@login_required
def sslcommerz_payment_create(request, order_id):
    """Create SSLCOMMERZ payment and redirect to SSLCOMMERZ"""
    try:
        order = get_object_or_404(Order, id=order_id, user=request.user)
        
        # Check if payment already exists
        existing_payment = Payment.objects.filter(order=order, payment_method='sslcommerz').first()
        if existing_payment and existing_payment.status == 'completed':
            return redirect('order_success', order_id=order.id)
        
        # Get customer information from form data
        customer_email = request.GET.get('customer_email', order.user.email or 'arifafjr17@gmail.com')
        customer_phone = request.GET.get('customer_phone', '+8801878125712')
        
        customer_info = {
            'name': order.user.get_full_name() or order.user.username,
            'email': customer_email,
            'phone': customer_phone
        }
        
        # Create SSLCOMMERZ payment
        sslcommerz_service = SSLCOMMERZPaymentService()
        result = sslcommerz_service.create_payment(order, order.total_amount, customer_info)
        
        if result['success']:
            # Update payment record with SSLCOMMERZ session key
            payment = result['payment']
            payment.sslcommerz_session_key = result['session_key']
            payment.save()
            
            # Redirect to SSLCOMMERZ payment page
            return redirect(result['gateway_url'])
        else:
            messages.error(request, f"Payment creation failed: {result['message']}")
            return redirect('checkout')
            
    except Exception as e:
        messages.error(request, f"An error occurred: {str(e)}")
        return redirect('checkout')

@csrf_exempt
def sslcommerz_payment_ipn(request):
    """Handle SSLCOMMERZ IPN (Instant Payment Notification)"""
    try:
        if request.method != 'POST':
            return JsonResponse({'success': False, 'message': 'Only POST method allowed'})
        
        # Get IPN data
        tran_id = request.POST.get('tran_id')
        val_id = request.POST.get('val_id')
        amount = request.POST.get('amount')
        status = request.POST.get('status')
        
        if not tran_id or not val_id:
            return JsonResponse({'success': False, 'message': 'Missing required parameters'})
        
        # Find payment record
        payment = Payment.objects.filter(payment_id=tran_id).first()
        if not payment:
            return JsonResponse({'success': False, 'message': 'Payment not found'})
        
        # Validate payment with SSLCOMMERZ
        sslcommerz_service = SSLCOMMERZPaymentService()
        validation_result = sslcommerz_service.validate_payment(val_id)
        
        if validation_result['success'] and validation_result['status'] in ['VALID', 'VALIDATED']:
            validation_data = validation_result['data']
            
            # Update payment status
            payment.status = 'completed'
            payment.sslcommerz_val_id = val_id
            payment.sslcommerz_bank_tran_id = validation_data.get('bank_tran_id', '')
            payment.sslcommerz_card_type = validation_data.get('card_type', '')
            payment.sslcommerz_card_no = validation_data.get('card_no', '')
            payment.sslcommerz_card_issuer = validation_data.get('card_issuer', '')
            payment.sslcommerz_card_brand = validation_data.get('card_brand', '')
            payment.sslcommerz_store_amount = validation_data.get('store_amount', 0)
            payment.gateway_response = validation_data
            payment.save()
            
            # Update order status
            payment.order.status = 'processing'
            payment.order.save()
            
            # Clear cart for the user
            if request.user.is_authenticated:
                cart = get_or_create_cart(request)
                cart.items.all().delete()
            
            return JsonResponse({'success': True, 'message': 'Payment processed successfully'})
        else:
            payment.status = 'failed'
            payment.failure_reason = f"Validation failed: {validation_result.get('message', 'Unknown error')}"
            payment.save()
            
            return JsonResponse({'success': False, 'message': 'Payment validation failed'})
            
    except Exception as e:
        logger.error(f"Error processing SSLCOMMERZ IPN: {str(e)}")
        return JsonResponse({'success': False, 'message': str(e)})

@csrf_exempt
def sslcommerz_payment_success(request):
    """Handle SSLCOMMERZ payment success redirect"""
    try:
        # SSLCOMMERZ sends data via POST, not GET
        tran_id = request.POST.get('tran_id') or request.GET.get('tran_id')
        val_id = request.POST.get('val_id') or request.GET.get('val_id')
        
        logger.info(f"SSLCOMMERZ Success Callback - Method: {request.method}")
        logger.info(f"SSLCOMMERZ Success Callback - POST data: {dict(request.POST)}")
        logger.info(f"SSLCOMMERZ Success Callback - GET data: {dict(request.GET)}")
        logger.info(f"SSLCOMMERZ Success Callback - tran_id: {tran_id}, val_id: {val_id}")
        
        # If no tran_id, try to find the latest pending payment for this session
        if not tran_id:
            logger.warning("No tran_id found, looking for latest pending payment")
            # Try to find the most recent pending payment
            latest_payment = Payment.objects.filter(
                status='pending',
                payment_method='sslcommerz'
            ).order_by('-created_at').first()
            
            if latest_payment:
                tran_id = latest_payment.payment_id
                logger.info(f"Found latest pending payment: {tran_id}")
            else:
                logger.error("No tran_id in SSLCOMMERZ success callback and no pending payments found")
                messages.error(request, 'Invalid payment response')
                return redirect('checkout')
        
        # Find payment record (don't require login for this callback)
        payment = Payment.objects.filter(payment_id=tran_id).first()
        if not payment:
            logger.error(f"Payment not found for tran_id: {tran_id}")
            messages.error(request, 'Payment not found')
            return redirect('checkout')
        
        logger.info(f"Found payment: {payment.id}, status: {payment.status}")
        
        # If payment is already completed, redirect to success page
        if payment.status == 'completed':
            logger.info(f"Payment already completed, redirecting to success page")
            return redirect('order_success', order_id=payment.order.id)
        
        # Mark payment as completed (since SSLCOMMERZ redirected to success)
        payment.status = 'completed'
        payment.gateway_response = {'success_redirect': True, 'tran_id': tran_id, 'val_id': val_id}
        payment.save()
        
        # Update order status
        payment.order.status = 'processing'
        payment.order.save()
        
        logger.info(f"Payment marked as completed, order status updated to processing")
        
        # Clear cart for the user (if they're logged in)
        if request.user.is_authenticated:
            cart = get_or_create_cart(request)
            cart.items.all().delete()
            logger.info("Cart cleared for authenticated user")
        else:
            # If user is not authenticated, try to clear cart based on order user
            try:
                cart = Cart.objects.filter(user=payment.order.user).first()
                if cart:
                    cart.items.all().delete()
                    logger.info(f"Cart cleared for user {payment.order.user.id} (not authenticated)")
            except Exception as cart_error:
                logger.warning(f"Could not clear cart: {cart_error}")
        
        # Redirect to success page
        logger.info(f"Redirecting to order success page for order {payment.order.id}")
        return redirect('order_success', order_id=payment.order.id)
        
    except Exception as e:
        logger.error(f"Error in SSLCOMMERZ success callback: {str(e)}")
        messages.error(request, f"An error occurred: {str(e)}")
        return redirect('checkout')

@csrf_exempt
def sslcommerz_payment_fail(request):
    """Handle SSLCOMMERZ payment failure redirect"""
    try:
        # SSLCOMMERZ sends data via POST, not GET
        tran_id = request.POST.get('tran_id') or request.GET.get('tran_id')
        
        logger.info(f"SSLCOMMERZ Fail Callback - Method: {request.method}")
        logger.info(f"SSLCOMMERZ Fail Callback - tran_id: {tran_id}")
        
        if tran_id:
            payment = Payment.objects.filter(payment_id=tran_id).first()
            if payment:
                payment.status = 'failed'
                payment.failure_reason = 'Payment failed at SSLCOMMERZ'
                payment.save()
                
                logger.info(f"Payment marked as failed for tran_id: {tran_id}")
                messages.error(request, 'Payment failed. Please try again.')
                return redirect('order_failed', order_id=payment.order.id)
        
        logger.warning("No tran_id found in fail callback")
        messages.error(request, 'Payment failed. Please try again.')
        return redirect('checkout')
        
    except Exception as e:
        logger.error(f"Error in SSLCOMMERZ fail callback: {str(e)}")
        messages.error(request, f"An error occurred: {str(e)}")
        return redirect('checkout')

@csrf_exempt
def sslcommerz_payment_cancel(request):
    """Handle SSLCOMMERZ payment cancellation redirect"""
    try:
        # SSLCOMMERZ sends data via POST, not GET
        tran_id = request.POST.get('tran_id') or request.GET.get('tran_id')
        
        logger.info(f"SSLCOMMERZ Cancel Callback - Method: {request.method}")
        logger.info(f"SSLCOMMERZ Cancel Callback - tran_id: {tran_id}")
        
        if tran_id:
            payment = Payment.objects.filter(payment_id=tran_id).first()
            if payment:
                payment.status = 'cancelled'
                payment.failure_reason = 'Payment cancelled by user'
                payment.save()
                
                logger.info(f"Payment marked as cancelled for tran_id: {tran_id}")
                messages.warning(request, 'Payment was cancelled.')
                return redirect('order_failed', order_id=payment.order.id)
        
        logger.warning("No tran_id found in cancel callback")
        messages.warning(request, 'Payment was cancelled.')
        return redirect('checkout')
        
    except Exception as e:
        logger.error(f"Error in SSLCOMMERZ cancel callback: {str(e)}")
        messages.error(request, f"An error occurred: {str(e)}")
        return redirect('checkout')

@login_required
def order_success(request, order_id):
    """Display order success page"""
    order = get_object_or_404(Order, id=order_id, user=request.user)
    payment = order.payments.filter(status='completed').first()
    
    context = {
        'order': order,
        'payment': payment,
    }
    return render(request, 'order_success.html', context)

@login_required
def order_failed(request, order_id):
    """Display order failed page"""
    order = get_object_or_404(Order, id=order_id, user=request.user)
    payment = order.payments.first()
    
    context = {
        'order': order,
        'payment': payment,
    }
    return render(request, 'order_failed.html', context)

def services(request):
    """Display services page"""
    return render(request, 'services.html')

def blog_list(request):
    """Display blog list page"""
    posts = BlogPost.objects.filter(status='published').order_by('-created_at')
    featured_posts = BlogPost.objects.filter(is_featured=True, status='published')[:3]
    
    # Get categories for filtering
    categories = BlogPost.CATEGORY_CHOICES
    
    # Filter by category if provided
    category = request.GET.get('category')
    if category:
        posts = posts.filter(category=category)
    
    context = {
        'posts': posts,
        'featured_posts': featured_posts,
        'categories': categories,
        'current_category': category,
    }
    return render(request, 'blog/blog_list.html', context)

def blog_detail(request, slug):
    """Display individual blog post"""
    post = get_object_or_404(BlogPost, slug=slug, status='published')
    
    # Increment view count
    post.views += 1
    post.save(update_fields=['views'])
    
    # Get related posts
    related_posts = BlogPost.objects.filter(
        category=post.category,
        status='published'
    ).exclude(id=post.id)[:3]
    
    context = {
        'post': post,
        'related_posts': related_posts,
    }
    return render(request, 'blog/blog_detail.html', context)
