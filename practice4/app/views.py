from django.shortcuts import render
from django.http import HttpResponse
from .forms import *

# Create your views here.


def index(request):
    return HttpResponse("Hello World!")


def add_brand(request):
    if request.method == 'POST':
        form = BrandForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("saved")
        else:
            raise Exception(f"some erros {form.errors}")
    return render(request, 'form.html', {'form': BrandForm()})


def add_reseller(request):
    if request.method == 'POST':
        form = ResellerForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("saved")
        else:
            raise Exception(f"some erros {form.errors}")
    return render(request, 'form.html', {'form': ResellerForm()})


def add_model(request):
    if request.method == 'POST':
        form = ModelForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("saved")
        else:
            raise Exception(f"some erros {form.errors}")
    return render(request, 'form.html', {'form': ModelForm()})


def add_showroom(request):
    if request.method == 'POST':
        form = ShowroomForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("saved")
        else:
            raise Exception(f"some erros {form.errors}")
    return render(request, 'form.html', {'form': ShowroomForm()})


def get_models(request):
    if request.method == 'GET':
        models = Model.objects.all()
        return render(request, 'index.html', {'iterable': models})


def get_resellers(request):
    if request.method == 'GET':
        resellers = Reseller.objects.all()
        return render(request, 'index.html', {'iterable': resellers})


def get_models_by_brand(request):
    if request.method == 'POST':
        form = BrandChooseForm(request.POST)
        if form.is_valid():
            brand = form.cleaned_data['brand']
            models = Model.objects.get__post_by_topic(brand=brand)
            return render(request, 'index.html', {'models': models})
    else:
        form = BrandChooseForm()
    return render(request, 'form.html', {'form': form})