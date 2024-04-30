from django import forms
from django.http import HttpResponse
from django.shortcuts import redirect, render

from main.forms import AuthorForm, BookForm, CategoryForm, ConsumerForm, ReviewForm
from django.contrib.auth import authenticate, login, decorators, logout, forms
from django.contrib.admin.views.decorators import staff_member_required

from django.contrib.auth.models import User
from.models import Author, Category, Book, Consumer, Review

@decorators.login_required(login_url='login')
def index(request):
  if request.user.is_staff:
    return render(request, 'admin_page.html')
  else:
    return render(request, 'user_page.html')

def basic_form(request, given_form):
  if request.method == 'POST':
    form = given_form(data=request.POST)
    if form.is_valid():
      form.save()
    else:
      raise Exception(f"some erros {form.errors}")
  return render(request, 'login.html', {'form': given_form()})

def logout_view(request):
  logout(request)
  return render(request, 'logout.html')

def login_view(request):
  if request.method == 'POST':
    form = forms.AuthenticationForm(data=request.POST)
    if form.is_valid():
      try:
        user = authenticate(**form.cleaned_data)
        login(request, user)
        if next := request.GET.get("next"):
          return redirect(next)
        return HttpResponse("OK")
      except Exception:
        return render(request, 'error.html', {'title': 'Invalid credentials', 'message': 'Please, enter valid user data.'})
    else:
      return render(request, 'error.html', {'title': 'Invalid credentials', 'message': 'Please enter a correct username and password. Note that both fields may be case-sensitive.'})
  return render(request, 'login.html', {'form': forms.AuthenticationForm()})


@decorators.login_required(login_url='login')
def users(request):
  if request.method == 'GET':
    users = User.objects.all()
    return render(request, 'users.html', {'users': users})
  
  if request.method == 'POST':
    form = forms.UserCreationForm(request.POST)
    try:
      if form.is_valid():
        form.save()
        return redirect('/users')
    except Exception as e:
      print(e)
  else:
    form = forms.UserCreationForm()
  context = {'form': form, 'model': 'user'}
  return render(request, 'form.html', context)

@decorators.login_required(login_url='login')
def authors(request):
  if request.method == 'GET':
    authors = Author.objects.all()
    return render(request, 'authors.html', {'authors': authors})
  if request.method == 'POST':
    form = AuthorForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('/authors')
  else:
    form = AuthorForm()
  context = {'form': form, 'model': 'author'}
  return render(request, 'form.html', context)

@decorators.login_required(login_url='login')
def categories(request):
  if request.method == 'GET':
    categories = Category.objects.all()
    return render(request, 'categories.html', {'categories': categories})
  if request.method == 'POST':
    form = CategoryForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('/categories')
  else:
    form = CategoryForm()
  context = {'form': form, 'model': 'category'}
  return render(request, 'form.html', context)

@decorators.login_required(login_url='login')
def books(request):
  if request.method == 'GET':
    sort_by = request.GET.get('sort_by')
    books = Book.objects
    if sort_by == 'author':
      books = books.order_by_author()
    else:
      books = books.all()
    return render(request, 'books.html', {'books': books})
  if request.method == 'POST':
    form = BookForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('/books')
  else:
    form = BookForm()
  context = {'form': form, 'model': 'book'}
  return render(request, 'form.html', context)

@decorators.login_required(login_url='login')
def get_book(request, id):
  book = Book.objects.get(pk=id)
  if book:
    return render(request, 'book.html', {'book': book})
  else:
    return HttpResponse("Book doesn't exist!")

@decorators.login_required(login_url='login')
def consumers(request):
  if request.method == 'GET':
    consumers = Consumer.objects.all()
    return render(request, 'consumers.html', {'consumers': consumers})
  if request.method == 'POST':
    form = ConsumerForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('/consumers')
  else:
    form = ConsumerForm()
  context = {'form': form, 'model': 'consumer'}
  return render(request, 'form.html', context)

@decorators.login_required(login_url='login')
def reviews(request):
  if request.method == 'GET':
    sort_by = request.GET.get('sort_by')
    reviews = Review.objects.all()
    if sort_by == 'book':
      reviews = sorted(reviews, key=lambda review: review.book.title)
    elif sort_by == 'user':
      reviews = sorted(reviews, key=lambda review: review.user.username)
    return render(request, 'reviews.html', {'reviews': reviews})
  if request.method == 'POST':
    form = ReviewForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('/reviews')
  else:
    form = ReviewForm()
  context = {'form': form, 'model': 'review'}
  return render(request, 'form.html', context)