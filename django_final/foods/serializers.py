from rest_framework import serializers

from food_categories.models import FoodCategory
from foods.models import Food


class FoodSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=FoodCategory.objects.all())

    class Meta:
        model = Food
        fields = "__all__"
