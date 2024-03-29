from django.shortcuts import render,get_object_or_404, HttpResponse, redirect
from django.contrib.auth import authenticate, login, decorators, logout, forms
from django.http import HttpResponseRedirect
from .models import *
from .forms import GistForm, CommitForm, FileForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

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
        form = forms.UserCreationForm(request.POST)
        if form.is_valid():
            form.save()


            return redirect('register')
    else:
        form = forms.UserCreationForm()
    
    return render(request, 'register.html', {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponse("You have logout")


def login_view(request):
    if request.method == 'POST':
        form = forms.AuthenticationForm(data=request.POST)
        if form.is_valid():
            try:
                user = authenticate(**form.cleaned_data)
                login(request, user)
                if next := request.GET.get("next"):
                    return redirect(next)
                return HttpResponse("everything is ok")
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
def gistReq(request):
    if request.method == 'POST':
        gist = GistForm(request.POST)
        if gist.is_valid():
            gist.save()
        else:
            raise Exception(f"Some Exception {gist.errors}")
        return HttpResponse("gist created successfully")
    elif request.method == 'GET':
        gist = Gist.objects
        if gist_name := request.GET.get('gist_name'):
            gist = gist.filter(gist__name=gist_name.capitalize())

        gist = gist.all()
    return render(request, 'gist.html', {'form': gist.values()})

@decorators.login_required(login_url='login')
def commitReq(request, gist_id):
    gist = get_object_or_404(Gist, ID=gist_id)
    if request.method == 'POST':
        commit = CommitForm(request.POST)

        if commit.is_valid():
            commit = commit.save(commit=False)
            commit.GistID = gist
            commit.save()
        else:
            raise Exception(f"Some Exception {commit.errors}")
        return HttpResponse("commit created successfully")
    elif request.method == 'GET':
        commit = Commit.objects
        if commit_name := request.GET.get('commit_name'):
            commit = commit.filter(commit__name=commit_name.capitalize())

        commit = commit.all()
    return render(request, 'commit.html', {'form': commit.values()})

@decorators.login_required(login_url='login')
def fileReq(request, commit_id):
    commit = get_object_or_404(Commit, ID=commit_id)
    if request.method == 'POST':
        file = FileForm(request.POST)

        if file.is_valid():
            file = file.save(commit=False)
            file.CommitID = commit
            file.save()
        else:
            raise Exception(f"Some Exception {file.errors}")
        return HttpResponse("file created successfully")
    elif request.method == 'GET':
        file = File.objects
        if file_name := request.GET.get('file_name'):
            file = file.filter(file__name=file_name.capitalize())

        file = file.all()
    return render(request, 'file.html', {'form': file.values()})
