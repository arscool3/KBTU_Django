from django.urls import path
from app.views import get_books,get_magazines,get_authors,get_publishers



urlpatterns = [
    path("books/", get_books,name='books'),
    path("magazines/", get_magazines,name='magazines'),
    path("authors/", get_authors,name='authors'),
    path('publishers/',get_publishers, name='publishers')
]