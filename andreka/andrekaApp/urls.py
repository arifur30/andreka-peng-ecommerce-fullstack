from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('collection/', views.collection_carousel, name='collection_carousel'),
    path('admin/seed-products/', views.seed_products, name='seed_products'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('blog/', views.blog_list, name='blog_list'),
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('sneakers/', views.sneakers, name='sneakers'),
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),
    path('cart/', views.cart_view, name='cart'),
    path('add-to-cart/', views.add_to_cart, name='add_to_cart'),
    path('update-cart-item/', views.update_cart_item, name='update_cart_item'),
    path('remove-from-cart/', views.remove_from_cart, name='remove_from_cart'),
    path('order-placed/', views.order_placed, name='order_placed'),
    path('button/', views.button_demo, name='button_demo'),
    path('signup/', views.signup_view, name='signup'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    
    # Profile URLs
    path('profile/', views.profile_view, name='profile'),
    path('profile/edit/', views.edit_profile_view, name='edit_profile'),
    path('profile/billing/', views.edit_billing_view, name='edit_billing'),
    path('profile/address/', views.edit_address_view, name='edit_address'),
    path('profile/orders/', views.order_history_view, name='order_history'),
    path('profile/orders/<int:order_id>/', views.order_detail_view, name='order_detail'),
    
    # Payment URLs
    path('checkout/', views.checkout_view, name='checkout'),
    path('create-order/', views.create_order, name='create_order'),
    
    # SSLCOMMERZ Payment URLs
    path('payment/sslcommerz/create/<int:order_id>/', views.sslcommerz_payment_create, name='sslcommerz_payment_create'),
    path('payment/sslcommerz/ipn/', views.sslcommerz_payment_ipn, name='sslcommerz_payment_ipn'),
    path('payment/sslcommerz/success/', views.sslcommerz_payment_success, name='sslcommerz_payment_success'),
    path('payment/sslcommerz/fail/', views.sslcommerz_payment_fail, name='sslcommerz_payment_fail'),
    path('payment/sslcommerz/cancel/', views.sslcommerz_payment_cancel, name='sslcommerz_payment_cancel'),
    
    path('order/success/<int:order_id>/', views.order_success, name='order_success'),
    path('order/failed/<int:order_id>/', views.order_failed, name='order_failed'),
]

