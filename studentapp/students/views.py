from django.shortcuts import render
from django.http import HttpResponse


student_list = [
    'name',
    'Arsen',
    'name2',
]

def index(request):
    return render(request, "index.html", {
        'student_list': student_list,
    })


def stuName(request, id):
    return HttpResponse(f"{student_list[id]}")