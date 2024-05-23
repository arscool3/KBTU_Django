from django.urls import path
from .views import home
from .views import BookListView, BookDetailView, AuthorListView, BooksByAuthorView

urlpatterns = [
    path('', home, name='home'),
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('authors/', AuthorListView.as_view(), name='author-list'),
    path('authors/<int:pk>/books/', BooksByAuthorView.as_view(), name='books-by-author'),

]
