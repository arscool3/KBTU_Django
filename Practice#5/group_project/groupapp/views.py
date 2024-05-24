from django.shortcuts import render, redirect
from .models import Book, Review
from django.contrib.auth.decorators import login_required

# GET - View all books
def book_list(request):
    books = Book.objects.with_reviews()  # Use custom manager
    return render(request, 'groupapp/book_list.html', {'books': books})

# POST - Create a new book (assuming authenticated user)
@login_required
def create_book(request):
    if request.method == 'POST':
        book_form = BookForm(request.POST)
        if book_form.is_valid():
            book_form.save()
            return redirect('book_list')
    else:
        book_form = BookForm()
    return render(request, 'groupapp/book_form.html', {'book_form': book_form})

# ... other views (GET and POST) for managing authors, reviewers, reviews, etc.
