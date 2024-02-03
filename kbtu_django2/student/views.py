from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
student_list = [
    'ali',
    'ali2',
    'ali3',
    
]

def index(request):
    return render(request, "index.html", {
        'student_list': student_list,
    })