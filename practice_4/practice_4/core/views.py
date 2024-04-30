from django.shortcuts import render, redirect
from .models import Book, Author, Publisher, Review
from .forms import BookForm


def book_list(request):
    books = Book.objects.all()
    return render(request, 'myapp/book_list.html', {'books': books})

def author_list(request):
    authors = Author.objects.all()
    return render(request, 'myapp/author_list.html', {'authors': authors})

def publisher_list(request):
    publishers = Publisher.objects.all()
    return render(request, 'myapp/publisher_list.html', {'publishers': publishers})

def review_list(request):
    reviews = Review.objects.all()
    return render(request, 'myapp/review_list.html', {'reviews': reviews})


def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'myapp/create_book.html', {'form': form})
