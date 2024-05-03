from django.urls import path
from core import views

urlpatterns = [
    path('api/products/', views.get_products, name='get_products'),
    path('api/products/create/', views.create_product, name='create_product'),
    path('api/products/<int:pk>/', views.update_product, name='update_product'),
    path('api/products/<int:pk>/delete/', views.delete_product, name='delete_product'),
]