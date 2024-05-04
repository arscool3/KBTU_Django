from django.shortcuts import get_object_or_404, render, redirect
from django.http import JsonResponse, HttpResponse
from .models import Product, Category, Customer, Cart, CartItem, Order
from .forms import ProductForm, CategoryForm, CustomerForm, OrderForm
from django.views.generic import TemplateView
from django.views.generic import View
from django.contrib.auth import authenticate, login, decorators, logout, forms
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

#Products
class CreateProductView(View): 
    # @method_decorator(permission_required('myapp.can_add_product', raise_exception=True))
    def get(self, request):
        # if request.user.has_perm('myapp.can_add_product'):
        form = ProductForm()
        return render(request, 'products/create_product.html', {'form': form})
        # raise Exception(f"{request.user} is not authenticated")

    # @method_decorator(permission_required('myapp.can_add_product', raise_exception=True))
    def post(self, request):
        # if request.user.has_perm('myapp.can_add_product'):
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
        else:
            return render(request, 'products/create_product.html', {'form': form})
        # raise Exception(f"{request.user} is not authenticated")

class ProductDetailView(View):
    # @method_decorator(login_required(login_url='login'))
    def get(self, request, product_id):
        product = get_object_or_404(Product, pk=product_id)
        user = request.user  # Access the logged-in user using request.user
        return render(request, 'products/product_detail.html', {'product': product, 'user': user})

# @decorators.login_required(login_url='login')
# def check_products(request):
#     products = Product.objects.all()
#     return render(request, 'products/product_list.html', {'products': products})


class UpdateProductView(View):
    # @method_decorator(permission_required('myapp.can_change_product', raise_exception=True))
    def get(self, request, product_id):
        product = get_object_or_404(Product, pk=product_id)
        form = ProductForm(instance=product)
        return render(request, 'products/update_product.html', {'form': form, 'product_id': product_id})

    # @method_decorator(permission_required('myapp.can_change_product', raise_exception=True))
    def post(self, request, product_id):
        product = get_object_or_404(Product, pk=product_id)
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_detail', product_id=product_id)
        else:
            return render(request, 'products/update_product.html', {'form': form, 'product_id': product_id})

class ProductListView(View):
    # @method_decorator(login_required(login_url='login'))
    def get(self, request):
        products = Product.objects.all()
        return render(request, 'products/product_list.html', {'products': products})


#Category

class CreateCategoryView(View):
    # @method_decorator(permission_required('myapp.can_add_category', raise_exception=True)) 
    def get(self, request):
        form = CategoryForm()
        return render(request, 'categories/create_category.html', {'form': form})

    # @method_decorator(permission_required('myapp.can_add_category', raise_exception=True)) 
    def post(self, request):
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
        else:
            return render(request, 'categories/create_category.html', {'form': form})

class CategoryDetailView(View):
    # @method_decorator(login_required(login_url='login'))
    def get(self, request, category_id):
        category = get_object_or_404(Category, pk=category_id)
        return render(request, 'categories/category_detail.html', {'category': category})

class UpdateCategoryView(View):
    # @decorators.permission_required('myapp.can_change_category', login_url='login')
    def get(self, request, category_id):
        category = get_object_or_404(Category, pk=category_id)
        form = CategoryForm(instance=category)
        return render(request, 'categories/update_category.html', {'form': form, 'category_id': category_id})

    # @decorators.permission_required('myapp.can_change_category', login_url='login')
    def post(self, request, category_id):
        category = get_object_or_404(Category, pk=category_id)
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_detail', category_id=category_id)
        else:
            return render(request, 'categories/update_category.html', {'form': form, 'category_id': category_id})

class CategoryListView(View):
    @method_decorator(login_required(login_url='login'))
    def get(self, request):
        categories = Category.objects.all()
        return render(request, 'categories/category_list.html', {'categories': categories})
    
#Customer
class CreateCustomerView(View):
    # @decorators.permission_required('myapp.can_add_customer', login_url='login')
    def get(self, request):
        form = CustomerForm()
        return render(request, 'customers/create_customer.html', {'form': form})

    # @decorators.permission_required('myapp.can_add_customer', login_url='login')
    def post(self, request):
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
        else:
            return render(request, 'customers/create_customer.html', {'form': form})

class CustomerDetailView(View):
    # @method_decorator(login_required(login_url='login'))
    def get(self, request, customer_id):
        customer = get_object_or_404(Customer, pk=customer_id)
        return render(request, 'customers/customer_detail.html', {'customer': customer})

class UpdateCustomerView(View):
    # @decorators.permission_required('myapp.can_change_customer', login_url='login')
    def get(self, request, customer_id):
        customer = get_object_or_404(Customer, pk=customer_id)
        form = CustomerForm(instance=customer)
        return render(request, 'customers/update_customer.html', {'form': form, 'customer_id': customer_id})

    # @decorators.permission_required('myapp.can_change_customer', login_url='login')
    def post(self, request, customer_id):
        customer = get_object_or_404(Customer, pk=customer_id)
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_detail', customer_id=customer_id)
        else:
            return render(request, 'customers/update_customer.html', {'form': form, 'customer_id': customer_id})

class CustomerListView(View):
    # @method_decorator(login_required(login_url='login'))
    def get(self, request):
        customers = Customer.objects.all()
        return render(request, 'customers/customer_list.html', {'customers': customers})
    
#Orders

class CreateOrderView(View):
    # @decorators.permission_required('myapp.can_add_order', login_url='login')
    def get(self, request):
        form = OrderForm()
        return render(request, 'orders/create_order.html', {'form': form})

    # @decorators.permission_required('myapp.can_add_order', login_url='login')
    def post(self, request):
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_list')
        else:
            return render(request, 'orders/create_order.html', {'form': form})

class OrderDetailView(View):
    # @method_decorator(login_required(login_url='login'))
    def get(self, request, order_id):
        order = get_object_or_404(Order, pk=order_id)
        return render(request, 'orders/order_detail.html', {'order': order})

class UpdateOrderView(View):
    # @decorators.permission_required('myapp.can_change_order', login_url='login')
    def get(self, request, order_id):
        order = get_object_or_404(Order, pk=order_id)
        form = OrderForm(instance=order)
        return render(request, 'orders/update_order.html', {'form': form, 'order_id': order_id})

    # @decorators.permission_required('myapp.can_change_order', login_url='login')
    def post(self, request, order_id):
        order = get_object_or_404(Order, pk=order_id)
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('order_detail', order_id=order_id)
        else:
            return render(request, 'orders/update_order.html', {'form': form, 'order_id': order_id})

class OrderListView(View):
    # @method_decorator(login_required(login_url='login'))
    def get(self, request):
        orders = Order.objects.all()
        return render(request, 'orders/order_list.html', {'orders': orders})