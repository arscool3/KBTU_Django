from django.shortcuts import render
from django.http import HttpResponse

from Library.forms import *
from Library.models import Book, Client

from rest_framework.generics import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from Library.serializers import *

# Create your views here.
def get_books(request):
    # books = Book.objects.all()
    books = Book.objects.available_books()
    return render(request, 'books.html', context={'books': books})

def get_books_by_genre(request, genre__id):
    books = Book.objects.books_by_genre(genre__id)
    return render(request, 'books.html', context={'books': books})
def get_book_by_id(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'book_detail.html', context={'book': book})

def get_clients(request):
    clients = Client.objects.all()
    return render(request, 'clients.html', context={'clients':clients})

def get_genres(request):
    genres = Genre.objects.all()
    return render(request, 'genres.html', context={'genres':genres})

def get_authors(request):
    authors = Author.objects.all()
    return render(request, 'authors.html', context={'authors':authors})

def get_loans(request):
    loans = Loan.objects.all()
    return render(request, 'loans.html', context={'loans':loans})

def get_publishing_office(request):
    publishing_office = PublishingOffice.objects.all()
    return render(request, '')

def delete_loan(request, client_id, book_id):
    client = Client.objects.get(id=client_id)
    book = Book.objects.get(id=book_id)
    loan = Loan.objects.filter(client=client, book=book)
    context = {'loan':loan}
    loan.delete()
    return render(request, 'delete_loan.html', context={'loan':context['loan']})


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

def add_loan(request):
    return add_model(request, LoanForm, 'add_loan', 'loan')

def add_publishing_office(request):
    return add_model(request, PublishingOfficeForm, 'add_publishing_office', 'publishing_office')


class BookViewSet(ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    @action(detail=True, methods=['get'])
    def availability(self, request, pk=None):
        book = self.get_object()
        if book.available:
            return Response({'available': True})
        else:
            return Response({'available': False})