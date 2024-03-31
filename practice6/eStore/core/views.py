from django.http.response import JsonResponse
import json
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from core.models import Category, Product
# Create your views here.
from core.forms import *
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User
from rest_framework import viewsets

# Create your models here.



class category_list(generics.ListAPIView):
    serializer_class = CategorySerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        return Category.objects.all()


class search(generics.ListAPIView):
    serializer_class = ProductPriceSerializer
    permission_classes = (AllowAny,)
    def get_queryset(self):
        search_query = self.request.GET.get('q','')
        
        return Product.objects.filter(
                Q(name__icontains=search_query) | 
                Q(description__icontains=search_query)
            )
        


class category_details(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    lookup_url_kwarg = 'category_id'
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class product_list_by_category(generics.ListAPIView):
    lookup_url_kwarg = 'category_id'
    serializer_class = ProductPriceSerializer
    permission_classes = (AllowAny,)
    def get_queryset(self):
        category_id = self.kwargs.get('category_id')
        return Product.objects.filter(category_id=category_id)
    

# class product_list(generics.ListCreateAPIView):
#     serializer_class = ProductPriceSerializer
#     permission_classes = (AllowAny,)
#     queryset = Product.objects.all()

class product_details(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductPriceSerializer
    lookup_url_kwarg = 'product_id'
    permission_classes = (IsAuthenticated,)
    def get_queryset(self):
        return Category.objects.all()

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)




class get_cart(generics.ListCreateAPIView):
    serializer_class = CartSerializer
    permission_classes = (IsAuthenticated,)
    def get_queryset(self):
        return Cart.objects.filter(user = self.request.user)



class get_cartItem(generics.ListCreateAPIView):
    serializer_class = CartItemSerializer
    permission_classes = (IsAuthenticated,)
    def get_queryset(self):
        return CartItem.objects.filter(cart__user=self.request.user)
    def perform_update(self, serializer):
        serializer.save(cart=get_cart.as_view())
    
    
class cartItem_details(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CartItemSerializer
    lookup_url_kwarg = 'cartItem_id'
    permission_classes = (IsAuthenticated,)
    def get_queryset(self):
        return CartItem.objects.filter(cart__user = self.request.user)
    
    def perform_update(self, serializer):
        serializer.save(cart__user=self.request.user)
    


class get_User(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    
    permission_classes = (IsAuthenticated,)
    def get_queryset(self):
        return User.objects.filter(username = self.request.user)
    
   

class create_User(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    def perform_create(self, serializer):
        user = serializer.save()
        Cart.objects.create(user=user)

class create_Store(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    def perform_create(self, serializer):
        user = serializer.save()
        Store.objects.create(user = user, store_name =f"{user.username}'s store")


       

class ProductPriceListAPIView(generics.ListAPIView):
    serializer_class = ProductPriceSerializer
    permission_classes = [AllowAny]
    queryset = Product.objects.all()