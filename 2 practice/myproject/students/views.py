from django.shortcuts import render

# Create your views here.
def students_list(request):
    students = ['Amirkhan', 'Serikbay', 'Arsen', 'Nusip']
    return render(request, 'students/students_list.html', {'students': students})
