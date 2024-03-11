from django.shortcuts import render,  get_object_or_404, redirect
from core.models import Product, Order, Category, Cart
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .serializers import ProductForm, OrderForm, CartForm, PaymentForm, UserProfileForm, CategoryForm

#6 GET Endpoints:
def get_product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})


def get_product_detail(request, product_name):
    product = get_object_or_404(Product, name=product_name)
    return render(request, 'product_detail.html', {'product': product})


@login_required
def get_user_orders(request):
    if request.method == 'GET':
        user = request.user
        orders = Order.objects.filter(user=user)

        serialized_orders = []
        for order in orders:
            serialized_order = {
                'id': order.id,
                'order_number': order.order_number,
                'total_amount': order.total_amount,
            }
            serialized_orders.append(serialized_order)

        response_data = {'orders': serialized_orders}
        return JsonResponse(response_data, safe=False)

    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})


def get_expensive_product_list(request):
    expensive_products = Product.objects.get_expensive_products() 
    return render(request, 'expensive_product_list.html', {'expensive_products': expensive_products})


def category_detail(request, category_name):
    category = get_object_or_404(Category, name=category_name)
    products_in_category = Product.objects.get_products_by_category(category_name)
    return render(request, 'category_details.html', {'category': category, 'products_in_category': products_in_category})


#6 POST Endpoints
def create_product(request):
    form = ProductForm(request.POST)
    if form.is_valid():
        form.save()
    return render(request, 'create_product.html', {'form': form})


def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = OrderForm()
    
    return render(request, 'create_order.html', {'form': form})


def add_to_cart(request, product_id):
    if request.method == 'POST':
        form = CartForm(request.POST)
        if form.is_valid():
             product = get_object_or_404(Product, pk=product_id)
             cart, created = Cart.objects.get_or_create(user=request.user)
             cart.products.add(product)
             cart.total_price += product.price
             cart.save()
    else:
        form = CartForm()
    
    return render(request, 'add_to_cart.html', {'form': form})


def process_payment(request, order_id):
    order = get_object_or_404(Order, pk=order_id)

    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.order = order
            payment.save()
            order.status = 'Paid'
            order.save()
    else:
        form = PaymentForm()
    
    return render(request, 'process_payment.html', {'form': form})


def update_user_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)

        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user
            user_profile.save() 
    else:
        form = UserProfileForm()
    
    return render(request, 'update_user_profile.html', {'form': form})


def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CategoryForm()

    return render(request, 'create_category.html', {'form': form})
