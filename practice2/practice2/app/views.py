from django.shortcuts import render

# Create your views here.

def book_list_view(request):
    books = ['Abai', 'Adam', 'Eva']  # Sample books data
    return render(request, 'index.html', {'books': books})