

from django.urls import path
from . import views, templatetags

urlpatterns = [
    path('home/',views.home, name ='home'),
    path('books/', views.get_all_books, name='books_list'),
    path('authors/', views.get_all_authors, name='authors_list'),
    path('genres/', views.get_all_genres, name='genres_list'),
    #path('books_by_genre/',templatetags.get_books_by_genre, name='books_by_genre'),
    #path('books_by_genre/<int:genre_id>/', views.books_by_genre, name='books_by_genre'),
    # path('books-by-genre/<int:genre_id>/', views.books_by_genre, name='books_by_genre'),
    path('books-by-genre/<int:genre_id>/', views.books_by_genre, name='books_by_genre'),
    path('books-by-author/<int:author_id>/', views.books_by_author, name='books_by_author'),
    path('create_user/', views.create_user, name='create_user'),
    path('create_book/', views.create_book, name='create_book'),
    path('create_author/', views.create_author, name='create_author'),
    path('create_genre/', views.create_genre, name='create_genre'),
    path('create_order/', views.create_order, name='create_order'),
    path('create_review/', views.create_review, name='create_review'),
]
