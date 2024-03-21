"""
URL configuration for lab4 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin


from django.urls import path
from bookstore.views import (
    BookListView, book_create_view,
    AuthorListView, author_create_view,
    GenreListView, genre_create_view,
    PublisherListView, publisher_create_view,
)

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/create/', book_create_view, name='book-create'),
    path('authors/', AuthorListView.as_view(), name='author-list'),
    path('authors/create/', author_create_view, name='author-create'),
    path('genres/', GenreListView.as_view(), name='genre-list'),
    path('genres/create/', genre_create_view, name='genre-create'),
    path('publishers/', PublisherListView.as_view(), name='publisher-list'),
    path('publishers/create/', publisher_create_view, name='publisher-create'),
]
