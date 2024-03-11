
from django.contrib import admin
from django.urls import path, include
from main.views import add_author, add_book, add_client, add_library, get_books, order_books_by_authors_id, get_library_location, get_all_matched_books

urlpatterns = [
   path('author/',add_author, name='add_author'),
   path('book/', add_book, name='add_book'),
   path('library/', add_library, name='add_library'),
   path('client/', add_client, name='add_client'),
   path('books/', get_books, name= 'get_books'),
   path('booksauthor', order_books_by_authors_id, name='get_books_by_authors_id'),
   path('libraries', get_library_location, name='get_library_location'),
   path('librariesbooks', get_all_matched_books, name='get_all_matched_books')
]
