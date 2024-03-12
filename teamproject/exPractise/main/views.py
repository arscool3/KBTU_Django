from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Book, Review

def get_book(request):
    book = get_object_or_404(Book)
    return render(request, 'book_detail.html', {'book': book})

def get_reviews(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    reviews = book.review_set.all()
    return render(request, 'reviews.html', {'book': book, 'reviews': reviews})

