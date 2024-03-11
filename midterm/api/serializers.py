from rest_framework import serializers
from .models import *

from django.contrib.auth.models import User


class TypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Type
        fields = ('type',)



class SortSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sort
        fields = ('sort', )
        read_only_fields =('__all__',)


class CategorySerializer(serializers.ModelSerializer):
    type = TypeSerializer()
    sort = SortSerializer()
    class Meta:
        model = Category
        fields = ('type', 'sort')


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = ('id', 'name', 'category', 'price', 'description')


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user



class UserField(serializers.Field):
    def to_internal_value(self, data):
        return User.objects.get(username=data)

    def to_representation(self, value):
        return value.username


class DateModel(serializers.Field):
    # Fields and definitions here
    def to_internal_value(self, data):
        return Commentary.objects.get(created_at=data)

    def to_representation(self, value):
        return value.strftime("%b %d, %Y %H:%M:%S")


class CommentSerializer(serializers.ModelSerializer):
    user = UserField()

    class Meta:
        model = Commentary
        fields = ('id', 'user', 'text', 'created_at', 'product')
        read_only_fields = ('id', 'created_at', 'product')


class RatingSerializer(serializers.ModelSerializer):
    user = UserField()
    class Meta:
        model = Rating
        fields = ('user', 'rating')
        read_only_fields = ('id', 'product')

class ProductField(serializers.Field):
    def to_internal_value(self, data):
        return Product.objects.get(id=data)

    def to_representation(self, value):
        return ProductSerializer(value).data

class OrderSerializer(serializers.ModelSerializer):
    user = UserField()
    products = ProductField()
    class Meta:
        model = Order
        fields = ('user', 'products')

