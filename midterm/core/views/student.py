from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required, permission_required
from core.models import *
from core.forms import *



@login_required(login_url='login')
def get_all_students(request):
    if request.method == 'GET':
        students = Student.objects.all()
        return render(request, 'index.html', {
            'iterable_name': 'Student',
            'iterable': students
        })
    
# def enroll_to_course(request):
