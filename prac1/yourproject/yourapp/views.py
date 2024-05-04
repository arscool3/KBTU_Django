from django.shortcuts import render
from django.http import HttpResponse


student_list = [
    "student1",
    "student2",
    "student3",
    "student4",
    "student5",
    "student6",
    "student7",
]

def index(request):
    return render(request, "index.html", {
        'student_list': student_list
    })

def test(request, id):
    return HttpResponse(f"5 times id = {5 * id}")
