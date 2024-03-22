from django.shortcuts import render

# Create your views here.
def view_students(request):
    students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
    return render(request, 'studentsapp/students_list.html', {'students': students})
