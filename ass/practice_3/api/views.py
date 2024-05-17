from django.shortcuts import render, redirect
from .forms import BookForm
from .models import Book
def bookView(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookForm()
    return render(request, 'books.html', {'form': form})

def home(request):
    books = Book.objects.all()
    return render(request, 'list.html', {"books" : books})