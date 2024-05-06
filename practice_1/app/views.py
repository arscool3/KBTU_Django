from django.shortcuts import render
from django.http import HttpResponse
import datetime


students = [
    'student 1',
    'student 2',
    'student 3',
]

title = 'Students List'

time_now = datetime.datetime.now()


def get_students(request):
    return render(request, 'index.html', {
        'header_title': title,
        'students_list': students,
        'time': time_now,
    })
