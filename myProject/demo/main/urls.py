from django.urls import path
from main import views

urlpatterns = [
    path('authors/', views.author_list, name='author_list'),
    path('authors/<int:author_id>', views.author_detail, name='author_detail'),
    path('authors/new/', views.author_new, name='author_new'),

    path('books/', views.book_list, name='book_list'),
]
