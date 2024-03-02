from django.shortcuts import render, redirect, get_object_or_404
from .models import Author, Book, Publisher, Magazine
from .forms import AuthorForm, BookForm, PublisherForm, MagazineForm

def author_list(request):
    authors = Author.objects.all()
    return render(request, 'author_list.html', {'authors': authors})

def book_list(request):
    name_filter = request.GET.get('name')
    books = Book.objects.all()
    if name_filter:
        books = books.filter(title__icontains=name_filter)
    return render(request, 'book_list.html', {'books': books})

def publisher_list(request):
    name_filter = request.GET.get('name')
    publishers = Publisher.objects.prefetch_related('books')
    if name_filter:
        publishers = publishers.filter(name__icontains=name_filter)
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

def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    return render(request, 'author_detail.html', {'author': author})

def author_update(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect('author_detail', pk=pk)
    else:
        form = AuthorForm(instance=author)
    return render(request, 'author_form.html', {'form': form})

def author_delete(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if request.method == 'POST':
        author.delete()
        return redirect('author_list')
    return render(request, 'author_delete_confirm.html', {'author': author})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'book_detail.html', {'book': book})

def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_detail', pk=pk)
    else:
        form = BookForm(instance=book)
    return render(request, 'book_form.html', {'form': form})

def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'book_delete_confirm.html', {'book': book})

def publisher_detail(request, pk):
    publisher = get_object_or_404(Publisher, pk=pk)
    return render(request, 'publisher_detail.html', {'publisher': publisher})

def publisher_update(request, pk):
    publisher = get_object_or_404(Publisher, pk=pk)
    if request.method == 'POST':
        form = PublisherForm(request.POST, instance=publisher)
        if form.is_valid():
            form.save()
            return redirect('publisher_detail', pk=pk)
    else:
        form = PublisherForm(instance=publisher)
    return render(request, 'publisher_form.html', {'form': form})

def publisher_delete(request, pk):
    publisher = get_object_or_404(Publisher, pk=pk)
    if request.method == 'POST':
        publisher.delete()
        return redirect('publisher_list')
    return render(request, 'publisher_delete_confirm.html', {'publisher': publisher})

def magazine_detail(request, pk):
    magazine = get_object_or_404(Magazine, pk=pk)
    return render(request, 'magazine_detail.html', {'magazine': magazine})

def magazine_update(request, pk):
    magazine = get_object_or_404(Magazine, pk=pk)
    if request.method == 'POST':
        form = MagazineForm(request.POST, instance=magazine)
        if form.is_valid():
            form.save()
            return redirect('magazine_detail', pk=pk)
    else:
        form = MagazineForm(instance=magazine)
    return render(request, 'magazine_form.html', {'form': form})

def magazine_delete(request, pk):
    magazine = get_object_or_404(Magazine, pk=pk)
    if request.method == 'POST':
        magazine.delete()
        return redirect('magazine_list')
    return render(request, 'magazine_delete_confirm.html', {'magazine': magazine})

