from django.urls import path
from . import views

urlpatterns = [
    path('authors/', views.author_list, name='author_list'),
    path('books/', views.book_list, name='book_list'),
    path('publishers/', views.publisher_list, name='publisher_list'),
    path('genres/', views.genre_list, name='genre_list'),
]
