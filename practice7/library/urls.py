from django.urls import path, include
from rest_framework import routers

from .views import *

router = routers.SimpleRouter()
router.register(r'all_authors', AuthorViewSet)
router.register(r'all_clients', ClientViewSet)
router.register(r'all_books', BookViewSet)
router.register(r'all_libraries', LibraryViewSet)

urlpatterns = [
   path('', include(router.urls)),
   path('author/',add_author, name='add_author'),
   path('book/', add_book, name='add_book'),
   path('library/', add_library, name='add_library'),
   path('client/', add_client, name='add_client'),
   path('books/', get_books, name= 'get_books'),
   path('booksauthor', order_books_by_authors_id, name='get_books_by_authors_id'),
   path('libraries', get_library_location, name='get_library_location'),
   path('librariesbooks', get_all_matched_books, name='get_all_matched_books')
]