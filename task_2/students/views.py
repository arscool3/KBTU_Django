from django.shortcuts import render

from .models import Student

def student_list(request):
    students = [
        {'name': 'Nursultan', 'age': 20},
        {'name': 'Arsen', 'age': 21},
        {'name': 'Kazakh', 'age': 22}
    ]
    return render(request, 'students/student_list.html', {'students': students})