from django.shortcuts import render

# Create your views here.

students = ["Yaslan", "Ersultan"]


def list_of_students(request):
    return render(request, 'index.html', {
        'students': students
    })
