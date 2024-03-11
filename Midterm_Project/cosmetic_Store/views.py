from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login,  forms
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *


# 6 Post requests

def homepage(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = forms.CustomerCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login in')
        else:
            return render(request, 'register.html', {'form': form, 'error_message': 'Invalid credentials'})
    return render(request, 'index.html', {'form': forms.CustomerCreationForm()})
   
def login(request):
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
            else:
                return render(request, 'login.html', {'form': form, 'error_message': 'Invalid credentials'})
    return render(request, 'index.html', {'form': LoginForm()})

def add_product(request):
    if request.method == 'POST':
        serializer = ProductSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    

def add_brand(request):
    if request.method == 'POST':
        serializer = BrandSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
        
def add_category(request):
    if request.method == 'POST':
        serializer = GenreSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    


# 6 Get requests
        
@api_view(['GET'])
def get_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(brands, many=True)
    return JsonResponse(serializer.data, safe=False)
    
@api_view(['GET'])
def get_brands(request):
    brands = Brand.objects.all()
    serializer = BrandSerializer(brands, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def get_categories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def get_customer(request):
    customer = Customer.objects.get()
    serializer = CustomerSerializer(customer)
    return JsonResponse(serializer.data)

@api_view(['GET'])
def get_favorite(request):
    favorite = Favorite.objects.get()
    serializer = FavoriteSerializer(favorite)
    return JsonResponse(serializer.data)

@api_view(['GET'])
def get_cartInformation(request):
    customer = Customer.objects.get()
    serializer = CustomerSerializer(customer)
    return JsonResponse(serializer.data)
