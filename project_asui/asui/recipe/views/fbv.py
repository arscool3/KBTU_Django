from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from recipe.models import Recipe, Review
from recipe.serializers import ReviewSerializer, RecipeSerializer


@api_view(['GET', 'POST'])
@csrf_exempt
def recipe_rating(request, recipe_id):
    try:
        recipe = Recipe.objects.get(pk=recipe_id)
    except Recipe.DoesNotExist as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        try:
            review = Review.objects.get(recipe=recipe, user=request.user)
        except Review.DoesNotExist as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    if request.method == 'POST':
        if request.user.is_authenticated:
            review = Review(user=request.user, recipe=recipe, rating=request.data)
            serializer = ReviewSerializer(review, data={'user': f'{request.user.id}', 'recipe': f'{recipe.id}', 'rating': int(request.data.get('rating'))})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'user_authenticated': False}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])
@csrf_exempt
def average_rating(request, recipe_id):
    try:
        recipe = Recipe.objects.get(pk=recipe_id)
    except Recipe.DoesNotExist as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        serializer = RecipeSerializer(recipe)
        return Response(serializer.data)