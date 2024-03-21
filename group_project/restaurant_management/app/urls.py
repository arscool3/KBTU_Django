from django.urls import path
from . import views

urlpatterns = [
    # Customer
    path('customers/', views.create_customer, name='create_customer'),
    path('customers/', views.get_customers, name='get_customers'),

    # Menu Item
    path('menu_items/', views.create_menu_item, name='create_menu_item'),
    path('menu_items/', views.get_menu_items, name='get_menu_items'),

    # Order
    path('orders/', views.create_order, name='create_order'),
    path('orders/', views.get_orders, name='get_orders'),

    # Delivery
    path('deliveries/', views.create_delivery, name='create_delivery'),
    path('deliveries/', views.get_deliveries, name='get_deliveries'),
]
