from django.contrib.auth import authenticate, login, forms
from .serializers import CustomUserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm

def homepage(request):
    return render(request, 'home.html')

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = authenticate(**form.cleaned_data)
            login(request, user)
            return redirect('home') 
    else:
        form = forms.AuthenticationForm()
    form = forms.AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout(request):
    return render(request, 'logout.html')


def registration(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            raise Exception(f"some erros {form.errors}")
        
    form = CustomUserCreationForm(request.POST)
    return render(request, 'registration.html', {'form': form})


