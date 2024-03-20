from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.get_books),
    path('book/<int:book_id>/', views.get_book_detail, name='book_detail'),
    path('book/create/', views.create_book, name='create_book'),
    path('orders/', views.get_orders, name='order_list'),
    path('order/<int:order_id>/', views.get_order_detail, name='order_detail'),
    path('order/create/', views.create_order, name='create_order'),
]
