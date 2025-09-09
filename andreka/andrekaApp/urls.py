from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contact/', views.contact, name='contact'),
    path('sneakers/', views.sneakers, name='sneakers'),
    path('product/', views.product_detail, name='product_detail'),
    path('cart/', views.cart, name='cart'),
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
]

