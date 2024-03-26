from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import *
from .models import *

# Create your views here.
def index(request):
    return render(request,"index.html")

def countryForm(request):
    if request.method=="POST":
        form = CountryForm(request.POST)
        if form.is_valid():
            c = Country(
                officialName=form.cleaned_data["officialName"],
                englishName=form.cleaned_data["englishName"],
                area=form.cleaned_data["area"])
            c.save()
            #print(c)
            return HttpResponseRedirect("../../")
    else:
        form = CountryForm()
    return render(request,"form.html",{"form":form,"entity":"Country"})

def cityForm(request):
    if request.method=="POST":
        form = CityForm(request.POST)
        if form.is_valid():
            c_ = form.cleaned_data["country"]
            n_ = form.cleaned_data["name"]
            c2 = Country.objects.get(englishName=c_)
            c = City(
                name=n_,
                country=c2)
            c.save()
            return HttpResponseRedirect("../../")
    else:
        form = CityForm()
    return render(request,"form.html",{"form":form,"entity":"City"})

def citizenForm(request):
    if request.method=="POST":
        form = CitizenForm(request.POST)
        if form.is_valid():
            c_ = form.cleaned_data["city"]
            c2 = City.objects.get(name=c_)
            c = Citizen(
                fname=form.cleaned_data["fname"],
                lname=form.cleaned_data["lname"],
                age=form.cleaned_data["age"],
                city=c2)
            c.save()
            return HttpResponseRedirect("../../")
    else:
        form = CitizenForm()
    return render(request,"form.html",{"form":form,"entity":"Citizen"})

def presidentForm(request):
    if request.method=="POST":
        form = PresidentForm(request.POST)
        if form.is_valid():
            c_ = form.cleaned_data["country"]
            c2 = Country.objects.get(englishName=c_)
            p = President(
                fname=form.cleaned_data["fname"],
                lname=form.cleaned_data["lname"],
                age=form.cleaned_data["age"],
                country=c2)
            p.save()
            return HttpResponseRedirect("../../")
    else:
        form = PresidentForm()
    return render(request,"form.html",{"form":form,"entity":"President"})

def countries(request,order=0):
    if order==0:
        cs = Country.objects.all()
    elif order==1:
        cs = Country.objects.area()
    else:
        cs = Country.objects.ofname()
    return render(request,"countries.html",{"countries":cs,"o":order})

def cities(request):
    cs = City.objects.all()
    return render(request,"cities.html",{"cities":cs})

def citizens(request):
    cs = Citizen.objects.all()
    return render(request,"citizens.html",{"citizens":cs})

def adults(request):
    cs = Citizen.objects.adults()
    return render(request,"citizens.html",{"citizens":cs})

def children(request):
    cs = Citizen.objects.kinder()
    return render(request,"citizens.html",{"citizens":cs})

def presidents(request):
    ps = President.objects.all()
    return render(request,"presidents.html",{"presidents":ps})

def country(request,name):
    c = Country.objects.get(englishName=name)
    cities = City.objects.filter(country=c)
    p = President.objects.get(country=c)
    return render(request,"country.html",{"country":c,"cities":cities,"president":p})

def city(request,name):
    c = City.objects.get(name=name)
    citizens = Citizen.objects.filter(city=c)
    return render(request,"city.html",{"city":c,"citizens":citizens,"pop":len(citizens)})

def citizen(request,name):
    c = Citizen.objects.get(fname=name)
    return render(request,"citizen.html",{"citizen":c})

def president(request,name):
    p = President.objects.get(fname=name)
    return render(request,"president.html",{"president":p})