
from django.shortcuts import render
from django.views.generic import ListView
from .models import Author, Book, Publisher, BookInstance

class AuthorListView(ListView):
    model = Author

class BookListView(ListView):
    model = Book

class PublisherListView(ListView):
    model = Publisher

class BookInstanceListView(ListView):
    model = BookInstance
