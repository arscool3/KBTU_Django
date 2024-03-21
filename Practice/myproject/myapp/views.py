from django.shortcuts import render

def student_list(request):
    students = ['Zhilkibaev Yernar', 'Ali Madiyar', 'Mauletkhan Nurbek', 'Zhumataev Ali', 'Eszhan Aliar','Saparov Aldiar', 'Dilda Ilyas', 'Mukhtarov Daniyal',]
    modified_students = []
    for student in students:
        if student == 'Dilda Ilyas' or student == 'Mukhtarov Daniyal':
            modified_students.append('Student not found')
        else:
            modified_students.append(student)
    
    return render(request, 'student_list.html', {'students': modified_students})
