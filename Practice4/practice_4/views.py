from django.shortcuts import render
from .models import Book, Publisher, Author
from .managers import BookManager, PublisherManager, AuthorManager
from .forms import BookForm

def get_books_by_author(request, author_name):
    books = Book.objects.get_books_by_author(author_name)
    return render(request, 'object_list.html', {'objects': books, 'title': f'Books by {author_name}'})

def get_publishers_with_magazines(request):
    publisher_manager = PublisherManager()
    publishers = publisher_manager.get_publishers_with_magazines()
    return render(request, 'object_list.html', {'objects': publishers, 'title': 'Publishers with Magazines'})

def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = BookForm()

    return render(request, 'create_object.html', {'form': form})

def get_authors(request):
    author_manager = AuthorManager()
    authors = author_manager.get_authors_with_books()
    return render(request, 'object_list.html', {'objects': authors, 'title': 'Authors with Books'})
