from rest_framework import serializers

from .models import Shop, WarehouseItem


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'


class WarehouseItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = WarehouseItem
        fields = ['id', 'product', 'shop', 'price', 'quantity']
