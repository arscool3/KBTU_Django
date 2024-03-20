from django.shortcuts import render

def view(request):
    students = [
        {'name': 'John', 'age': 20, 'sex': 'Male'},
        {'name': 'Alice', 'age': 22, 'sex': 'Female'},
        {'name': 'Bob', 'age': 21, 'sex': 'Male'},
    ]
    return render(request, 'index.html', {'students': students})
