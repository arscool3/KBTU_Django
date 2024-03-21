# myapp/views.py

from django.shortcuts import render
from .models import *

def get_authors(request):
    authors = Author.objects.authors_with_books()
    return render(request, 'authors.html', {'authors': authors})

def get_publishers(request):
    publishers = Publisher.objects.get_publishers_with_magazines()
    return render(request, 'publishers.html', {'publishers': publishers})
