from django.shortcuts import render

def student_list(request):
    students = ['Zhilkibaev Yernar', 'Ali Madiyar', 'Mauletkhan Nurbek', 'Zhumataev Ali', 'Eszhan Aliar','Saparov Aldiar', 'Dilda Ilyas', 'Mukhtarov Daniyal',]

    return render(request, 'student_list.html', {'students': students})
