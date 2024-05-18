from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import Customer,Manufacturer,Category,Product,HistoryItem,Comment

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ['url','username','email','first_name','last_name']

class ManufacturerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ['url','username','email','descr']

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['url','name','descr']

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['url','name','descr','manufacturer','category','cost','count']

class HistoryItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HistoryItem
        fields = ['url','product','user','count','date']

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ['url','product','user','text']


