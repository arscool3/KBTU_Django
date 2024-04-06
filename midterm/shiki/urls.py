from django.urls import path
from .views import *

app_name = "shiki"

urlpatterns = [
    path('anime/', anime_list, name='anime-list'),
    path('anime/<int:pk>/', anime_detail, name='anime-detail'),
    path('anime/create/', anime_create, name='anime-create'),
    path('anime/<int:pk>/update/', anime_update, name='anime-update'),
    path('anime/<int:pk>/delete/', anime_delete, name='anime-delete'),

    path('genre/', genre_list, name='genre-list'),
    path('genre/<int:pk>/', genre_detail, name='genre-detail'),
    path('genre/create/', genre_create, name='genre-create'),
    path('genre/<int:pk>/update/', genre_update, name='genre-update'),
    path('genre/<int:pk>/delete/', genre_delete, name='genre-delete'),

]
