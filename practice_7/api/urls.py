from django.urls import path
from . import views

urlpatterns = [
    path('order/create/', views.create_order, name='create-order'),
    path('order/<int:pk>/', views.order_detail, name='order-detail'),
    path('orders/', views.order_list, name='order-list'),
]