from django.urls import path
from .views import *

urlpatterns = [
    path('', CheckView.index, name='home'),
    path('products/', ProductsView.as_view(), name='products'),
    path('products/<int:id>/', ProductByIdView.as_view(), name='product'),
    path('categories/', CategoriesView.as_view(), name='categories'),
    path('categories/<int:id>', CategoryByIdView.as_view(), name='category'),
    path('categories/<int:id>/products/', ProductsByCategoryView.as_view(), name='productsByCategory'),
    path('topByID', top_ten_products_byId),
    path('topByPrice', top_ten_productsByPrice),
    path('register/', RegisterApi.as_view()),
    path('orders/', OrderListCreateView.as_view(), name='order-list-create'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('order-products/', OrderProductListCreateView.as_view(), name='orderproduct-list-create'),
    path('order-products/<int:pk>/', OrderProductDetailView.as_view(), name='orderproduct-detail'),
]
