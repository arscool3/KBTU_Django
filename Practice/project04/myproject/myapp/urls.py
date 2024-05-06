from django.urls import path
from . import views

urlpatterns = [
    path('authors/create/', views.author_create, name='author_create'),
    path('authors/<int:pk>/', views.author_detail, name='author_detail'),
    path('authors/<int:pk>/update/', views.author_update, name='author_update'),
    path('authors/<int:pk>/delete/', views.author_delete, name='author_delete'),
    
    path('books/create/', views.book_create, name='book_create'),
    path('books/<int:pk>/', views.book_detail, name='book_detail'),
    path('books/<int:pk>/update/', views.book_update, name='book_update'),
    path('books/<int:pk>/delete/', views.book_delete, name='book_delete'),

    path('publishers/', views.publisher_list, name='publisher_list'),
    path('publishers/create/', views.publisher_create, name='publisher_create'),
    path('publishers/<int:pk>/', views.publisher_detail, name='publisher_detail'),
    path('publishers/<int:pk>/update/', views.publisher_update, name='publisher_update'),
    path('publishers/<int:pk>/delete/', views.publisher_delete, name='publisher_delete'),

    path('magazines/', views.magazine_list, name='magazine_list'),
    path('magazines/create/', views.magazine_create, name='magazine_create'),
    path('magazines/<int:pk>/', views.magazine_detail, name='magazine_detail'),
    path('magazines/<int:pk>/update/', views.magazine_update, name='magazine_update'),
    path('magazines/<int:pk>/delete/', views.magazine_delete, name='magazine_delete'),

    path('authors/', views.AuthorListCreate.as_view(), name='author-list-create'),
    path('books/', views.BookListCreate.as_view(), name='book-list-create'),
    path('userprofiles/', views.UserProfileListCreate.as_view(), name='userprofile-list-create'),
    path('categories/', views.CategoryListCreate.as_view(), name='category-list-create'),
    path('posts/', views.PostListCreate.as_view(), name='post-list-create'),
    path('comments/', views.CommentListCreate.as_view(), name='comment-list-create'),
]
