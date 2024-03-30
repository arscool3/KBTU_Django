import logging

from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from rest_framework.viewsets import ModelViewSet

from .forms import *


from .models import *


# Create your views here.
from .serializers import *


def homepage(request):
    Products = Product.objects.get_all_products()
    return render(request, 'Store/productList.html', {'Products': Products})


def get_pr_by_cat(request, cat_id):
    Products = Product.objects.get_cat_pr(cat_id)
    return render(request, 'Store/productList.html', {'Products': Products})

def busket(request):
    b = BusketItems.objects.get_UserBusket(request.user.pk).get_not_purchased()
    total_cost = 0

    for i in b:
        total_cost += i.product.cost * i.amount


    return render(request, 'Store/busket.html', {'busket' : b, 'total_cost': total_cost})

def purch(request):
    b = BusketItems.objects.get_UserBusket(request.user.pk).get_purchased().order_by('-purch__date')
    return render(request, 'Store/purchases.html', {'busket': b})

def profil(request):
    us = UserInfo.objects.get(user=request.user)

    if request.method == 'POST':
        form1 = UserDescForm(request.POST)
        if form1.is_valid():
            try:
                ui = UserInfo.objects.get(user=request.user)
                ui.desc = form1.instance.desc
                ui.save()
                return redirect('profil')
            except:
                form1.add_error(None, 'Ошибка')
    else:
        form1 = UserDescForm

    if request.method == 'POST':
        u = request.user
        form2 = UserForm(request.POST, instance=u)
        if form2.is_valid():
            try:
                form2.save()
                return redirect('profil')
            except:
                form2.add_error(None, 'Ошибка')
    else:
        initial_data = {
            'username': request.user.username,
            'email': request.user.email,
            'first_name': request.user.first_name,
            'last_name': request.user.last_name
        }

        form2 = UserForm(initial=initial_data)

    if request.method == 'POST':
        ui = request.user.userinfo
        form3 = UserImageForm(request.POST, request.FILES, instance=ui)
        if form3.is_valid():
            try:
                form3.save()
                return redirect('profil')
            except:
                form3.add_error(None, 'Ошибка')
    else:
        form3 = UserImageForm

    return render(request, 'Store/profil.html', {'me': us, 'form1': form1, 'form2': form2, 'form3': form3})

def addAdress(request):
    if request.method == 'POST':
        form = addAdressForm(request.POST)
        if form.is_valid():
            try:
                form.instance.user = request.user
                Adress.objects.get(user=request.user).delete()
                form.save()
                ui = UserInfo.objects.get(user=request.user)
                ui.default_address = Adress.objects.get(user=request.user)
                ui.save()
                return redirect('profil')
            except:
                form.add_error(None, 'Ошибка')
    else:
        form = addAdressForm()
    return render(request, 'Store/addAdress.html', {'form': form})

class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'Store/login.html'

    def get_success_url(self):
        return reverse_lazy('home')



class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'Store/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        UserInfo.objects.just_registrated(user)
        return redirect('home')

def logout_user(request):
    logout(request)
    return redirect('login')



def add_Buscket(request, pr, am):
    previous_page_url = request.META.get('HTTP_REFERER')
    if request.user.is_authenticated:
        BusketItems.objects.addItem(pr, am, request.user)
        return redirect(previous_page_url)

    else: return redirect(previous_page_url)

def del_Buscket(request, id):
    previous_page_url = request.META.get('HTTP_REFERER')
    if request.user.is_authenticated:
        BusketItems.objects.get(pk=id).delete()
        return redirect(previous_page_url)


def buy_Buscket(request):
    previous_page_url = request.META.get('HTTP_REFERER')

    try:
        if request.user.is_authenticated:
            u = request.user
            bis = BusketItems.objects.get_UserBusket(u.pk)
            b = bis.get_not_purchased()
            total_cost = 0

            for i in b:
                total_cost += i.product.cost * i.amount

            prch = Purchase.objects.makePurch(u, u.adress, total_cost)

            for b in bis:
                b.purch = prch
                b.save()

            return redirect(previous_page_url)
    except:
        return redirect('addAdress')


# DRF views

class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

class CatViewSet(ModelViewSet):
    serializer_class = CatSerializer
    queryset = Category.objects.all()


