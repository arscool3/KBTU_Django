from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, decorators, logout
from django.contrib.auth.forms import AuthenticationForm
from .models import *
from .forms import *


def basic_form(request, given_form):
    if request.method == 'POST':
        form = given_form(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('products')
        else:
            raise Exception(f"some erros {form.errors}")
    return render(request, 'index.html', {'form': given_form()})

def register_view(request):
    return basic_form(request, CustomUserCreationForm)

def logout_view(request):
    logout(request)
    return redirect('products')

def check_view(request):
    if request.user.is_authenticated:
        return HttpResponse(f"{request.user} is authenticated")
    return HttpResponse(f"{request.user} is not authenticated")

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            try:
                user = authenticate(**form.cleaned_data)
                login(request, user)
                if next := request.GET.get("next"):
                    return redirect(next)
                return redirect('products')
            except Exception:
                return HttpResponse("something is not ok")
        else:
            raise Exception(f"some erros {form.errors}")
    return render(request, 'index.html', {'form': AuthenticationForm()})


def get_products(request):
    categories = Category.objects.all()
    products = Product.objects
    form = ProductPriceForm(request.POST)
    if name := request.GET.get('name'):
        products = products.filter(name=name.capitalize())
    products = products.all()
    return render(request, "productlist.html", {"iterable": products,"categories": categories, "object": "Products", 'form': form, "user":request.user.is_authenticated})



def add_category(request):
    form = CategoryForm(request.POST)
    if form.is_valid():
            form.save()
            return redirect('categories')
    return render(request, "main.html", { "object": "Category", 'form': form})

def get_category_list(request):
    categories = Category.objects
    form = CategoryForm()
    if name := request.GET.get('name'):
        categories = categories.filter(name=name.capitalize())
    categories = categories.all()
    return render(request, "categories.html", {"ss": categories, "object": "Categories", 'form': form})


def add_product(request):
    form = ProductPriceForm(request.POST)
    if form.is_valid():
            form.save()
            return redirect('categories')
    return render(request, "main.html", { "object": "Category", 'form': form})

def get_product_list_by_category(request, category_name):
    categories = Category.objects.all()
    product = Product.objects.get_products_by_category(category_name)
    return render(request, "productlist.html", {"iterable": product,"categories": categories, "object": "Products","user":request.user.is_authenticated})


def get_product_details(request, product_id):
     product = Product.objects.get_product_details(product_id)
     return render(request, "product.html", {"iterable": product, "object": "Product details"})
     


@decorators.login_required(login_url='login')
def get_cart(request):
     cart = Cart.objects.filter(user = request.user)
     return render(request, "main.html", {"iterable": cart, "object": "Carts"})

@decorators.login_required(login_url='login')
def get_cart_items(request):
     cart = Cart.objects.filter(user = request.user).first()
     cart = cart.filter(name=name.capitalize())
     
     cartitems = CartItem.objects.filter(cart = cart)
     return render(request, "cart.html", {"iterable": cartitems, "object": "CartItems"})

@decorators.login_required(login_url='login')
def add_cart_items(request):
    if request.method == 'POST':
        form = CartItemForm(request.POST)
        if form.is_valid():
            cart = Cart.objects.filter(user = request.user).first()  
            cart_item = form.save(commit=False)
            cart_item.cart = cart  
            cart_item.save()
            return redirect('cartitems')  # Redirect to a relevant page after adding the item to the cart
    else:
        form = CartItemForm()
    return render(request, "main.html", { "object": "CartItems", 'form': form})
    #  cart = Cart.objects.filter(user = request.user).first()
    #  cartitems = CartItem.objects.filter(cart = cart)
    #  return render(request, "main.html", {"iterable": cartitems, "object": "Carts"})



@decorators.login_required(login_url='login')
def get_user(request):
    if request.user.is_authenticated:
        user = request.user
        return render(request, "main.html", {"user": user, "object": "User"})


def create_seller(request):
     pass

def get_seller_items(request):
     pass

