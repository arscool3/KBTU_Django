from django.shortcuts import render

def student_list(request):
    students = ['Student1', 'Student2', 'Student3', 'Student4', 'Student5']
    return render(request, 'student_list.html', {"students" : students})

