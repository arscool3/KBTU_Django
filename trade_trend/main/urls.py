from django.contrib import admin
from django.urls import path, include
from .views import *
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from main.viewsets import *
router = DefaultRouter()

router.register(r'carts', CartViewSet, basename='cart')
router.register(r'orders', OrderViewSet, basename='order')
router.register(r'notifications', NotificationViewSet, basename='notification')
urlpatterns = [
    path('', get_index, name='main-home'),
    path('categories/', CategoryViewSet.as_view({'get': 'list'}), name='main-categories'),
    path('categories/<str:pk>', ProductViewSet.as_view({'get': 'list'}), name= 'main-products'),
    path('product-list/', product_list, name='product-list'),
    path('products/<int:pk>/', product_detail, name='product-detail'),
    path('product/<int:pk>/review/', create_review, name='review-create'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path("logout/", logout_view, name='logout'),
    path('cart/', cart_view, name='cart'),
    path('remove_from_cart/<int:cart_id>/', remove_from_cart, name='remove_from_cart'),
    path('orders/', orders_view, name='orders'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('create_order/<int:product_id>/', create_order, name='create_order'),
    path('notifications/', notification_list, name='main-notifications')
]