from django.shortcuts import render
from django.http import HttpResponse

from .forms import CourierForm, OrderForm, UserForm


def add_model(request, given_form, given_url, name):
    if request.method == "POST":
        form = given_form(request.POST)
        if form.is_valid():
            form.save()
        else:
            raise Exception(f"Some Exception {form.errors}")
        return HttpResponse(f'OK, {name} was created')

    return render(request, 'index.html', {'form': given_form(), 'given_url': given_url})


def add_courier(request):
    return add_model(request, CourierForm, 'add_courier', 'courier')


def create_oder(request):
    return add_model(request, OrderForm, 'create_order', 'order')


def add_user(request):
    return add_model(request, UserForm, 'add_user', 'user')