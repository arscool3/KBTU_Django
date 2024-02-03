from django.shortcuts import render


def students_list(request):
    students = ['Ali Zhumataev', 'Ali Madiyar', 'Zhilkibaev Ernar', 'Mauletkhan Nurbek']
    return render(request, 'students_list.html', {'students': students})

