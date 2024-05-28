from django.shortcuts import render, redirect
from .models import Author, Book, Publisher, Genre
from .forms import BookForm

def list_of_authors(request):
    authors = Author.objects.all()
    return render(request, 'book_list.html', {'objects': authors, 'object_type': 'Authors'})

def list_of_books(request):
    books = Book.objects.all()
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # Redirect to book list after form submission
    else:
        form = BookForm()
    return render(request, 'book_list.html', {'objects': books, 'form': form, 'object_type': 'Books'})

def list_of_publishers(request):
    publishers = Publisher.objects.all()
    return render(request, 'book_list.html', {'objects': publishers, 'object_type': 'Publishers'})

def list_of_genres(request):
    genres = Genre.objects.all()
    return render(request, 'book_list.html', {'objects': genres, 'object_type': 'Genres'})