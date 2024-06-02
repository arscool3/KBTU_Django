from django.contrib import admin
from django.urls import path

from core.views import *

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('check/', check_view, name='check'),
    path('movies/', get_movies, name='movies'),
    path("logout/", logout_view, name='logout'),
    path('add_movies/', add_movies, name='add_movies'),
    path('delete_movie/<int:id>', delete_movie, name='delete_movie'),
]