from django.urls import path
from .views import *

urlpatterns = [
    path('authors/', get_authors, name='authors'),
    path('books/', get_books, name='books'),
    path('readers/', get_readers, name='readers'),
    path('readingList/', get_readingLists, name='readingLists'),
    path('create_author/', create_author, name='create_author'),
    path('create_book/', create_book, name='create_book'),
    path('create_reader/', create_reader, name='create_reader'),
    path('create_readingList/', create_readingList, name='create_readingList'),
]