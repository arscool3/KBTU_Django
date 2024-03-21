from django.urls import path

from app.views import get_films, get_director, get_genres, get_films_by_rating

urlpatterns = [
    path("films/",get_films, name='main'),
    path("directors/",get_director, name='main'),
    path("genres/",get_genres, name='main'),
    path("films/rating",get_films_by_rating, name='main'),

  
]