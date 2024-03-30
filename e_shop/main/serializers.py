from rest_framework import serializers

from main.models import Product, Shop, Cart, Order, Review

class ProductSerializer(serializers.ModerlSerializer):
    class Meta:
        model = Product
        fields='__all__'

class ShopSerializer(serializers.ModerlSerializer):
    class Meta:
        model = Shop
        fields='__all__'

class CartSerializer(serializers.ModerlSerializer):
    class Meta:
        model = Cart
        fields='__all__'

class OrderSerializer(serializers.ModerlSerializer):
    class Meta:
        model = Order
        fields='__all__'

class ReviewSerializer(serializers.ModerlSerializer):
    class Meta:
        model = Review
        fields='__all__'