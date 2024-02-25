# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.category_list, name='category_list'),
    path('products/', views.product_list, name='product_list'),
    path('expensive-products/', views.expensive_product_list, name='expensive_product_list'),
    path('products/<str:product_name>/', views.product_detail, name='product_detail'),
    path('popular-categories/', views.popular_category_list, name='popular_category_list'),
    path('categories/<str:category_name>/', views.category_detail, name='category_detail'),
]
