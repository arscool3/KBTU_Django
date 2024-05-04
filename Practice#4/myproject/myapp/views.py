from django.shortcuts import render
from .models import Book

def book_list(request):
    books = Book.objects.with_genres()  # Use custom manager
    return render(request, 'myapp/book_list.html', {'books': books})
