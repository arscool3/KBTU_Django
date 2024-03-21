from http.client import HTTPResponse
from django.shortcuts import render, redirect

from .models import *

# Create your views here.

def get_categories(request):
    categories = Category.objects.all()
    return render(request,"index.html", {"categories":categories})

def get_product(request):
    products = Product.objects.all()
    return render(request, "product.html", {"products":products})

def add_product(request):
    if request.method == "POST":
        name = request.POST.get("name")
        price = request.POST.get("price")
        used = request.POST.get("used")
        if used == 'on':
            used = True
        else:
            used = False
        product = Product(name=name, price=price, used=used)
        product.save()
        return redirect("product.html")
    return render("product.html")

def add_category(request):
    if request.method == "POST":
        name = request.post.get("name")
        product = request.post.get("product")
        used = request.post.get("used")
        if used == "on":
            used = True
        else:
            used = True
        productQ = Product.objects
        try:
            prod = Product.objects.get(name = product)
        except:
            return HTTPResponse("NO SUCH PROD")
        category = Category(name = name, product = prod)
        category.save()
        return redirect("index.html")
    return render("index.html")