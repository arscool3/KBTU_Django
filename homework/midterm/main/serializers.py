from rest_framework import serializers
from .models import Basket, Product, In_Basket, Order, In_Order

class BasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class InBasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = In_Basket
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class InOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = In_Order
        fields = '__all__'
