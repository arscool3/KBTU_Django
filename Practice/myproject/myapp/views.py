from django.shortcuts import render

def student_list(request):
    students = ['Zhilkibaev Yernar', 'Ali Madiyar', 'Mauletkhan Nurbek', 'Zhumataev Ali', 'Eszhan Aliar','Saparov Aldiar', 'Dilda Ilyas', 'Mukhtarov Daniyal',]
    initial = request.GET.get('initial')
    filtered_students = []
    if initial:
        filtered_students = [student for student in students if initial.lower() in student.lower().split()[-1].lower()]
    else:
        filtered_students = students
    
    return render(request, 'student_list.html', {'students': filtered_students, 'initial': initial})
