from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from library.forms import BookForm, AuthorForm, PublisherForm, GenreForm, CustomerForm, BookInstanceForm
from library.models import Book, BookInstance, Customer, Author


# Create your views here.
def index(request):
    books = Book.objects.all()
    return render(request, 'books.html', {"iterable": books, "object": "Books"})


def get_users(request):
    users = Customer.objects.all()
    return render(request, 'users.html', {"iterable": users, "object": "Users"})


def get_user(request, user_id):
    user = Customer.objects.get(pk=user_id)
    return render(request, 'user.html', {"user": user, "object": "User"})


def get_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'book.html', {"book": book, "object": "Book"})


def get_author(request):
    authors = Author.objects.all()
    return render(request, 'users.html', {"iterable": authors, "object": "Author"})


def add_model(request, given_form, given_url, name):
    if request.method == "POST":
        form = given_form(request.POST)
        if form.is_valid():
            form.save()
        else:
            raise Exception(f"Some Exception {form.errors}")
        return HttpResponse(f'OK, {name} was created')

    return render(request, 'create.html', {'form': given_form(), 'given_url': given_url})


def add_book(request):
    return add_model(request, BookForm, 'add_book', 'book')


def add_author(request):
    return add_model(request, AuthorForm, 'add_author', 'author')


def add_publisher(request):
    return add_model(request, PublisherForm, 'add_publisher', 'publisher')


def add_genre(request):
    return add_model(request, GenreForm, 'add_genre', 'genre')


def add_customer(request):
    return add_model(request, CustomerForm, 'add_customer', 'customer')


def add_instance(request):
    return add_model(request, BookInstanceForm, 'add_instance', 'instance')


