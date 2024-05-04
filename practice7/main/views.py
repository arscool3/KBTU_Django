from dramatiq.results import ResultMissing
from rest_framework.generics import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django.shortcuts import render
from .models import Author, Book, Client, Library
from .models import BookQuerySet, LibraryQuerySet
from django.http import HttpResponse
from .forms import AuthorForm, LibraryForm, ClientForm, BookForm
from .serializers import *
from tasks import check_book_task, result_backend


# Create your views here.
class AuthorViewSet(ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class BookViewSet(ModelViewSet):
    serializer_class = BookSerializer
    queryset = Author.objects.all()


class LibraryViewSet(ModelViewSet):
    serializer_class = LibrarySerializer
    queryset = Author.objects.all()


class ClientViewSet(ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Author.objects.all()


def get_books_by_authors(request):
    name = request.GET.get('name')
    books = BookQuerySet.get_books_by_authors(request, name)
    return render(request, "index.html", {"books": books})


def add_model(request, given_form, given_url, name):
    if request.method == "POST":
        form = given_form(request.POST)
        if (form.is_valid()):
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


def start_check_books_in_stock(request):
    task = check_book_task(request.GET['id' or 'book_id'])
    return {'task_id': task.message_id}


def get_check_books_in_stock(request):
    try:
        status = result_backend.get_result(check_book_task.message().copy(message_id=request.GET['id' or 'task_id']))
    except ResultMissing:
        return {"status": "pending"}
    return {'status': status}
