from django.urls import path
from . import views

urlpatterns = [
    path("authors/", views.authors, name='authors'),
    path("publishers/", views.publishers, name='publishers'),
    path("create-book/", views.create_book, name='create_book'),
]
