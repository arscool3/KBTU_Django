from django.shortcuts import render
from .models import Author, Book, Publisher
from .forms import BookForm

def authors(request):
    authors = Author.objects.all()
    return render(request, 'authors.html', {'authors'})

def publishers(request):
    publishers = Publisher.objects.all()
    return render(request, 'publishers.html', {'publishers'})

def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = BookForm()
    return render(request, 'create_book.html', {'form': form})
