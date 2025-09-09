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
]

