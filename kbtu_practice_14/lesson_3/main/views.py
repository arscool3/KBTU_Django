import dataclasses

from django.http import HttpResponse
from django.shortcuts import render

students = [
    'arMan',
    'nurzHan',
    'mAnys',
]

teachers = [
    'boBUr',
    'mEls',
    'arsLan',
]

@dataclasses.dataclass
class Student:
    name: str
    age: int
    sex: str


students = [
    Student(name='aliYa', age=18, sex='female'),
    Student(name='asKar', age=19, sex='male'),
    Student(name='alEN', age=20, sex='male'),
]


def view(request):
    return render(request, 'index.html', {'students': students})
