from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, decorators, logout
from django.contrib.auth.forms import AuthenticationForm
from rest_framework import status
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets

from .renderers import UserJSONRenderer
from .serializers import *
from .models import *


class UserRegistrationAPIView(APIView):
    renderer_classes = (UserJSONRenderer,)
    permission_classes = (AllowAny,)
    serializer_class = UserRegistrationSerializer

    def post(self, request):
        user = request.data.get('user', {})
        print(user)

        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        email = serializer.data.get('email')

        send_email.delay(email, 'Welcome!', 'Thank you for registering!')

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserLoginAPIView(APIView):
    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = UserLoginSerializer

    def post(self, request):
        user = request.data.get('user', {})

        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


def get_products(request):
    categories = Category.objects.all()
    products = Product.objects
    form = ProductPriceForm(request.POST)
    if name := request.GET.get('name'):
        products = products.filter(name=name.capitalize())
    products = products.all()
    return render(request, "productlist.html", {"iterable": products,"categories": categories, "object": "Products", 'form': form, "user":request.user.is_authenticated})

class CategoryAPIView(APIView):
    def post(self, request):
        form = CategoryForm(request.POST)
        if form.is_valid():
                form.save()
                return redirect('categories')
        return render(request, "main.html", { "object": "Category", 'form': form})

    def get(self, request):
        categories = Category.objects
        form = CategoryForm()
        if name := request.GET.get('name'):
            categories = categories.filter(name=name.capitalize())
        categories = categories.all()
        return render(request, "categories.html", {"ss": categories, "object": "Categories", 'form': form})


def add_product(request):
    form = ProductPriceForm(request.POST)
    if form.is_valid():
            form.save()
            return redirect('categories')
    return render(request, "main.html", { "object": "Category", 'form': form})

def get_product_list_by_category(request, category_name):
    categories = Category.objects.all()
    product = Product.objects.get_products_by_category(category_name)
    return render(request, "productlist.html", {"iterable": product,"categories": categories, "object": "Products","user":request.user.is_authenticated})


def get_product_details(request, product_id):
     product = Product.objects.get_product_details(product_id)
     return render(request, "product.html", {"iterable": product, "object": "Product details"})