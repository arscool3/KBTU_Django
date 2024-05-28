from django.shortcuts import render

# Create your views here.
def student_list(request):
    students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
    return render(request, 'myapp/templates/student_list.html', {'students': students})