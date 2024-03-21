import dataclasses

from django.http import HttpResponse
from django.shortcuts import render
from .forms import StudentForm

@dataclasses.dataclass
class Student:
    name: str
    age: int
    course: int


students = [
    Student(name='Anar', age=18, course=2),
    Student(name='Dauren', age=19, course=2),
    Student(name='Daniyar', age=20, course=3),
]


def view(request):
    return render(request, 'index.html', {'students': students})

def view2(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        course = request.POST.get("course")
        students.append(Student(name = name, age = age, course = course))
        print('i am here')
    studentform = StudentForm()
    return render(request, 'index2.html', {'form': studentform})
