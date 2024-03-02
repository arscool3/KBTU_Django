# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('stores/', views.store_list, name='store_list'),
    path('categories/', views.category_list, name='category_list'),
    path('manufacturers/', views.manufacturer_list, name='manufacturer_list'),
    path('products/', views.product_list, name='product_list'),
]
