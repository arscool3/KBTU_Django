# noinspection PyUnresolvedReferences
from api.models.book import Book
import json

# noinspection PyUnresolvedReferences
# noinspection PyUnresolvedReferences
from api.models.category import Category
from django.http.response import HttpResponse, JsonResponse
# noinspection PyUnresolvedReferences
from api.serializers.book import BookSerializer2
from rest_framework.views import APIView
import random
# noinspection PyUnresolvedReferences
from rest_framework.response import Response
from rest_framework.decorators import api_view
@api_view(['GET'])
def books(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer2(books,many=True)
        return Response(
            serializer.data
        )
def get_random_books(request):
    total_books = Book.objects.count()
    random_ids = [random.randrange(total_books) for i in range(3)]
    random_books = Book.objects.filter(id__in=random_ids).values()
    return JsonResponse(list(random_books),safe=False)

@api_view(['GET'])
def book_by_id(request, id):
    try:
        book = Book.objects.get(id=id)
    except:
        pass
    if request.method == 'GET':
        serializer = BookSerializer2(book,many=False)
        return Response(serializer.data)
# def delete_books_with_characters():
#     books_to_delete = Book.objects.filter(title__icontains='Ã¶©âÄÐµ½Ð°')
#     books_to_delete.delete()