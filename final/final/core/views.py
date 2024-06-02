from django.shortcuts import render, redirect
from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets
from final.settings import LOGIN_REDIRECT_URL, LOGIN_URL
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout, get_user_model

from core.models import *
from core.forms import *

@login_required(login_url=LOGIN_URL)
def profile(request):
    his = [val for val in HistoryItem.objects.all() if val in request.user.history.all()]
    return render(request, "profile.html", {'user':request.user,'hist':his})

def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is None:
            return HttpResponse("Invalid credentials.")
        login(request, user)
        return redirect(LOGIN_REDIRECT_URL)
    else:
        form = LoginForm()
        return render(request, 'form.html', {'form':form,'entity':'Log in'})

@login_required(login_url=LOGIN_URL)     
def signout(request):
    logout(request)
    return redirect('/')
            
def signup(request):
    if request.method=="POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        newuser = User.objects.create_user(
            first_name=first_name, 
            last_name=last_name,
            username=username,
            password=password,
            email=email
        )
        try:
            newuser.save()
            newcust = Customer(user=newuser, balance=0.0)
            newcust.save()
            return redirect('/')
        except:
            return HttpResponse("Something went wrong.")
    else:
        form = CustomerForm()
        return render(request, 'form.html', {'form':form,'entity':'Sign up'})

def signup_mfr(request):
    if request.method=="POST":
        username = request.POST['username']
        descr = request.POST['descr']
        password = request.POST['password']
        email = request.POST['email']
        newuser = User.objects.create_user(
            username=username,
            password=password,
            email=email
        )
        try:
            newuser.save()
            newmfr = Manufacturer(user=newuser, descr = descr)
            newmfr.save()
            return redirect('/')
        except:
            return HttpResponse("Something went wrong.")
    else:
        form = ManufacturerForm()
        return render(request, 'form.html', {'form':form,'entity':'Sign up as a Manufacturer'})

def index(request):
    cats = Category.objects.all()
    return render(request, "index.html", {'user':request.user.username,'cats':cats})

def category(request):
    cat = Category.objects.get(id=id)
    products = Product.objects.filter(category=cat)
    return render(request, "category.html", {'cat':cat,'products':products})

def product(request):
    prod = Product.objects.get(id=id)
    return render(request, "product.html", {'prod':prod})

def new_product(request):
    if request.method=="POST":
        mfr = request.POST['username']
        cat = request.POST['descr']
        cost = request.POST['cost']
        count = request.POST['count']
        image = request.POST['image']
        try:
            newprod = Product(manufacturer=mfr, category=cat, cost=cost, count=count, image=image)
            newprod.save()
            return redirect('/')
        except:
            return HttpResponse("Something went wrong.")
    else:
        form = ProductForm()
        return render(request, 'form.html', {'form':form,'entity':'Create a new product'})

def buy_product(request):
    product = Product.objects.get(id=request.POST['product'])
    zahl = request.POST['zahl']
    user = request.user
    if zahl > product.count:
        return HttpResponse("Invalid amount")
    try:
        newhi = HistoryItem(user=user, product=product, count=zahl)
        newhi.save()
        return redirect('/')
    except:
        return HttpResponse("Something went wrong.")