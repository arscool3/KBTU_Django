from django.shortcuts import render


def student_list(request):
    students = ['Dias', 'Aibek', 'Alisa', 'Timur']
    return render(request, 'students_list.html', {'students': students})
