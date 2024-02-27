from django.shortcuts import render
from .models import Book, Review, Author, Department

def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_url')  # Redirect to success page or other URL
    else:
        form = BookForm()
    return render(request, 'create_book.html', {'form': form})

def get_books(request):
    books = Book.objects.all()
    return render(request, 'index.html', {'items': books})


def get_authors(request):
    authors = Author.objects.all()
    return render(request, 'index.html', {'items': authors})


def get_reviews(request):
    reviews = Review.objects.all()
    return render(request, 'index.html', {'items': reviews})


def get_departments(request):
    departments = Department.objects.all()
    return render(request, 'index.html', {'items': departments})


# def my_view(request):
#     if request.method == 'POST':
#         form = MyForm(request.POST)
#         if form.is_valid():
#
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#
#             return HttpResponse("Form submitted successfully!")
#     else:
#         form = MyForm()
#     return render(request, 'index.html', {'form': form})