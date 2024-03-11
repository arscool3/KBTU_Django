from django.shortcuts import render,get_object_or_404, HttpResponse, redirect
from django.contrib.auth import authenticate, login, decorators, logout, forms
from django.http import HttpResponseRedirect
from core.models import *
from core.forms import CartForm, ReviewForm , AddProductToOrderForm, AddProductToCartForm
from django.urls import reverse
from django.contrib import messages


def basic_form(request, given_form):
    if request.method == 'POST':
        form = given_form(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("OK")
        else:
            raise Exception(f"some erros {form.errors}")
    return render(request, 'index.html', {'form': given_form()})


# def register_view(request):
#     return basic_form(request, forms.UserCreationForm)

def register_view(request):
    if request.method == 'POST':
        form = forms.UserCreationForm(request.POST)
        if form.is_valid():
            form.save()


            return redirect('add_profile_info')
    else:
        form = forms.UserCreationForm()
    
    return render(request, 'register.html', {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponse("You have logout")


def login_view(request):
    if request.method == 'POST':
        form = forms.AuthenticationForm(data=request.POST)
        if form.is_valid():
            try:
                user = authenticate(**form.cleaned_data)
                login(request, user)
                if next := request.GET.get("next"):
                    return redirect(next)
                return HttpResponse("everything is ok")
            except Exception:
                return HttpResponse("something is not ok")
        else:
            raise Exception(f"some erros {form.errors}")
    return render(request, 'index.html', {'form': forms.AuthenticationForm()})


@decorators.login_required(login_url='login')
def check_view(request):
    if request.user.is_authenticated:
        return HttpResponse(f"{request.user} is authenticated")
    raise Exception(f"{request.user} is not authenticated")



@decorators.login_required(login_url='login')
def category_detail_view(request, id):
    # Получаем объект категории или возвращаем 404, если он не существует
    category = get_object_or_404(Category, pk = id)
    # Передаем объект категории в шаблон для отображения
    return render(request, 'category.html', {'category': category})


@decorators.login_required(login_url='login')
def product_detail_view(request, id):
    # Получаем объект продукта или возвращаем 404, если он не существует
    product = get_object_or_404(Product, pk=id)
    # Передаем объект продукта в шаблон для отображения
    return render(request, 'product_detail.html', {'product': product})

@decorators.login_required(login_url='login')
def order_detail_view(request, id):
    # Получаем объект заказа или возвращаем 404, если он не существует
    order = get_object_or_404(Order, pk=id)
    # Передаем объект заказа в шаблон для отображения
    return render(request, 'order_product_detail.html', {'order': order})


@decorators.login_required(login_url='login')
def user_profile_view(request):
    # Получаем профиль пользователя текущего пользователя
    profile = UserProfile.objects.get(user=request.user)
    # Передаем объект профиля пользователя в шаблон для отображения
    return render(request, 'user_profile.html', {'profile': profile})


@decorators.login_required(login_url='login')
def add_product_to_order(request, order_id):
    order = Order.objects.get(id=order_id)
    if request.method == 'POST':
        form = AddProductToOrderForm(request.POST)
        if form.is_valid():
            product_id = form.cleaned_data['product_id']
            quantity = form.cleaned_data['quantity']
            try:
                product = Product.objects.get(id=product_id)
                order_product = OrderProduct(order=order, product=product, quantity=quantity, price=product.price)
                order_product.save()
                messages.success(request, 'Product added to order successfully!')
                return HttpResponseRedirect(reverse('order_detail', kwargs={'id': order_id}))  # Перенаправление на страницу подробностей заказа
            except Product.DoesNotExist:
                messages.error(request, 'Product does not exist!')
    else:
        form = AddProductToOrderForm()
    return render(request, 'add_product_to_order.html', {'form': form})

@decorators.login_required(login_url='login')
def cart_view(request):
    # Получаем объект корзины текущего пользователя
    cart = Cart.objects.get(user=request.user)
    values = cart.products.all()
    values = list(values)
    
    print(values)
    # Передаем объект корзины в шаблон для отображения
    return render(request, 'cart.html', {'cart': values})

@decorators.login_required(login_url='login')
def review_view(request, id):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            product = Product.objects.get(pk=id)
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()
            return redirect('product_detail', pk=id)
    else:
        form = ReviewForm()
    return render(request, 'review.html', {'form': form})

@decorators.permission_required('core.can_add_to_cart', login_url='login')
def add_to_cart_view(request):
    if request.method == 'POST':
        form = AddProductToCartForm(request.POST)
        if form.is_valid():
            # Получение данных из формы
            product_id = form.cleaned_data['product_id']
            quantity = form.cleaned_data['quantity']

            # Получение текущего пользователя
            user = request.user

            # Логика добавления продуктов в корзину
            cart, _ = Cart.objects.get_or_create(user=user)
            cart.products.add(product_id, through_defaults={'quantity': quantity})

            # Перенаправление на страницу корзины
            return redirect('cart')
    else:
        form = AddProductToCartForm()
    return render(request, 'add_to_cart.html', {'form': form})

@decorators.login_required(login_url='login')
def make_order_view(request):
    if request.method == 'POST':
        # Создаем заказ и сохраняем его в базе данных
        order = Order(user=request.user)
        order.save()
        # Дополнительная логика для обработки товаров в заказе
        return HttpResponseRedirect(reverse('order_detail', kwargs={'id': order.pk}))  # Перенаправление на страницу подробностей заказа
    else:
        return render(request, 'order.html')
    

@decorators.login_required(login_url='login')
def get_all_products(request):
    # Получаем все продукты из базы данных
    products = Product.objects.all()
    # Передаем продукты в шаблон для отображения
    return render(request, 'product_list.html', {'products': products})


@decorators.login_required(login_url='login')
def make_reviews(request, product_id, user_id):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            # Сохранение отзыва в базу данных
            product = Product.objects.get(id=product_id)
            user = User.objects.get(id=user_id)
            review = form.save(commit=False)
            review.product = product
            review.user = user
            review.save()
            return HttpResponseRedirect(reverse('product_detail', args=[product_id]))
    else:
        form = ReviewForm()

    return render(request, 'make_review.html', {'form': form})

@decorators.login_required(login_url='login')
def add_profile_info(request):
    if request.method == 'POST':
        shipping_address = request.POST.get('shipping_address')
        # Получаем текущего пользователя
        user = request.user
        # Проверяем, существует ли уже профиль для данного пользователя
        profile, created = UserProfile.objects.get_or_create(user=user)
        # Обновляем информацию о доставке
        profile.shipping_address = shipping_address
        profile.save()
        return render(request, 'profile_updated.html')
    else:
        return render(request, 'add_profile_info.html')
    

@decorators.login_required(login_url='login')
def cart_detail(request):
    user_cart = Cart.objects.get_or_create(user=request.user)[0]
    cart_products = user_cart.products.all()
    context = {
        'user_cart': user_cart,
        'cart_products': cart_products
    }
    return render(request, 'cart_detail.html', context)
