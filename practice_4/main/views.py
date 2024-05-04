from django.shortcuts import render
from django.http import HttpResponse
from main.models import Student, Teacher, Course, University
from main.forms import StudentForm, TeacherForm, CourseForm, UniversityForm
# Create your views here.

def get_univesities(request):
    universities = University.objects
    universities = universities.all()
    return render(request, "index.html", {"universities": universities})

def get_budget(request):
    universities = University.objects.get_budget()
    return render(request, "index.html", {"universities": universities})

def get_language(request):
    universities = University.objects.get_lang()
    return render(request, "index.html", {"universities": universities})

def get_gpa(request):
    students = Student.objects.get_gpa()
    return render(request, "student.html", {"students": students})

def get_dorms(request):
    students = Student.objects.get_dorms()
    return render(request, "student.html", {"students": students})


def add_model(request, given_form, given_url, name):
    if request.method == "POST":
        form = given_form(request.POST)
        if form.is_valid():
            form.save()
        else:
            raise Exception(f"Some Exception {form.errors}")
        return HttpResponse(f'OK, {name} was created')

    return render(request, 'create.html', {'form': given_form(), 'given_url': given_url})

def add_course(request):
    return add_model(request, CourseForm, 'add_course', 'course')


def add_student(request):
    return add_model(request, StudentForm, 'add_student', 'student')


def add_teacher(request):
    return add_model(request, TeacherForm, 'add_teacher', 'teacher')

def add_university(request):
    return add_model(request, UniversityForm, 'add_university', 'university')