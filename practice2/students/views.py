from django.shortcuts import render
from django.shortcuts import render


def student_list(request):
    students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
    return render(request, 'student_list.html', {'students': students})
