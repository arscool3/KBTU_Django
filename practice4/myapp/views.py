from django.shortcuts import render, redirect
from .models import Category, Product, Order, OrderItem
from .forms import OrderForm


def get_products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})


def get_orders(request):
    orders = Order.objects.all()
    return render(request, 'orders.html', {'orders': orders})


def get_categories(request):
    categories = Category.objects.all()
    return render(request, 'categories.html', {'categories': categories})


def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            # Retrieve product IDs from the form data
            product_ids = request.POST.getlist('products')
            for product_id in product_ids:
                product = Product.objects.get(pk=product_id)
                OrderItem.objects.create(order=order, product=product, quantity=1)
            return redirect('orders')
    else:
        form = OrderForm()
    return render(request, 'create_order.html', {'form': form})
