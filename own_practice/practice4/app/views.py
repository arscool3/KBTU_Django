from django.shortcuts import render, redirect
from .models import Author, Book, Publisher, Genre
from .managers import AuthorManager, BookManager
from .forms import BookForm

def author_list(request):
    authors = Author.objects.all()
    return render(request, 'index.html', {'objects': authors, 'object_type': 'Authors'})

def book_list(request):
    books = Book.objects.all()
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # Redirect to book list after form submission
    else:
        form = BookForm()
    return render(request, 'index.html', {'objects': books, 'form': form, 'object_type': 'Books'})

def publisher_list(request):
    publishers = Publisher.objects.all()
    return render(request, 'index.html', {'objects': publishers, 'object_type': 'Publishers'})

def genre_list(request):
    genres = Genre.objects.all()
    return render(request, 'index.html', {'objects': genres, 'object_type': 'Genres'})
