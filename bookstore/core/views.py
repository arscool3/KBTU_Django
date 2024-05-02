from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, decorators, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .models import Book
from .forms import BookForm
from django.http import HttpResponse

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = authenticate(request, **form.cleaned_data)
            if user is not None:
                login(request, user)
                return render(request, 'home.html')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form':form})


@decorators.login_required(login_url='login')
def home(request):
    return render(request, 'home.html')

@decorators.login_required(login_url='login')
def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

@decorators.login_required(login_url='login')
def book_detail(request, pk):
    book = Book.objects.get(pk=pk)
    return render(request, 'book_detail.html', {'book': book})

@decorators.login_required(login_url='login')
def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return HttpResponse('Form is invalid')

    else:
       form = BookForm()
    return render(request, 'create_book.html', {'form': form })

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('book_list')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponse("You have logout")
