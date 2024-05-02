from django.shortcuts import render
# Create your views here.

def student_list(request):
    students = [
        {'name': 'Darkhan', 'age' : '20', 'grade' : 'A+'},
        {'name': 'Aidar', 'age': '5', 'grade': 'C-'},
    ]
    return render(request, 'students_list.html', {'students' : students})