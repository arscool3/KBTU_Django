from django.shortcuts import render


def student_list_view(request):
    students = ['Dauren', 'Daulet', 'Adam', 'Eva']  # Sample student data
    return render(request, 'student_list.html', {'students': students})

