from django.shortcuts import render
from rest_framework import viewsets
from .models import User, Product, Category, Review
from .serializers import UserSerializer, ProductSerializer, CategorySerializer, ReviewSerializer
from .models import *
from rest_framework.decorators import action
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework import status, generics
from django.shortcuts import HttpResponse, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, decorators, logout, forms
from .tasks import notify_user_of_order
from .forms import ReviewForm
from .serializers import NotificationSerializer


def get_index(request):
    products = Product.objects.all()
    return render(request, "index.html", {"products": products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})

def product_list(request):
    category_id = request.GET.get('category')
    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'products.html', {'products': products, 'categories': categories})



def basic_form(request, given_form):
    if request.method == 'POST':
        form = given_form(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("OK")
        else:
            raise Exception(f"some erros {form.errors}")
    return render(request, 'login.html', {'form': given_form()})


def register_view(request):
    return basic_form(request, forms.UserCreationForm)


def logout_view(request):
    logout(request)
    return redirect("main-home")


def login_view(request):
    if request.method == 'POST':
        form = forms.AuthenticationForm(data=request.POST)
        if form.is_valid():
            try:
                user = authenticate(**form.cleaned_data)
                login(request, user)
                if next := request.GET.get("next"):
                    return redirect(next)
                return redirect("main-home")
            except Exception:
                return HttpResponse("something is not ok")
        else:
            raise Exception(f"some erros {form.errors}")
    return render(request, 'login.html', {'form': forms.AuthenticationForm()})

@login_required
def cart_view(request):
    cart = Cart.objects.filter(user=request.user)
    return render(request, 'cart.html', {'cart': cart})

@login_required
def orders_view(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'orders.html', {'orders': orders})

@login_required
def create_review(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()
            return redirect('product-detail', pk=pk)
    else:
        form = ReviewForm()
    return render(request, 'review_form.html', {'form': form})

@login_required
def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart')

@login_required
def remove_from_cart(request, cart_id):
    cart_item = get_object_or_404(Cart, id=cart_id, user=request.user)
    cart_item.delete()
    return redirect('cart')

@login_required
def create_order(request, product_id):
    product = Product.objects.get(id=product_id)
    order, created = Order.objects.get_or_create(user=request.user, status='Pending')
    if created:
        cart_item, _ = Cart.objects.get_or_create(user=request.user, product=product)
        cart_item.quantity = 1
        cart_item.save()
    return redirect('orders')

@login_required
def notification_list(request):
    queryset = Notification.objects.filter(user=request.user)
    serializer = NotificationSerializer(queryset, many=True)
    notifications = serializer.data
    return render(request, "notifications.html", {"notifications": notifications})