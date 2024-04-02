from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import forms, authenticate, login, decorators, logout
from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from app.forms import *
from app.models import *
from app.serializers import SpecialitySerializer, FacultySerializer


def basic_form(request, given_form):
    if request.method == 'POST':
        form = given_form(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            raise Exception(f"some errors {form.errors}")
    return render(request, 'login.html', {'form': given_form()})


def register_view(request):
    return basic_form(request, UserCreationForm)


@decorators.login_required(login_url='login')
def logout_view(request):
    logout(request)
    return redirect(reverse('about'))


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            try:
                user = authenticate(**form.cleaned_data)
                login(request, user)
                if next := request.GET.get("next"):
                    return redirect(next)
                return redirect(reverse('profile'))
            except Exception:
                return HttpResponse("something is not ok")
        else:
            return redirect(reverse('register'))
            # raise Exception(f"some errors {form.errors}")
    return render(request, 'login.html', {'form': AuthenticationForm()})


def basic_view(request):
    superuser = None
    if request.user.is_authenticated:
        superuser = request.user
        student = Student.objects.filter(login=superuser).first()
        professor = Professor.objects.filter(login=superuser).first()
        if student or professor: superuser = None
    return superuser


def about_view(request):
    return render(request, 'about.html')


@decorators.login_required(login_url='login')
def profile_view(request):
    user = None
    if request.user.is_authenticated:
        user = request.user
        student = Student.objects.filter(login=user).first()
        professor = Professor.objects.filter(login=user).first()

        if student:
            return render(request, 'profile.html', {'object': student, 'type': 'Student'})
        if professor:
            return render(request, 'profile.html', {'object': professor, 'type': 'Professor'})
    return render(request, 'profile.html', {'object': None, 'type': 'Not Authorized', 'admin': user})


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
    superuser = basic_view(request)
    return render(request, 'schedule.html', {'schedule': schedule, 'admin': superuser})


@decorators.login_required(login_url='login')
def journal_view(request):
    superuser = basic_view(request)
    return render(request, 'journal.html', {'admin': superuser})


@decorators.login_required(login_url='login')
def disciplines_view(request):
    disciplines = Discipline.objects.all().filter()
    superuser = basic_view(request)
    return render(request, 'disciplines.html', {'disciplines': disciplines, 'admin': superuser})


@decorators.login_required(login_url='login')
def news_view(request):
    news_items = News.objects.all()
    superuser = basic_view(request)
    return render(request, 'news.html', {'news': news_items, 'admin': superuser})


def settings_view(request):
    superuser = basic_view(request)
    return render(request, 'settings.html', {'admin': superuser})


def crud(request, myForm):
    if request.method == 'POST':
        form = myForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news')
    else:
        form = myForm()
    return render(request, 'login.html', {'form': form})


def crud_news(request):
    return crud(request, NewsForm)


def crud_student(request):
    return crud(request, StudentForm)


def crud_faculty(request):
    return crud(request, FacultyForm)


def crud_schedule(request):
    return crud(request, ScheduleForm)


def crud_professor(request):
    return crud(request, ProfessorForm)


def crud_discipline(request):
    return crud(request, DisciplineForm)


def crud_speciality(request):
    return crud(request, SpecialityForm)



class FacultyListCreateAPIView(APIView):
    def get(self, request):
        faculties = Faculty.objects.all()
        serializer = FacultySerializer(faculties, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FacultySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SpecialityListCreateAPIView(APIView):
    def get(self, request):
        specialities = Speciality.objects.all()
        serializer = SpecialitySerializer(specialities, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SpecialitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)