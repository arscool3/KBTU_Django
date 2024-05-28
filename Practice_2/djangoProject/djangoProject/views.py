from django.shortcuts import render

def student_list(request):
    students = ['Ayan', 'Arsen', 'Arman', 'Almas']
    return render(request, 'student_list.html', {'students': students})