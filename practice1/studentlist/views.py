from django.shortcuts import render

# Create your views here.
def student_list(request):
    students = [
        {'first_name': 'John', 'last_name': 'Doe'},
        {'first_name': 'Jane', 'last_name': 'Smith'}
    ]

    return render(request, 'studentlist/student_list.html', {'students': students})
