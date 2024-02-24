from django.shortcuts import render
from django.http import HttpResponse

from core.forms import LessonForm, StudentForm, TeacherForm


def add_model(request, given_form, given_url, name):
    if request.method == "POST":
        form = given_form(request.POST)
        if form.is_valid():
            form.save()
        else:
            raise Exception(f"Some Exception {form.errors}")
        return HttpResponse(f'OK, {name} was created')

    return render(request, 'index.html', {'form': given_form(), 'given_url': given_url})


def add_lesson(request):
    return add_model(request, LessonForm, 'add_lesson', 'lesson')


def add_student(request):
    return add_model(request, StudentForm, 'add_student', 'student')


def add_teacher(request):
    return add_model(request, TeacherForm, 'add_teacher', 'teacher')
