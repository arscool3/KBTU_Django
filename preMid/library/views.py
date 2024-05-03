from django.shortcuts import render
from django.http import HttpResponse

from library.forms import *
from library.models import Book, Client


# Create your views here.
def get_books(request):
    books = Book.objects.all()
    return render(request, 'books.html', context={'books': books})

def get_clients(request):
    clients = Client.objects.all()
    return render(request, 'clients.html', context={'clients':clients})

def get_genres(request):
    genres = Genre.objects.all()
    return render(request, 'genres.html', context={'genres':genres})

def get_authors(request):
    authors = Author.objects.all()
    return render(request, 'authors.html', context={'authors':authors})


def add_model(request, given_form, given_url, name):
    if request.method == "POST":
        form = given_form(request.POST)
        if form.is_valid():
            form.save()
        else:
            raise Exception(f"Some Exception {form.errors}")
        return HttpResponse(f'OK, {name} was created')

    return render(request, 'index.html', {'form': given_form(), 'given_url': given_url})


def add_book(request):
    return add_model(request, BookForm, 'add_book', 'book')

def add_author(request):
    return add_model(request, AuthorForm, 'add_author', 'author')

def add_genre(request):
    return add_model(request, GenreForm, 'add_genre', 'genre')

def add_client(request):
    return add_model(request, ClientForm, 'add_client', 'client')