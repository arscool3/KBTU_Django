from django.shortcuts import render, HttpResponse, redirect
from .models import Client, Manager, Request
from .forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout, forms

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            print(form.errors)
    return render(request, 'log_reg.html', {'form': UserCreationForm})

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
                return redirect('application_page')
            except Exception:
                pass
        else:
            return render(request, 'log_reg.html', {'form': forms.AuthenticationForm(), 'comment': 'Wrong credentials, or you still do not have access to enter the Web page'})
    elif request.method == "GET":
        return render(request, 'log_reg.html', {'form': forms.AuthenticationForm()})

