from django.urls import path
from . import views

app_name = 'books'  # Set the app namespace

urlpatterns = [
    path('', views.login_view, name='login'),
    path('home/', views.home, name='home'),
    path('book-list', views.book_list, name='book-list'),
    path('books/<int:pk>/', views.book_detail, name='book-detail'),
    path('register/', views.register_user, name='register'),
    path('create-book/', views.create_book, name='create-book'),
    path('logout/', views.logout_view, name='logout')
]