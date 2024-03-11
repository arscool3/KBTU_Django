# urls.py
from django.urls import path
from .views import AuthorListView, BookListView, PublisherListView, BookInstanceListView

urlpatterns = [
    path('authors/', AuthorListView.as_view(), name='author_list'),
    path('books/', BookListView.as_view(), name='book_list'),
    path('publishers/', PublisherListView.as_view(), name='publisher_list'),
    path('bookinstances/', BookInstanceListView.as_view(), name='bookinstance_list'),
]
