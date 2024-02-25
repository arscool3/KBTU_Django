from django.urls import path
from . import views

urlpatterns = [
    path('authors/', views.author_list, name='author_list'),
    path('books/', views.book_list, name='book_list'),
    path('publishers/', views.publisher_list, name='publisher_list'),
    path('magazines/', views.magazine_list, name='magazine_list'),
    path('author/create/', views.author_create, name='author_create'),
    path('book/create/', views.book_create, name='book_create'),
    path('publisher/create/', views.publisher_create, name='publisher_create'),
    path('magazine/create/', views.magazine_create, name='magazine_create'),
]