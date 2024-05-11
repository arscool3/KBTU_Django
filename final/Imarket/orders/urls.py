from django.urls import path

from rest_framework import routers

from .views import OrderViewSet, OrderItemViewSet

urlpatterns = [
    path('users/<int:user_id>/cart_order_items/',
         OrderItemViewSet.as_view(
             {'get': 'get_order_items_in_cart'}), name='get products in cart'),
    path('users/<int:user_id>/orders/',
         OrderItemViewSet.as_view(
             {'get': 'get_user_orders'}), name='get orders'),
    path('orders/<int:order_id>/orderitems/',
         OrderItemViewSet.as_view(
             {'get': 'get_user_order_orderitems'}), name='get orderitems in exact order'),
    path('users/<int:user_id>/purchase_cart/',
         OrderViewSet.as_view(
             {'put': 'purchase_orderitems_in_order'}), name='purchase cart'),
    path('orderitems/<int:orderitem_id>/',
         OrderItemViewSet.as_view(
             {'delete': 'delete_order_item_from_order'}), name='delete order item'),
    path('users/<int:user_id>/add_item_to_cart/',
         OrderItemViewSet.as_view(
             {'post': 'add_order_item_to_order'}), name='add order item'),
]

r = routers.DefaultRouter()

r.register(r'orders', OrderViewSet)
r.register(r'order_items', OrderItemViewSet)

urlpatterns += r.urls
