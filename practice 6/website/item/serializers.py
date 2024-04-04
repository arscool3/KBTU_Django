from rest_framework import serializers
from .models import Item, ItemReview

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class ItemReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemReview
        fields = '__all__'
