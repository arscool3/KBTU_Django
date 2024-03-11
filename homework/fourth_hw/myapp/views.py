from django.shortcuts import render
from .models import *
from .forms import *
# Create your views here.
def authors(request):
    authors = Author.objects.all()
    return render(request, 'authors.html', {'authors': authors})

def books(request):
    books = Book.objects.all()
    return render(request, 'books.html', {'books': books})

def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = BookForm()
    return render(request, 'book_create.html', {'form': form})