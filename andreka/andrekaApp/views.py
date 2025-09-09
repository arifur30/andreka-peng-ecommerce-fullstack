from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import UserProfile, Order, OrderItem
import uuid

# Create your views here.

def index(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')


def sneakers(request):
    return render(request, 'sneakers.html')


def product_detail(request):
    return render(request, 'sproduct.html')


def cart(request):
    return render(request, 'cart.html')


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