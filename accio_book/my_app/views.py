from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, decorators, logout, forms
from django.contrib.auth.forms import AuthenticationForm
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from my_app.serializers import AuthorSerializer, BookSerializer, UserProfileSerializer, FavoriteSerializer, GenreSerializer
from django.contrib.auth.decorators import login_required
from my_app.models import Author, Book, UserProfile, Favorite, Genre, User
from my_app.forms import BookForm, AuthorForm, FavoriteForm, GenreForm


# 6 Post requests

def homepage(request):
    return render(request, 'homepage.html')

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
    if request.method == 'POST':
        form = forms.UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            raise Exception(f"some erros {form.errors}")
    return render(request, 'index.html', {'form': forms.UserCreationForm()})
   

def logout_view(request):
    logout(request)
    return redirect('homepage')


def login_view(request):
    if request.method == 'POST':
        form = forms.AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = authenticate(**form.cleaned_data)
            login(request, user)
            next_url = request.session.pop('next_url', None)
            if next_url:
                return redirect(next_url)
            else:
                return redirect('get_all_books')
    else:
        form = forms.AuthenticationForm()
    return render(request, 'index.html', {'form': form})


@decorators.login_required(login_url='login')
def check_view(request):
    if request.user.is_authenticated:
        return HttpResponse(f"{request.user} is authenticated")
    raise Exception(f"{request.user} is not authenticated")


def add_book(request):
    if request.method == 'POST':
        serializer = BookSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    else:
        if request.user.is_authenticated:
            return basic_form(request, BookForm)
        else:
            next_url = request.GET.get('next')
            print("Next URL:", next_url) 
            request.session['next_url'] = next_url
            return redirect('login')

def add_author(request):
    if request.method == 'POST':
        serializer = AuthorSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    else:
        if request.user.is_authenticated:
            return basic_form(request, AuthorForm)
        else:
            next_url = request.GET.get('next')
            print("Next URL:", next_url) 
            request.session['next_url'] = next_url
            return redirect('login')
        
def add_genre(request):
    if request.method == 'POST':
        serializer = GenreSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    else:
        if request.user.is_authenticated:
            return basic_form(request, GenreForm)
        else:
            next_url = request.GET.get('next')
            print("Next URL:", next_url) 
            request.session['next_url'] = next_url
            return redirect('login')


# 6 Get requests
        
@api_view(['GET'])
def get_all_books(request):
    if request.user.is_authenticated:
        books = Book.objects.all()
        return render(request, 'book.html', {'books': books})
    else:
        next_url = request.GET.get('next')
        request.session['next_url'] = next_url
        return redirect('login')


@api_view(['GET'])
def get_book_details(request, book_id):
    try:
        book = Book.objects.get(pk=book_id)
        serializer = BookSerializer(book)
        return JsonResponse(serializer.data)
    except Book.DoesNotExist:
        return JsonResponse({'error': 'Book not found'}, status=404)

@api_view(['GET'])
def get_all_authors(request):
    authors = Author.objects.all()
    serializer = AuthorSerializer(authors, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def get_author_details(request, author_id):
    try:
        author = Author.objects.get(pk=author_id)
        serializer = AuthorSerializer(author)
        return JsonResponse(serializer.data)
    except Author.DoesNotExist:
        return JsonResponse({'error': 'Author not found'}, status=404)
    
@api_view(['GET'])
def get_all_genres(request):
    genres = Genre.objects.all()
    serializer = GenreSerializer(genres, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def get_genre_details(request, genre_id):
    try:
        genre = Genre.objects.get(pk=genre_id)
        serializer = GenreSerializer(genre)
        return JsonResponse(serializer.data)
    except genre.DoesNotExist:
        return JsonResponse({'error': 'genre not found'}, status=404)

