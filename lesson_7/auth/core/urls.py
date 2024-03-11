from django.contrib import admin
from django.urls import path

from core.views import login_view, check_view, get_movies, logout_view, register_view, add_movies

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('check/', check_view, name='check'),
    path('movies/', get_movies, name='movies'),
    path("logout/", logout_view, name='logout'),
    path('add_movies/', add_movies, name='add_movies'),
]