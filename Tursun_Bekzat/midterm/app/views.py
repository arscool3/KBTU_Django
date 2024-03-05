from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import forms, authenticate, login, decorators, logout
from app.models import *

def basic_form(request, given_form):
    if request.method == 'POST':
        form = given_form(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(login)
        else:
            raise Exception(f"some erros {form.errors}")
    return render(request, 'login.html', {'form': given_form()})


def register_view(request):
    return basic_form(request, forms.UserCreationForm)

@decorators.login_required(login_url='login')
def logout_view(request):
    logout(request)
    return render(request, 'login.html')


def login_view(request):
    if request.method == 'POST':
        form = forms.AuthenticationForm(data=request.POST)
        if form.is_valid():
            try:
                user = authenticate(**form.cleaned_data)
                login(request, user)
                if next := request.GET.get("next"):
                    if next != 'logout/':
                        return redirect('home/')
                    return redirect(next)
                return render(request, 'home.html')
            except Exception:
                return HttpResponse("something is not ok")
        else:
            raise Exception(f"some erros {form.errors}")
    return render(request, 'login.html', {'form': forms.AuthenticationForm()})

@decorators.login_required(login_url='login')
def home_view(request):
    # if request.user.is_authenticated:
    return render(request, 'home.html', {'content': f'Welcome, {request.user.password}!'})
    # return render(request, 'login.html')

@decorators.login_required(login_url='login')
def profile_view(request):
    user = request.user
    student = Student.objects.filter(login=user).first()
    professor = Professor.objects.filter(login=user).first()
    if student:
        return render(request, 'profile.html', {'object': student, 'type': 'Student'})
    return render(request, 'profile.html', {'object': professor, 'type': 'Professor'})


@decorators.login_required(login_url='login')
def schedule_view(request):
    # Assuming you have a model for schedule
    # Replace 'Schedule' with your actual model name
    # Assuming each schedule entry has fields 'time' and 'discipline'
    # Adjust the queryset based on your actual model structure
    schedule_entries = Schedule.objects.all()

    # Generate time slots for each hour from 8:00 to 22:00
    hours = range(8, 23)

    # Create an empty schedule dictionary to hold the schedule data
    schedule = {}
    for hour in hours:
        # Format the hour as 'HH:00 - HH+1:00'
        time_slot = f"{hour}:00 - {hour + 1}:00"
        # Initialize an empty list for each time slot
        schedule[time_slot] = ['' for _ in range(7)]  # Assuming 7 days in a week

    # Populate the schedule dictionary with actual schedule data
    for entry in schedule_entries:
        # Convert time to hour format
        hour = entry.time.hour
        time_slot = f"{hour}:00 - {hour + 1}:00"
        # Assuming day_index is the index representing the day (e.g., 0 for Monday, 1 for Tuesday, etc.)
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