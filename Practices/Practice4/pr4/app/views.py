from django.http import HttpResponse
from django.shortcuts import render
from .forms import *

# Create your views here.


def add_model(request, given_form, given_url, name):
    if request.method == "POST":
        form = given_form(request.POST)
        if form.is_valid():
            form.save()
        else:
            raise Exception(f"Some Exception {form.errors}")
        return HttpResponse(f'OK, {name} was created')

    return render(request, 'app/AddObjects.html', {'form': given_form(), 'given_url': given_url})

def add_person(request):
    return add_model(request, PersonForm , 'AddPerson', 'person')

def add_family(request):
    return add_model(request, FamilyForm, 'AddFamily', 'family')

def add_doctor(request):
    return add_model(request, DoctorForm, 'AddDoctor', 'doctor')

def add_hospital(request):
    return add_model(request, HospitalForm , 'AddHospital', 'hospital')


def showPersons(request):
    return render(request, 'app/GetPerson.html', {'persons': Person.objects.all()})

def showPersons_byFamily(request, f_id):
    return render(request, 'app/GetPerson.html', {'persons': Person.objects.all().get_by_family(f_id)})

def showPersons_byAge(request, age):
    return render(request, 'app/GetPerson.html', {'persons': Person.objects.all().get_by_age(age)})

def showPerson(request, p_id):
    return render(request, 'app/GetPerson.html', {'persons': [Person.objects.all().get_by_id(p_id)]})


def showFamily(request):
    return render(request, 'app/GetFamilies.html', {'families': Family.objects.all()})


def showDoctors(request):
    return render(request, 'app/GetDoctors.html', {'doctors': FamilyDoctor.objects.all()})

def showDoctor_byHospital(request, h_id):
    return render(request, 'app/GetDoctors.html', {'doctors': FamilyDoctor.objects.all().get_by_hospital(h_id)})

def showDoctor(request, d_id):
    return render(request, 'app/GetDoctors.html', {'doctors': [FamilyDoctor.objects.all().get_by_id(d_id)]})


def showHospital(request):
    return render(request, 'app/GetHospitals.html', {'hospitals': Hospital.objects.all()})

