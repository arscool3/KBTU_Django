from django.contrib.auth.models import Group, User
from rest_framework import serializers
from core.models import *

"""
class CustomerUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name']
class ManufacturerUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email']
"""

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class CustomerSerializer(serializers.ModelSerializer):
    #user = CustomerUserSerializer(many=False)
    class Meta:
        model = Customer
        fields = ['user','image','balance']

class ManufacturerSerializer(serializers.ModelSerializer):
    #user = ManufacturerUserSerializer(many=False)
    class Meta:
        model = Manufacturer
        fields = ['user','descr','image']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name','descr']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name','descr','manufacturer','category','cost','count']

class HistoryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoryItem
        fields = ['product','user','count','date']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['product','user','text']


