from django.contrib import admin
from django.urls import path, include
from .views import *
from rest_framework import routers
from main.viewsets import ProductViewSet, CategoryViewSet
urlpatterns = [
    path('', get_index, name='main-home'),
    path('categories/', CategoryViewSet.as_view({'get': 'list'}), name='main-categories'),
    path('products/', ProductViewSet.as_view({'get': 'list'}), name= 'main-products'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path("logout/", logout_view, name='logout'),
]