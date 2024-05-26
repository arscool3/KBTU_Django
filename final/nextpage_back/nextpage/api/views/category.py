from django.http import JsonResponse
from django.shortcuts import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
# noinspection PyUnresolvedReferences
from api.serializers.category import CategorySerializer2
# noinspection PyUnresolvedReferences
from api.serializers.book import BookSerializer2
# noinspection PyUnresolvedReferences
from api.models.category import Category
# noinspection PyUnresolvedReferences
from api.serializers.category import CategorySerializer2
# noinspection PyUnresolvedReferences
from api.serializers.book import BookSerializer2
# noinspection PyUnresolvedReferences
from api.models.category import Category
# noinspection PyUnresolvedReferences
from api.models.book import Book



class CategoryListAPIView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer2(categories, many=True)
        return Response(serializer.data)
    # def delete(self, request):
    #     book_categories = Book.objects.values_list('category__id', flat=True).distinct()
    #     empty_categories = Category.objects.exclude(id__in=book_categories)
    #     empty_categories.delete()
    #     return Response({'deleted': True})

class CategoryDetailAPIView(APIView):
    def get_object(self, category):
        try:
            return Category.objects.get(pk=category)
        except Category.DoesNotExist as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, category_id):
        instance = self.get_object(category_id)
        serializer = CategorySerializer2(instance)
        try:
            return Response(serializer.data)
        except Category.DoesNotExist as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

class BooksByCategoryAPIView(APIView):
    def get(self, request, category_id):
        books = Book.objects.filter(category=category_id)
        serializer = BookSerializer2(books, many=True)
        return Response(serializer.data)
        