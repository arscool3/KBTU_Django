
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render

from core.models import Teacher, Admin, Student, Book
from core.forms import BookForm, StudentForm, TeacherForm, AdminForm


def add_model(request, given_form, given_url, name):
    if request.method == "POST":
        form = given_form(request.POST)
        if form.is_valid():
            form.save()
        else:
            # raise Exception(f"Some Exception {form.errors}")
            return HttpResponse(f'Fill the form correctly, please!')
        return HttpResponse(f'OK, {name} was created')
    #if name == 'book':


    return render(request, 'index.html', {'form': given_form(), 'given_url': given_url})


def add_book(request):
    return add_model(request, BookForm, 'add_Book', 'Book')


def add_student(request):
    return add_model(request, StudentForm, 'add_student', 'student')


def add_teacher(request):
    return add_model(request, TeacherForm, 'add_teacher', 'teacher')

def add_admin(request):
    return add_model(request, AdminForm, 'add_admin', 'admin')

    

#-----------------------------

def get_student_by_name(request):
    students = Student.objects
    if name := request.GET.get('name'):
        students = students.filter(name=name.capitalize())
    students = students.all()
    return render(request, "index.html", {"iterable": students, "object":   "students"})


def get_books(request):
    books = Book.objects
    if student_name := request.GET.get('student_name'):
        books = books.filter(student__name=student_name.capitalize())
    books = books.all()
    return render(request, 'index.html', {"iterable": books, "object": "Books"})


def get_teacher(request):
    teachers = Teacher.objects
    if teacher_name := request.GET.get('teacher_name'):
        teachers = teachers.filter(teacher__name=teacher_name.capitalize())
    teachers = teachers.all()
    return render(request, 'index.html', {"iterable": teachers, "object": "Teachers"})

    