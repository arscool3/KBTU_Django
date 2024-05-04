from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.book_list, name='book-list'),
    path('books/create/', views.create_book, name='create-book'),
    
    path('authors/', views.author_list, name='author-list'),
    path('authors/create/', views.create_author, name='create-author'),

    path('publishers/create/', views.create_publisher, name='create-publisher'),
    path('publishers/', views.get_publishers, name='get-publisher'),
    
    path('review', views.get_reviews, name='get-review'),
    path('review/create/', views.create_review, name='create-review'),
]
