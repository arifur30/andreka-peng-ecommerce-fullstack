from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

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