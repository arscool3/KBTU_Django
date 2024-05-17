from django.shortcuts import render

def list(request):
    students = ['Yera', 'Sala', 'Morti', 'Noname', 'Who']
    return render(request, 'list.html', {"students" : students})