from django.urls import path
from . import views

urlpatterns = [
    path('authors/', views.author_list, name='author_list'),
    path('publishers/', views.publisher_list, name='publisher_list'),
    path('author/create/', views.author_create, name='author_create'),
    path('publisher/create/', views.publisher_create, name='publisher_create'),
]