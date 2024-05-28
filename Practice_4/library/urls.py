from django.urls import path
from library.views import *

urlpatterns = [
    path('authors/', list_of_authors, name='author_list'),
    path('books/', list_of_books, name='book_list'),
    path('publishers/', list_of_publishers, name='publisher_list'),
    path('genres/', list_of_genres, name='genre_list'),
]