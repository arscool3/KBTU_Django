from core.models import *
from rest_framework import serializers 


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id','name','photoUrl')

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'

class StoreItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreItem
        fields = '__all__'
        

class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields = ('id','username', 'email', 'password')

class CartSerializer(serializers.ModelSerializer):
    user_info = UserSerializer(source= 'user', read_only = True)
    class Meta:
        model = Cart
        fields = ('id', 'user_info')

class ProductPriceSerializer(serializers.ModelSerializer):
    store_items = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'category', 'photoUrl', 'store_items']

    def get_store_items(self, product):
        store_items = StoreItem.objects.filter(product=product).order_by('price')
        return [{'store': item.store.store_name, 'price': item.price} for item in store_items]


class CartItemSerializer(serializers.ModelSerializer):
    products = ProductPriceSerializer(source='product', read_only=True)
    carts = CartSerializer(source = 'cart', read_only = True)
    class Meta:
        model = CartItem
        fields = '__all__'