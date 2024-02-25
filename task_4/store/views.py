from django.shortcuts import render , redirect

from django.views.generic import ListView
from .models import Category, Product , Cart , CartItem
from .forms import ProductForm , CategoryForm , AddToCartForm

class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'

    def get_queryset(self):
        return Product.objects.all()

def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product-list')
    else:
        form = ProductForm()
    return render(request, 'store/product_form.html', {'form': form})

def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category-list')
    else:
        form = CategoryForm()
    return render(request, 'store/create_category.html', {'form': form})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'store/category_list.html', {'categories': categories})

def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        form = AddToCartForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            cart, created = Cart.objects.get_or_create()
            cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
            cart_item.quantity += quantity
            cart_item.save()
            return redirect('view_cart')
    else:
        form = AddToCartForm()
    return render(request, 'store/product_form.html', {'form': form, 'product': product})

def delete_from_cart(request, cart_item_id):
    cart_item = CartItem.objects.get(id=cart_item_id)
    if request.method == 'POST':
        cart_item.delete()
        return redirect('product-list')
    return render(request, 'store/product_form.html', {'cart_item': cart_item})

def view_cart(request):
    cart = Cart.objects.first()  
    cart_items = CartItem.objects.filter(cart=cart)
    products = [item.product for item in cart_items] 
    return render(request, 'store/view_cart.html', {'cart_items': cart_items, 'products': products})
