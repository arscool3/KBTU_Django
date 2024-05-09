from datetime import date, datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, decorators, logout
from django.contrib.auth import forms as auth_forms

from .models import FitnessUser, Goal, HealthMetrics, CurrentProgress
from .forms import *


def register_view(request):
    if request.method == 'POST':
        form = auth_forms.UserCreationForm(data=request.POST)
        if form.is_valid():
            f_user = FitnessUser(username=form.cleaned_data['username'], fullname=form.cleaned_data['username'])
            form.save()
            f_user.save()
            goal = Goal(user=f_user)
            goal.save()
            health_metrics = HealthMetrics(user=f_user)
            health_metrics.save()
            return HttpResponse("OK")
        else:
            raise Exception(f"some errors {form.errors}")
    return render(request, 'index.html', {'form': auth_forms.UserCreationForm})


def logout_view(request):
    logout(request)
    return HttpResponse("You have logout")


def login_view(request):
    if request.method == 'POST':
        form = auth_forms.AuthenticationForm(data=request.POST)
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
            raise Exception(f"some errors {form.errors}")
    return render(request, 'index.html', {'form': auth_forms.AuthenticationForm()})


@decorators.login_required(login_url='login')
def fitness_user_view(request):
    if request.method == 'POST':
        f_user = FitnessUser.objects.get(username=request.user.username)
        form = FitnessUserForm(instance=f_user)
        if form.is_valid():
            form.save()
            return HttpResponse("OK")
        else:
            raise Exception(f"some errors {form.errors}")
    return render(request, 'index.html', {'form': FitnessUserForm})


@decorators.login_required(login_url='login')
def activity_view(request):
    if request.method == 'POST':
        form = ActivityForm(data=request.POST)
        if form.is_valid():
            activity = form.save(commit=False)
            activity.user = FitnessUser.objects.get(username=request.user.username)
            activity.save()
            return HttpResponse("OK")
        else:
            raise Exception(f"some errors {form.errors}")
    return render(request, 'index.html', {'form': ActivityForm})


@decorators.login_required(login_url='login')
def diet_view(request):
    if request.method == 'POST':
        form = DietForm(data=request.POST)
        if form.is_valid():
            diet = form.save(commit=False)
            diet.user = FitnessUser.objects.get(username=request.user.username)
            diet.registered_datetime = datetime.now()
            diet.save()
            return HttpResponse("OK")
        else:
            raise Exception(f"some errors {form.errors}")
    return render(request, 'index.html', {'form': DietForm})


@decorators.login_required(login_url='login')
def health_metrics_view(request):
    if request.method == 'POST':
        f_user = HealthMetrics.objects.get(user__username=request.user.username)
        form = HealthMetricsForm(data=request.POST, instance=f_user)
        if form.is_valid():
            form.save()
            return HttpResponse("OK")
        else:
            raise Exception(f"some errors {form.errors}")
    return render(request, 'index.html', {'form': HealthMetricsForm})


@decorators.login_required(login_url='login')
def goal_view(request):
    if request.method == 'POST':
        f_user = Goal.objects.get(user__username=request.user.username)
        form = GoalForm(data=request.POST, instance=f_user)
        if form.is_valid():
            form.save()
            return HttpResponse("OK")
        else:
            raise Exception(f"some errors {form.errors}")
    return render(request, 'index.html', {'form': GoalForm})


@decorators.login_required(login_url='login')
def progress_view(request):
    if request.method == 'POST':
        form = ProgressForm(data=request.POST)
        if form.is_valid():
            progress = form.save(commit=False)
            progress.user = FitnessUser.objects.get(username=request.user.username)
            progress.date = date.today()
            progress.save()
            CurrentProgress.objects.update_calories(progress.user, progress.date)
            return HttpResponse("OK")
        else:
            raise Exception(f"some errors {form.errors}")
    return render(request, 'index.html', {'form': ProgressForm})


@decorators.login_required(login_url='login')
def check_fitness_user(request):
    items = FitnessUser.objects.filter(username=request.user.username).all()
    data = []
    for item in items:
        data.append("Username: " + item.username + ". Fullname: " + item.fullname)
    return render(request, 'check.html', {'data': data, 'data_name': 'user params'})


@decorators.login_required(login_url='login')
def check_activities(request):
    items = Activity.objects.filter(user__username=request.user.username).all()
    data = []
    for item in items:
        data.append(
            item.activity_name + ". Stared at " + str(item.start_datetime) +
            ", ended at " + str(item.end_datetime) + ". Calories burnt " + str(item.burnt_calories)
        )
    return render(request, 'check.html', {'data': data, 'data_name': 'activities'})


@decorators.login_required(login_url='login')
def check_diets(request):
    items = Diet.objects.filter(user__username=request.user.username).all()
    data = []
    for item in items:
        data.append(
            item.food_name + " at " + str(item.registered_datetime) + ", "
            + str(item.calorie_content) + "calories")
    return render(request, 'check.html', {'data': data, 'data_name': 'diets'})


@decorators.login_required(login_url='login')
def check_health_metrics(request):
    items = HealthMetrics.objects.filter(user__username=request.user.username).all()
    data = []
    for item in items:
        data.append("Weight = " + str(item.weight) + ", height = "
                    + str(item.height) + ", age = " + str(item.age) + ", sex = " + item.sex + ", blood type = " + item.blood_type)
    return render(request, 'check.html', {'data': data, 'data_name': 'health metrics'})


@decorators.login_required(login_url='login')
def check_goal(request):
    items = Goal.objects.filter(user__username=request.user.username).all()
    data = []
    for item in items:
        data.append(
            "Goal is " + str(item.steps) + " steps, " + str(item.burnt_calories) + "burnt calories, " +
            str(item.eaten_calories) + "eaten calories, " + str(item.sleep_time) + "sleep hours"
        )
    return render(request, 'check.html', {'data': data, 'data_name': 'goal parameters'})


@decorators.login_required(login_url='login')
def check_progress(request):
    items = CurrentProgress.objects.filter(user__username=request.user.username).all()
    data = []
    for item in items:
        data.append(
            "Goal progress for " + str(item.date) + " is " + str(item.steps) + " steps, " +
            str(item.burnt_calories) + "burnt calories, " + str(item.eaten_calories) +
            "eaten calories, " + str(item.sleep_time) + " sleep hours"
        )
    return render(request, 'check.html', {'data': data, 'data_name': 'diets'})
