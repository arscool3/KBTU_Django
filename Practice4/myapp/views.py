from django.shortcuts import render, redirect
from .forms import *


def get_authors(request):
    authors = Author.objects.all()
    return render(request, 'authors.html', {'authors': authors})


def get_books(request):
    books = Book.objects.all()
    return render(request, 'books.html', {'books': books})


def get_readers(request):
    readers = Reader.objects.all()
    return render(request, 'readers.html', {'readers': readers})


def get_readingLists(request):
    readingLists = ReadingList.objects.all()
    return render(request, 'readingLists.html', {'readingLists': readingLists})


def create_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save()
            return redirect('authors')  # Redirect to author detail view
    else:
        form = AuthorForm()
    return render(request, 'create_author.html', {'form': form})


def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()
            return redirect('books')  # Redirect to book detail view
    else:
        form = BookForm()
    return render(request, 'create_book.html', {'form': form})


def create_reader(request):
    if request.method == 'POST':
        form = ReaderForm(request.POST)
        if form.is_valid():
            reader = form.save()
            return redirect('readers')  # Redirect to reader detail view
    else:
        form = ReaderForm()
    return render(request, 'create_reader.html', {'form': form})


def create_readingList(request):
    if request.method == 'POST':
        form = ReadingListForm(request.POST)
        if form.is_valid():
            reading_list = form.save()
            return redirect('readingLists')  # Redirect to reading list detail view
    else:
        form = ReadingListForm()
    return render(request, 'create_readingList.html', {'form': form})
