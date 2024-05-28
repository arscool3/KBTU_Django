from rest_framework import serializers
from .models import *


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'name']


class DirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direction
        fields = ['id', 'recipe', 'step', 'content']


class RecipeIngredientSerializer(serializers.ModelSerializer):
    ingredient = IngredientSerializer()

    class Meta:
        model = RecipeIngredient
        fields = ['id', 'recipe', 'ingredient', 'measurement_unit', 'measurement_quantity']


class RecipeSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(read_only=True, many=True)
    recipe_ingredients = RecipeIngredientSerializer(read_only=True, many=True)
    directions = DirectionSerializer(read_only=True, many=True)
    average_rating = serializers.SerializerMethodField()
    reviews = serializers.SerializerMethodField()

    def get_average_rating(self, recipe):
        return recipe.average_rating

    def get_reviews(self, recipe):
        return recipe.num_of_reviews

    class Meta:
        model = Recipe
        fields = ['id', 'title', 'ingredients','recipe_ingredients', 'directions', 'reviews', 'average_rating', 'author', 'difficulty',
                  'prep_time',
                  'cook_time',
                  'servings', 'photo']
        read_only_fields = ['author']


class MeasurementUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeasurementUnit
        fields = ['id', 'unit']


class MeasurementQuantitySerializer(serializers.ModelSerializer):
    class Meta:
        model = MeasurementQuantity
        fields = ['id', 'qty']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'user', 'recipe', 'rating', 'comment']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'user', 'recipe', 'text', 'created_at']
