from django.urls import path
from .views import *


urlpatterns = [

    path('books/', get_books),
    path('authors/', get_authors),
    path('reviews/', get_reviews),
    path('departments/', get_departments),

    path('create-book/', create_book, name='create_book'),
]