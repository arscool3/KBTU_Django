from django.shortcuts import render
from django.http import HttpResponse


todo_list = [
    'brush_teeth',
    'shower',
    'coffee',
    'sleep',
]

def index(request):
    return render(request, "index.html", {
        'todo_list': todo_list,
    })


def test(request, id):
    return HttpResponse(f"5 times id is {id * 5}!")

def students_list(request):
    students = [
        {'name': 'Darkhan', 'age': 20, 'grade': 'A'},
        {'name': 'Aidar', 'age': 23, 'grade': 'C'},
    ]
    return render(request, 'students.html', {'students' : students})
