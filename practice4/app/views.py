# views.py

from django.shortcuts import render, redirect
from .forms import AuthorForm, BookForm, PublisherForm, MagazineForm
from .models import Author, Book, Publisher, Magazine

def get_books(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = BookForm()
    return render(request, 'populate_forms.html', {'object': 'Add Book', 'form': form})

def get_magazines(request):
    if request.method == 'POST':
        form = MagazineForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = MagazineForm()
    return render(request, 'populate_forms.html', {'object': 'Add Magazine', 'form': form})

def get_authors(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AuthorForm()
    return render(request, 'populate_forms.html', {'object': 'Add Author', 'form': form})

def get_publishers(request):
    if request.method == 'POST':
        form = PublisherForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PublisherForm()
    return render(request, 'populate_forms.html', {'object': 'Add Publisher', 'form': form})
