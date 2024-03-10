# In urls.py within your 'core' app

from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home, name ='home'),
    path('books/', views.get_all_books, name='books_list'),
    path('authors/', views.get_all_authors, name='authors_list'),
    path('genres/', views.get_all_genres, name='genres_list'),
    path('create_user/', views.create_user, name='create_user'),
    path('create_book/', views.create_book, name='create_book'),
    path('create_author/', views.create_author, name='create_author'),
    path('create_genre/', views.create_genre, name='create_genre'),
    path('create_order/', views.create_order, name='create_order'),
    path('create_review/', views.create_review, name='create_review'),
]
