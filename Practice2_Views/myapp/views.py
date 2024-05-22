from django.shortcuts import render


def get_students(request):
    students = ['Timur', 'Dias', 'Aibek', 'Nurali', 'Arslan', 'Azamat']
    return render(request, 'students.html', {'students': students})