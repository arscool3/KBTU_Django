from django.shortcuts import render, redirect
from django.http import Http404
from main.models import Author
from main.forms import AuthorForm


def author_list(request):
    authors = Author.objects.all()
    context = {
        'authors': authors
    }
    return render(request, 'author/list.html', context)


def author_detail(request, author_id):
    try:
        author = Author.objects.get(id=author_id)
    except Author.DoesNotExist:
        raise Http404("Author not found")
    context = {
        'author': author,
        'books': author.books.all()
    }
    return render(request, 'author/detail.html', context)


def author_new(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('author_list')
    else:
        form = AuthorForm()
    context = {
        'form': form
    }
    return render(request, 'author/new.html', context)


def book_list(request):
    return render(request, 'book/list.html')
