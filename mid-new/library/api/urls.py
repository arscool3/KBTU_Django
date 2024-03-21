from django.contrib import admin
from django.urls import path
from .views import login_view, check_view, get_books, logout_view, register_view, add_books, get_book, get_genres, \
    get_reviews, add_review, get_publishers

urlpatterns = [
    path('register/', register_view, name='register'), #post 1
    path('login/', login_view, name='login'), #post 2
    path('check/', check_view, name='check'), #post 3
    path('books/', get_books, name='books'), #get 1
    path('logout/', logout_view, name='logout'), #get 2
    path('add_books/', add_books, name='add_books'), #post 4
    path('books/<int:pk>/', get_book, name='get_book'), #get 3
    path('genres/', get_genres, name='get_genres'), #get 4

    path('books/<int:pk>/reviews', get_reviews, name='get_reviews'), #get 5
    path('books/<int:pk>/add_review/', add_review, name='add_review'), #post 5
    path('publishers/', get_publishers, name='get_publishers'), #get 6

]