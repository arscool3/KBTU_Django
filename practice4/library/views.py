from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Genre, Author, Book, Borrower
from .forms import GenreForm, AuthorForm, BookForm, BorrowerForm


def genre_list(request):
    genres = Genre.objects.all()
    context = {'genres': genres}
    return render(request, 'genre_list.html', context)


def genre_detail(request, pk):
    genre = get_object_or_404(Genre, pk=pk)
    context = {'genre': genre}
    return render(request, 'genre_detail.html', context)


def book_list(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'book_list.html', context)


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    context = {'book': book}
    return render(request, 'book_detail.html', context)


def author_list(request):
    authors = Author.objects.all()
    context = {'authors': authors}
    return render(request, 'author_list.html', context)


def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    context = {'author': author}
    return render(request, 'author_detail.html', context)


def borrower_list(request):
    borrowers = Borrower.objects.all()
    context = {'borrowers': borrowers}
    return render(request, 'borrower_list.html', context)


def borrower_detail(request, pk):
    borrower = get_object_or_404(Borrower, pk=pk)
    context = {'borrower': borrower}
    return render(request, 'borrower_detail.html', context)


def add_model(request, given_form, given_url, name):
    if request.method == "POST":
        form = given_form(request.POST)
        if form.is_valid():
            form.save()
        else:
            raise Exception(f"Some Exception {form.errors}")
        return HttpResponse(f'OK, {name} was created')

    return render(request, 'index.html', {'form': given_form(), 'given_url': given_url})


def add_genre(request):
    return add_model(request, GenreForm, 'add_genre', 'genre')


def add_author(request):
    return add_model(request, AuthorForm, 'add_author', 'author')


def add_book(request):
    return add_model(request, BookForm, 'add_book', 'book')


def add_borrower(request):
    return add_model(request, BorrowerForm, 'add_borrower', 'borrower')
