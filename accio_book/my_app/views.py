from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, decorators, logout, forms
from django.contrib.auth.forms import AuthenticationForm

from my_app.models import Book
from my_app.forms import BookForm

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


def add_books(request):
    if request.user.is_authenticated:
        return basic_form(request, BookForm)
    else:
        next_url = request.GET.get('next')
        print("Next URL:", next_url) 
        request.session['next_url'] = next_url
        return redirect('login')

def add_books(request):
    return basic_form(request, BookForm)
   

def logout_view(request):
    logout(request)
    return HttpResponse("You have logout")


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
                return redirect('books')  # Перенаправление на главную страницу после входа
    else:
        form = forms.AuthenticationForm()
    return render(request, 'index.html', {'form': form})


@decorators.login_required(login_url='login')
def check_view(request):
    if request.user.is_authenticated:
        return HttpResponse(f"{request.user} is authenticated")
    raise Exception(f"{request.user} is not authenticated")


@decorators.login_required(login_url='login')
def get_books(request):
    books = Book.objects.all()
    return render(request, 'book.html', {'books': books})