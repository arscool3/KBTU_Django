from django.shortcuts import render, redirect
from .models import Author, Book, Publisher, Magazine
from .forms import AuthorForm, BookForm, PublisherForm, MagazineForm

def author_list(request):
    authors = Author.objects.all()
    return render(request, 'author_list.html', {'authors': authors})

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

def publisher_list(request):
    publishers = Publisher.objects.all()
    return render(request, 'publisher_list.html', {'publishers': publishers})

def magazine_list(request):
    magazines = Magazine.objects.all()
    return render(request, 'magazine_list.html', {'magazines': magazines})

def author_create(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('author_list')
    else:
        form = AuthorForm()
    return render(request, 'author_form.html', {'form': form})

def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'book_form.html', {'form': form})

def publisher_create(request):
    if request.method == 'POST':
        form = PublisherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('publisher_list')
    else:
        form = PublisherForm()
    return render(request, 'publisher_form.html', {'form': form})

def magazine_create(request):
    if request.method == 'POST':
        form = MagazineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('magazine_list')
    else:
        form = MagazineForm()
    return render(request, 'magazine_form.html', {'form': form})
