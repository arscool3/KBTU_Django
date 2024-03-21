from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
student_list = [
    'gulim',
    'aru',
    'nurem',
    
]

def index(request):
    return render(request, "index.html", {
        'student_list': student_list,
    })