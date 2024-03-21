from app.models import Product, Category, Order, User
from django.shortcuts import render, get_list_or_404


def get_product_by_name(request, name):
    product = get_list_or_404(Product, name=name)
    return render(request, 'product_details.html', {'product': product})
    

def get_all_products(request):
    all_products = Product.objects.all()
    return render(request, 'product_list.html', {'products': all_products})
  
    
def get_all_products_by_categoryname(request, category_name):
    all_products_by_category = get_list_or_404(Product, category=category_name)
    return render(request, 'category_product_list.html', {'products:': all_products_by_category})


def get_all_categories(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'products': categories})


def get_orders_by_user(request, username):
    # user_orders = get_list_or_404(Order, username=username)
    user_orders = Order.objects.get_orders_by_user(username=username)
    return render(request, 'user_orders_list.html', {'user_orders': user_orders}) 


def get_customer_by_email(request, email):
    user_email = User.objects.get_customer_by_email(email=email)
    return render(request, {'user': user_email})
    
