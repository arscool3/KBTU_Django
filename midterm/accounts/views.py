from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login, authenticate, logout, forms


def register(request):
    if request.method == 'POST':
        form = forms.UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    else:
        form = forms.UserCreationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = forms.AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if next := request.GET.get("next"):
                    return redirect(next)
                return redirect('accounts:profile')
        else:
            raise Exception(f"some erros {form.errors}")
    else:
        form = forms.AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('home')


def profile(request):
    return render(request, 'profile.html')


def paper_shelf(request):
    account = request.user.account
    paper_shelf = account.paper_shelf
    if paper_shelf:
        papers = paper_shelf.papers.all()
    else:
        papers = None
    return render(request, 'paper_shelf.html', {'papers': papers})

