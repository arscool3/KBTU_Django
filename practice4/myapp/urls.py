from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.get_products, name='products'),
    path('orders/', views.get_orders, name='orders'),
    path('create_order/', views.create_order, name='create_order'),
    path('categories/', views.get_categories, name='categories'),

]
