from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.decorators import method_decorator
from django.views import View

from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm

from .models import *


class HomeView(View):
    def get(self, request):
        products = Product.objects.all()

        context = {'products': products}
        return render(request, 'home.html', context)


class ProductDetailView(View):
    def get(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)

        context = {'product': product}
        return render(request, 'product_detail.html', context)

    def post(self, request, product_id):
        product = get_object_or_404(Product, pk=product_id)
        user_cart, created = Cart.objects.get_or_create(user=request.user)

        cart_item, created = CartItem.objects.get_or_create(cart=user_cart, product=product)

        cart_item.quantity += 1
        cart_item.save()

        return JsonResponse({'message': 'Product added to cart successfully'})


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class UserProfileView(View):
    def get(self, request):
        user_profile, created = UserProfile.objects.get_or_create(user=request.user)

        context = {'user_profile': user_profile}
        return render(request, 'user_profile.html', context)


class CategoryView(View):
    def get(self, request):
        categories = Category.objects.all()
        context = {
            'categories': categories,
        }

        return render(request, 'category.html', context)


@method_decorator(login_required(login_url='/accounts/login/'), name='dispatch')
class CartView(View):
    def get(self, request):
        user_cart, created = Cart.objects.get_or_create(user=request.user)
        cart_items = user_cart.cartitem_set.all()

        context = {
            'cart': user_cart,
            'cart_items': cart_items,
        }

        return render(request, 'cart.html', context)

    def post(self, request):
        action = request.POST.get('action')

        if action == 'remove':
            return self.remove_from_cart(request)
        elif action == 'clear':
            return self.clear_cart(request)
        elif action == 'create_order':
            return self.create_order(request)
        else:
            return JsonResponse({'message': 'Invalid action'})

    def remove_from_cart(self, request):
        product_id = request.POST.get('product_id')
        user_cart, created = Cart.objects.get_or_create(user=request.user)

        try:
            cart_item = CartItem.objects.get(cart=user_cart, product_id=product_id)
            cart_item.delete()
            message = 'Product removed from cart successfully'
        except CartItem.DoesNotExist:
            message = 'Product not found in cart'

        return JsonResponse({'message': message})

    def clear_cart(self, request):
        user_cart, created = Cart.objects.get_or_create(user=request.user)

        user_cart.cartitem_set.all().delete()

        return JsonResponse({'message': 'Cart cleared successfully'})

    def create_order(self, request):
        user_cart, created = Cart.objects.get_or_create(user=request.user)

        total_price = user_cart.calculate_total_price()

        order = Order.objects.create(user=request.user, total_price=total_price)

        cart_items = user_cart.cartitem_set.all()
        for cart_item in cart_items:
            order_item = OrderItem.objects.create(order=order, product=cart_item.product, quantity=cart_item.quantity)

        user_cart.cartitem_set.all().delete()

        return JsonResponse({'message': 'Order created successfully'})


class CustomLoginView(LoginView):
    template_name = 'login.html'


class CustomLogoutView(LogoutView):
    def get_next_page(self):
        return redirect('home')


class CustomSignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


@method_decorator(login_required(login_url='/accounts/login/'), name='dispatch')
class OrderView(View):
    def get(self, request):
        user_orders = Order.objects.filter(user=request.user)
        order_items = OrderItem.objects.filter(order__user=request.user)

        context = {
            'user_orders': user_orders,
            'order_items': order_items,
        }

        return render(request, 'order.html', context)
