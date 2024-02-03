from django.shortcuts import render


students = ["Yersultan", "Nursultan", "Aisultan", "Sultan"]


def list_of_students(request):
    return render(request, 'index.html', {
        'students': students
    })