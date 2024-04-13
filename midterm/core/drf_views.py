from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import *

from django.shortcuts import render,get_object_or_404, HttpResponse, redirect
from django.contrib.auth import authenticate, login, decorators, logout, forms
from django.http import HttpResponseRedirect
from core.models import *
from core.forms import CartForm, ReviewForm , AddProductToOrderForm, AddProductToCartForm
from django.urls import reverse
from django.contrib import messages

@api_view(['GET'])
@login_required(login_url='login')
def get_all_products_drf(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    


@api_view(['POST'])
def add_to_cart(request):
    if request.method == 'POST':
        form = AddProductToCartForm(request.data)
        if form.is_valid():
            product_id = form.cleaned_data['product_id']
            quantity = form.cleaned_data['quantity']

            user = request.user

            cart, _ = Cart.objects.get_or_create(user=user)
            cart.products.add(product_id, through_defaults={'quantity': quantity})

            return Response({'message': 'Product added to cart successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'message': 'Only POST method allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['PUT'])
def make_order(request):
    if request.method == 'PUT':
        order = Order(user=request.user)
        order.save()
        return Response({'order_id': order.pk}, status=status.HTTP_201_CREATED)
    else:
        return Response({'message': 'Only PUT method allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['DELETE'])
def remove_from_cart(request, id):
    try:
        cart = Cart.objects.get(user=request.user)
        cart.products.remove(id)
        return Response({'message': 'Product removed from cart successfully'}, status=status.HTTP_204_NO_CONTENT)
    except Cart.DoesNotExist:
        return Response({'message': 'Cart does not exist'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def cart_detail_drf(request):
    if request.method == 'GET':
        user_cart = Cart.objects.get_or_create(user=request.user)[0]

        cart_products = user_cart.products.all()

        serializer = CartSerializer(user_cart)

        return Response(serializer.data)