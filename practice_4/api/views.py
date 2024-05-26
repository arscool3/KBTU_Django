from django.shortcuts import render, get_object_or_404, redirect

from .forms import AuthorForm, GenreForm, BookForm
from .models import Book, Author, Genre, Reader
from django.http import JsonResponse

def get_books(request):
    books = Book.objects.all()
    data = [{'title': book.title, 'author': book.author.name, 'genres': [genre.name for genre in book.genres.all()]} for book in books]
    return JsonResponse(data, safe=False)

def get_readers(request):
    readers = Reader.objects.all()
    data = [{'name': reader.name, 'email': reader.email} for reader in readers]
    return JsonResponse(data, safe=False)

def get_books_by_author(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    books = Book.objects.filter(author=author)
    data = [{'title': book.title, 'author': author.name, 'genres': [genre.name for genre in book.genres.all()]} for book in books]
    return JsonResponse(data, safe=False)

def get_books_by_genre(request, genre_id):
    genre = get_object_or_404(Genre, pk=genre_id)
    books = genre.book_set.all()
    data = [{'title': book.title, 'author': book.author.name} for book in books]
    return JsonResponse(data, safe=False)

def get_authors(request):
    authors = Author.objects.all()
    data = [{'name': author.name} for author in authors]
    return JsonResponse(data, safe=False)

def get_genres(request):
    genres = Genre.objects.all()
    data = [{'name': genre.name} for genre in genres]
    return JsonResponse(data, safe=False)

def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_books')
    else:
        form = BookForm()
    return render(request, 'book_form.html', {'form': form})

def create_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_authors')
    else:
        form = AuthorForm()
    return render(request, 'author_form.html', {'form': form})

def create_genre(request):
    if request.method == 'POST':
        form = GenreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_genres')
    else:
        form = GenreForm()
    return render(request, 'genre_form.html', {'form': form})