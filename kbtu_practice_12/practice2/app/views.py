import dataclasses

from django.http import HttpResponse
from django.shortcuts import render

studentsList = [
    'Timur',
    'Azamat',
    'Dias',
]

teachers = [
    'Aibek',
    'Arslan',
    'Saidy',
]

@dataclasses.dataclass
class Student:
    name: str
    age: int
    sex: str
    teacher: str


students = [

]

for index, (element1, element2) in enumerate(zip(studentsList, teachers)):
    st = Student(name=f'{element1}', age = 18, sex = 'male', teacher=f'{element2}')
    students.append(st)


def view(request):
    return render(request, 'index.html', {'students': students})