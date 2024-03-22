from django.shortcuts import render

# Create your views here.


def student_list(request):
    students = ['Sula', 'Baxa', 'Toxa', 'Ers', 'Emma']
    return render(request, 'index.html', {'students': students})
