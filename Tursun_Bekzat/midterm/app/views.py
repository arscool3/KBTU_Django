from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import forms, authenticate, login, decorators, logout
from django.urls import reverse

from app.models import *


def basic_form(request, given_form):
    if request.method == 'POST':
        form = given_form(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(login)
        else:
            raise Exception(f"some errors {form.errors}")
    return render(request, 'login.html', {'form': given_form()})


def register_view(request):
    return basic_form(request, forms.UserCreationForm)


@decorators.login_required(login_url='login')
def logout_view(request):
    logout(request)
    # return render(request, 'about.html')
    return redirect(reverse('about'))


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            try:
                user = authenticate(**form.cleaned_data)
                login(request, user)
                if next := request.GET.get("next"):
                    if next != 'logout/':
                        return redirect(reverse('profile'))
                    return redirect(next)
                return render(request, 'basic.html')
            except Exception:
                return HttpResponse("something is not ok")
        else:
            raise Exception(f"some errors {form.errors}")
    return render(request, 'login.html', {'form': AuthenticationForm()})


def about_view(request):
    return render(request, 'about.html')


@decorators.login_required(login_url='login')
def profile_view(request):
    if request.user.is_authenticated:
        user = request.user
        student = Student.objects.filter(login=user).first()
        professor = Professor.objects.filter(login=user).first()

        if student:
            return render(request, 'profile.html', {'object': student, 'type': 'Student'})
        return render(request, 'profile.html', {'object': professor, 'type': 'Professor'})
    return render(request, 'profile.html', {'object': None, 'type': 'Not Authorized'})


@decorators.login_required(login_url='login')
def schedule_view(request):
    schedule_entries = Schedule.objects.all()
    hours = range(8, 23)
    schedule = {}
    for hour in hours:
        time_slot = f"{hour}:00 - {hour + 1}:00"
        schedule[time_slot] = ['' for _ in range(7)]

    for entry in schedule_entries:
        hour = entry.time.hour
        time_slot = f"{hour}:00 - {hour + 1}:00"
        day_index = entry.time.weekday()
        schedule[time_slot][day_index] = entry.discipline

    return render(request, 'schedule.html', {'schedule': schedule})


@decorators.login_required(login_url='login')
def journal_view(request):
    return render(request, 'journal.html')


@decorators.login_required(login_url='login')
def disciplines_view(request):
    disciplines = Discipline.objects.all()
    return render(request, 'disciplines.html', {'disciplines': disciplines})


@decorators.login_required(login_url='login')
def news_view(request):
    news_items = {}
    return render(request, 'news.html', {'news': news_items})