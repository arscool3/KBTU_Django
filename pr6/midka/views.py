from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action

from .forms import BookForm, AuthorForm, PublisherForm, GenreForm, BorrowBookForm, CustomerForm
from .models import Book, BookInstance, Customer, Person
from .serializers import PersonSerializer

# Create your views here.
def index(request):
    books = Book.objects.all()
    return render(request, 'index.html', {'books': books})


def get_user(request, user_id):
    user = User.objects.get(pk=user_id)
    return render(request, 'index.html', {'users': user})


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


def borrow_book(request, user_id):
    if request.method == 'POST':
        form = BorrowBookForm(request.POST)
        if form.is_valid():
            book_instance_id = form.cleaned_data['book_instance_id']

            user = get_object_or_404(Customer, pk=user_id)
            book_instance = get_object_or_404(BookInstance, id=book_instance_id)

            if book_instance.is_available:
                book_instance.is_available = False
                book_instance.save()
                user.borrowed_books.add(book_instance)
                user.save()
                return HttpResponse(f'successfully borrowed book {book_instance}')
            else:
                raise Exception(f'Exception: {form.errors}')
    else:
        form = BorrowBookForm()
    return render(request, 'borrow.html', {'form': form})


class PersonViewSet(ModelViewSet):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()
    lookup_field = 'id'

    @action(methods=['get'], detail=True)
    def get_genre(self, request):
        return Response('some persons')