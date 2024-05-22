from django.contrib import admin
from django.urls import path

from .views import *
from . import views

urlpatterns = [
    path('', homepage, name='homepage'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('add_product/', views.add_product, name='add_product'),
    path('add_brand/', views.add_brand, name='add_brand'),
    path('add_category/', views.add_category, name='add_category'),
    path('get_products/', views.get_products, name='get_products'),
    path('get_brands/', views.get_brands, name='get_brands'),
    path('get_category/', views.get_categories, name='get_categories'),
    
    
]