from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.core.serializers import serialize
import json
from .models import Book
from .forms import BookForm


def basic_form(request, given_form):
    if request.method == 'POST':
        form = given_form(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("OK")
        else:
            raise Exception(f"some erros {form.errors}")
    return render(request, 'index.html', {'form': given_form()})



def add_books(request):
    return basic_form(request, BookForm)


def get_books(request):
    books = Book.objects.all()
    return render(request, 'books.html', {'books': books})

def get_book(request, pk):
    try:
        book = Book.objects.get(id=pk)
        book_data = serialize('json', [book])
        book_json = json.loads(book_data)[0]['fields']
        return JsonResponse(book_json, safe=False)
    except Book.DoesNotExist:
        return JsonResponse({'error': 'Book not found'}, status=404)









