from django.http import HttpResponse
from django.shortcuts import render
from forms import *


# Create your views here.
def add_model(request, given_form, given_url, name):
    if request.method == "POST":
        form = given_form(request.POST)
        if form.is_valid():
            form.save()
        else:
            raise Exception(f"Some Exception {form.errors}")
        return HttpResponse(f'OK, {name} was created')

    return render(request, 'create.html', {'form': given_form(), 'given_url': given_url})


def add_author(request):
    add_model(request, AuthorForm, 'add_author', 'author')


def add_book(request):
    add_model(request, BookForm, 'add_book', 'book')


def add_member(request):
    add_model(request, MemberForm, 'add_member', 'member')


def borrow_book(request):
    add_model(request, BorrowForm, 'borrow_book', 'borrow')


def get_users(request):
    authors = Author.objects.all()
    return render(request, 'index_for_authors.html', {'authors': authors})


def get_books(request):
    books = Book.objects.all()
    return render(request, 'index.html', {'books': books})


def get_author(request, author_id):
    author = Author.objects.get(pk=author_id)
    return render(request, 'for_user.html', {'author': author})


def get_book(request, book_id):
    book = Book.objects.get(pk=book_id)
    return render(request, 'for_user.html', {'author': book})



