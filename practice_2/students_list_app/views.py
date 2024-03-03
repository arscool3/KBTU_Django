from django.shortcuts import render
from students_list_app.models import student_list

# Create your views here.
def showList(request):
    return render(request, "index.html", {
            'student_list': student_list
    })