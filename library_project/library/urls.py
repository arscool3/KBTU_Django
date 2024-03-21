from django.urls import path
from .views import views

urlpatterns = [
    path('books/', views.book_list, name='book_list'),
    path('books/<int:book_id>/', views.book_detail, name='book_detail'),
    path('books/borrow/<int:book_id>/', views.borrow_book, name='borrow_book'),
    path('books/return/<int:book_id>/', views.return_book, name='return_book'),
    path('profile/', views.user_profile, name='user_profile'),
    path('profile/update/', views.update_profile, name='update_profile'),
]