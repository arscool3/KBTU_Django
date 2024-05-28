from urllib import request
from warnings import filters
from django.shortcuts import get_object_or_404, render
from rest_framework import status, viewsets, permissions, filters
from rest_framework.response import Response
from rest_framework.decorators import action
from recipe.tasks import process_review
from recipe.models import Direction, MeasurementQuantity, MeasurementUnit, Recipe, Ingredient, RecipeIngredient, Review
from recipe.serializers import DirectionSerializer, MeasurementQuantitySerializer, MeasurementUnitSerializer, RecipeIngredientSerializer, RecipeSerializer, IngredientSerializer, ReviewSerializer
from users.serializers import BookmarkSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from recipe.permission import IsAuthorOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['cook_time', 'difficulty']    
    ordering_fields = ['cook_time', 'difficulty']

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [permissions.AllowAny()]
        elif self.action in ['create', 'save']:
            return [permissions.IsAuthenticated()]
        elif self.action in ['update', 'partial_update', 'destroy']:
            return [permissions.IsAuthenticated(), IsAuthorOrReadOnly()]
        return super().get_permissions()

    def create(self, request):
        serializer = RecipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        recipe = self.get_object()
        serializer = RecipeSerializer(recipe)
        return Response(serializer.data)    

    def update(self, request, pk=None):
        recipe = self.get_object()
        serializer = RecipeSerializer(recipe, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        recipe = self.get_object()
        recipe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def save(self, request, pk=None):
        recipe = self.get_object()
        serializer = BookmarkSerializer(data={'user': request.user.id, 'recipe': pk})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['get']) 
    def filtered_recipes(self, request): 
        prep_time = request.GET.get('prep_time') 
        difficulty = request.GET.get('difficulty') 
        recipes = self.get_queryset() 
         
        if prep_time: 
            recipes = recipes.filter(prep_time=prep_time) 
        if difficulty: 
            recipes = recipes.filter(difficulty=difficulty) 
         
        page = self.paginate_queryset(recipes) 
        if page is not None: 
            serializer = self.get_serializer(page, many=True) 
            return self.get_paginated_response(serializer.data) 
         
        serializer = self.get_serializer(recipes, many=True) 
        return Response(serializer.data)

class DirectionViewSet(viewsets.ModelViewSet):
    queryset = Direction.objects.all()
    serializer_class = DirectionSerializer
    permission_classes = [IsAuthorOrReadOnly]

class MeasurementUnitViewSet(viewsets.ModelViewSet):
    queryset = MeasurementUnit.objects.all()
    serializer_class = MeasurementUnitSerializer
    

class MeasurementQuantityViewSet(viewsets.ModelViewSet):
    queryset = MeasurementQuantity.objects.all()
    serializer_class = MeasurementQuantitySerializer

class RecipeIngredientViewSet(viewsets.ModelViewSet):
    queryset = RecipeIngredient.objects.all()
    serializer_class = RecipeIngredientSerializer
    permission_classes = [IsAuthorOrReadOnly]


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        review = Review.objects.get(pk=response.data['id'])
        process_review.send(review.id)
        return response
