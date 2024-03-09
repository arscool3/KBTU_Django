from django.shortcuts import render

from coursera.models import Course


# Create your views here.

def get_courses(request):
    courses = Course.objects.all()
    return render(request, 'courses.html', {'courses': courses})
