from django.urls import path

from library.views import *

urlpatterns = [
    path('add_book/', add_book, name='add_book'),
    path('add_author/', add_author, name='add_author'),
    path('add_genre/', add_genre, name='add_genre'),
    path('add_client/', add_client, name='add_client'),

    path('books/', get_books, name='get_books'),
    path('genres/', get_genres, name='get_genres'),
    path('authors/', get_authors, name='get_authors'),
    path('clients/', get_clients, name='get_clients')
]