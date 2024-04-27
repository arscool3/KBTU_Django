from django.shortcuts import render

def student_list(request):
    students = ['Alice', 'Bob', 'Charlie', 'David','Arsen','Beks']
    return render(request, 'myapp/student_list.html', {'students': students})
