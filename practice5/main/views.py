from django.shortcuts import render
from main.models import Author, Book, Client, Library
from main.models import BookQuerySet, LibraryQuerySet
from django.http import HttpResponse
from main.forms import AuthorForm, LibraryForm, ClientForm, BookForm
# Create your views here.


def get_books_by_authors(request):
    name = request.GET.get('name')
    books = BookQuerySet.get_books_by_authors(request, name)
    return render(request, "index.html", {"books": books})

def add_model(request, given_form, given_url, name):
    if request.method == "POST":
        form = given_form(request.POST)
        if(form.is_valid()):
            form.save()
        else:
            raise Exception(form.errors)
        return HttpResponse(f"OK, author was created!")
    return render(request, 'index.html', {'form': given_form(), 'given_url': given_url})

def add_author(request):
    return add_model(request, AuthorForm, 'add_author', 'author')

def add_library(request):
    return add_model(request, LibraryForm, 'add_library', 'library')

def add_book(request):
    return add_model(request, BookForm, 'add_book', 'book')

def add_client(request):
    return add_model(request, ClientForm, 'add_client', 'client')

def get_books(request):
    books = Book.objects.order_books_by_price().all()
    return render(request, 'books.html', {'books': books})

def order_books_by_authors_id(request):
    books = Book.objects.get_books_by_authors_id(request.GET['name'])
    return render(request, 'book_author.html', {'books': books})

def get_library_location(request):
    locations = Library.objects.get_locations(request.GET['city'])
    return render(request, 'library.html', {'libraries': locations})

def get_all_matched_books(request):
    libraries = Library.objects.get_all_matched_books(request.GET['book_name'])
    return render(request, 'library_books.html', {'libraries': libraries})