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
from final.celery import send_email


class UserRegistrationAPIView(APIView):
    renderer_classes = (UserJSONRenderer,)
    permission_classes = (AllowAny,)
    serializer_class = UserRegistrationSerializer

    def post(self, request):
        user = request.data

        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        email = serializer.data.get('email')

        send_email(email, 'Welcome!', 'Thank you for registering!')

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserLoginAPIView(APIView):
    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = UserLoginSerializer

    def post(self, request):
        user = request.data

        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data = request.data)
        serializer.seller = request.user
        if serializer.is_valid():
            serializer.save()
            return Response({"success": "true", "data": {"product": serializer.data}}, status=status.HTTP_201_CREATED)
        else:
            return Response({"success": "false", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        search_param = request.GET.get("search")
        products = self.get_queryset()

        if search_param:
            products = products.filter(name__icontains=search_param)

        serializer = self.serializer_class(products, many=True)
        return Response({
            "success": "true",
            "products": serializer.data
        }, status=status.HTTP_200_OK)


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Product.objects.all()
    serializer_class = CategorySerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": "true", "data": {"category": serializer.data}}, status=status.HTTP_201_CREATED)
        else:
            return Response({"success": "false", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        search_param = request.GET.get("search")
        products = self.get_queryset()

        if search_param:
            products = products.filter(name__icontains=search_param)

        serializer = self.serializer_class(products, many=True)
        return Response({
            "success": "true",
            "category": serializer.data
        }, status=status.HTTP_200_OK)


class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data = request.data)
        serializer.author = request.user
        if serializer.is_valid():
            serializer.save()
            return Response({"success": "true", "data": {"comment": serializer.data}}, status=status.HTTP_201_CREATED)
        else:
            return Response({"success": "false", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        search_param = request.GET.get("search")
        comments = self.get_queryset()

        if search_param:
            comments = comments.filter(content__icontains=search_param)

        serializer = self.serializer_class(comments, many=True)
        return Response({
            "success": "true",
            "comments": serializer.data
        }, status=status.HTTP_200_OK)


class LikeViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data = request.data)
        serializer.user = request.user
        if serializer.is_valid():
            serializer.save()
            return Response({"success": "true", "data": {"like": serializer.data}}, status=status.HTTP_201_CREATED)
        else:
            return Response({"success": "false", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        search_param = request.GET.get("search")
        likes = self.get_queryset()

        if search_param:
            likes = comments.filter(content__icontains=search_param)

        serializer = self.serializer_class(likes, many=True)
        return Response({
            "success": "true",
            "likes": serializer.data
        }, status=status.HTTP_200_OK)


def get_products(request):
    categories = Category.objects.all()
    products = Product.objects
    form = ProductPriceForm(request.POST)
    if name := request.GET.get('name'):
        products = products.filter(name=name.capitalize())
    products = products.all()
    return render(request, "productlist.html", {"iterable": products,"categories": categories, "object": "Products", 'form': form, "user":request.user.is_authenticated})


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