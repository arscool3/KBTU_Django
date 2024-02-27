from django.shortcuts import render
from django.views.generic import ListView
from .models import Book, Author, Genre, Publisher
from .forms import BookForm, AuthorForm, GenreForm, PublisherForm

class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'

def book_create_view(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = BookForm()
    context = {
        'form': form
    }
    return render(request, 'book_create.html', context)

class AuthorListView(ListView):
    model = Author
    template_name = 'author_list.html'

def author_create_view(request):
    form = AuthorForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = AuthorForm()
    context = {
        'form': form
    }
    return render(request, 'author_create.html', context)

class GenreListView(ListView):
    model = Genre
    template_name = 'genre_list.html'

def genre_create_view(request):
    form = GenreForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = GenreForm()
    context = {
        'form': form
    }
    return render(request, 'genre_create.html', context)

class PublisherListView(ListView):
    model = Publisher
    template_name = 'publisher_list.html'

def publisher_create_view(request):
    form = PublisherForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = PublisherForm()
    context = {
        'form': form
    }
    return render(request, 'publisher_create.html', context)