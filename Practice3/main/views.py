import dataclasses

from django.http import HttpResponse
from django.shortcuts import render

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
