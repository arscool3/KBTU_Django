from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from main.forms import ProductForm, ShopForm, CartForm
from django.contrib.auth.decorators import login_required, permission_required
from rest_framework.generics import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from main.models import Product, Shop, Cart, Order, Review
from main.serializers import ProductSerializer, CartSerializer

class CartViewSet(ModelViewSet):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()
    lookup_field='id'
    
        


def get_products(request):
    products = Product.objects.all()
    return render(request, "index.html", {"products":products})

def sort_by_category(request):
    product = Product.objects.get_prods_by_category(request.GET['category_name'])
    return render(request, 'category_prods.html', {'products': product})

def get_prod(request):
    product = Product.objects.get_product(request.GET['prod_id'])
    return render(request, 'product.html', {'product': product})

def order_prods_by_price(request):
    products = Product.objects.sort_by_price()
    return render(request, "index.html", {"products":products})


def get_shops_by_city(request):
    shops = Shop.objects.cities_shops(request.GET['city_name'])
    return render(request, 'shops.html', {'shops': shops})

def order_shops_budget(request):
    shops = Shop.objects.shops_by_budget()
    return render(request, 'shops.html', {'shops': shops})

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main')
        else:
            messages.success(request, ("Error occured, invalid username or password"))
            return redirect('login')
    else:
        return render(request, 'login.html', {})
    
def logout_user(request):
    logout(request)
    return redirect('main')

def signup_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('main')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form':form})



def add_model(request, given_form, given_url, name):
    if request.method == "POST":
        form = given_form(request.POST)
        if form.is_valid():
            form.save()
        else:
            raise Exception(f"Some Exception {form.errors}")
        return HttpResponse(f'OK, {name} was created')

    return render(request, 'create.html', {'form': given_form(), 'given_url': given_url})

@permission_required("main.add_product", login_url="login_user", raise_exception=True)
def addProduct(request):
    return add_model(request, ProductForm, 'add_product', 'add_prod')

@permission_required("main.add_shop", login_url="login_user", raise_exception=True)
def addShop(request):
    return add_model(request, ShopForm, 'add_shop', 'shop')

@permission_required("main.add_cart", login_url="add_cart", raise_exception=True)
def addCart(request):
    return add_model(request, CartForm, 'add_cart', 'add_cart')