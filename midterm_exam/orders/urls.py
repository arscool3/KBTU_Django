from django.urls import path
from .views import UserOrderListView, OrderDetailView

urlpatterns = [
    path('orders/', UserOrderListView.as_view(), name='user-orders'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
]
