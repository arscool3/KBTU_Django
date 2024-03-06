from django.shortcuts import render

from django.http import HttpResponse
from .models import *
from .form import *


def get_users(request):
    users = CustomUser.objects.all()
    return render(request, 'index.html', {"iterable": users, "object": "Users"})


def get_user(request):
    user = CustomUser.objects.get_name('user1');

    return render(request, 'index.html', {"iterable": user, "object": "Users"})



def add_model(request, given_form, given_url, name):
    if request.method == "POST":
        form = given_form(request.POST)
        if form.is_valid():
            form.save()
        else:
            raise Exception(f"Some Exception {form.errors}")
        return HttpResponse(f'OK, {name} was created')

    return render(request, 'index.html', {'form': given_form(), 'given_url': given_url})


def create_user(request):
    return add_model(request, UserForm, 'add_user', 'user')