from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, decorators, logout, forms
from django.http import JsonResponse
from django.core.serializers import serialize
import json
from .models import Book, Genre, Review, Publisher
from .forms import BookForm, ReviewForm


def basic_form(request, given_form):
    if request.method == 'POST':
        form = given_form(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("OK")
        else:
            raise Exception(f"some erros {form.errors}")
    return render(request, 'index.html', {'form': given_form()})


def register_view(request):
    return basic_form(request, forms.UserCreationForm)


@decorators.permission_required('core.can_add_books', login_url='login')
def add_books(request):
    return basic_form(request, BookForm)


def logout_view(request):
    logout(request)
    return redirect('login')


def login_view(request):
    if request.method == 'POST':
        form = forms.AuthenticationForm(data=request.POST)
        if form.is_valid():
            try:
                user = authenticate(**form.cleaned_data)
                login(request, user)
                if next := request.GET.get("next"):
                    return redirect(next)
                return redirect("books")
            except Exception:
                return HttpResponse("something is not ok")
        else:
            raise Exception(f"some erros {form.errors}")
    return render(request, 'index.html', {'form': forms.AuthenticationForm()})


@decorators.login_required(login_url='login')
def check_view(request):
    if request.user.is_authenticated:
        return HttpResponse(f"{request.user} is authenticated")
    raise Exception(f"{request.user} is not authenticated")


@decorators.login_required(login_url='login')
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


def get_genres(request):
    genres = Genre.objects.all()
    genres_list = list(genres.values())
    return JsonResponse(genres_list, safe=False)


def get_reviews(request, pk):
    book = Book.objects.get(id=pk)
    reviews = Review.objects.filter(book=book)
    print(reviews)
    reviews_list = list(reviews.values())
    return JsonResponse(reviews_list, safe=False)


def get_publishers(request):
    publishers = Publisher.objects.all()
    publishers_list = list(publishers.values())
    return JsonResponse(publishers_list, safe=False)


def add_review(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.book = book
            review.save()
            return redirect('get_book', pk=pk)  # Redirect to book detail page or any other appropriate page
    else:
        form = ReviewForm()

    return render(request, 'add_review.html', {'form': form})
