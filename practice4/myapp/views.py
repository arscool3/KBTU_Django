from django.shortcuts import render
from myapp.models import Category, Product
from django.shortcuts import render, get_object_or_404

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def product_detail(request, product_name):
    product = get_object_or_404(Product, name=product_name)
    return render(request, 'product_detail.html', {'product': product})

def expensive_product_list(request):
    expensive_products = Product.objects.get_expensive_products() 
    return render(request, 'expensive_product_list.html', {'expensive_products': expensive_products})

def popular_category_list(request):
    popular_categories = Category.objects.get_popular_categories()
    return render(request, 'popular_category_list.html', {'popular_categories': popular_categories})

def category_detail(request, category_name):
    category = get_object_or_404(Category, name=category_name)
    products_in_category = Product.objects.get_products_by_category(category_name)
    return render(request, 'category_details.html', {'category': category, 'products_in_category': products_in_category})