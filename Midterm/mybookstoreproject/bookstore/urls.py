from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.user_list, name='user_list'),  
    path('books/', views.book_list, name='book_list'),
    path('books/<int:pk>/', views.book_detail, name='book_detail'),
    path('categories/', views.category_list, name='category_list'),
    path('orders/', views.order_list, name='order_list'),  
    path('reviews/<int:pk>/', views.review_list, name='review_list'), 

    path('users/register/', views.user_create, name='user_create'),
    path('books/create/', views.book_create, name='book_create'),  
    path('categories/create/', views.category_create, name='category_create'),  
    path('orders/create/', views.order_create, name='order_create'),
    path('reviews/create/', views.review_create, name='review_create'), 
]
