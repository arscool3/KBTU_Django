from django.shortcuts import render
from .models import Author,Book,Publisher,Magazine, Consultant,BookstoreClerk
from .forms import MagazineForm,PublisherForm,AuthorForm,BookForm


def get_bookstore(request):
    authors = Author.objects.all()
    books = Book.objects.all()
    publishers = Publisher.objects.all()
    magazines = Magazine.objects.all()
    author_form = AuthorForm(prefix='author')
    book_form = BookForm(prefix='book')
    publisher_form = PublisherForm(prefix='publisher')
    magazine_form = MagazineForm(prefix='magazine')

    expensive_books = Book.consultants.expensive_books()
    fiction_books = Book.consultants.fiction_books()
    alphabetically_books = Book.bookstore_clerks.alphabetically_books()
    non_fiction_books = Book.bookstore_clerks.non_fiction_books()

    if request.method == 'POST':
        book_form = BookForm(request.POST, prefix='book')
        author_form = AuthorForm(request.POST, prefix='author')
        publisher_form = PublisherForm(request.POST, prefix='publisher')
        magazine_form = MagazineForm(request.POST, prefix='magazine')
        if book_form.is_valid():
            Book.objects.create(**book_form.cleaned_data)
            book_form = BookForm()
        elif author_form.is_valid():
            Author.objects.create(**author_form.cleaned_data)
        elif publisher_form.is_valid():
            Publisher.objects.create(**publisher_form.cleaned_data)
        elif magazine_form.is_valid():
            Magazine.objects.create(**magazine_form.cleaned_data)

    return render(request, 'bookstore.html', {
        'authors': authors,
        'books': books,
        'publishers': publishers,
        'magazines': magazines,
        'book_form': book_form,
        'author_form': author_form,
        'publisher_form': publisher_form,
        'magazine_form': magazine_form,
        'expensive_books': expensive_books,
        'fiction_books': fiction_books,
        'alphabetically_books': alphabetically_books,
        'non_fiction_books': non_fiction_books
    })