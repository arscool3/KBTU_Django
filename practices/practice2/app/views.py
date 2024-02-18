from django.shortcuts import render

class Student:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

students = [
    Student(name='togzhan', age=19, sex='f'),
    Student(name='aizhan', age=15, sex='f'),
    Student(name='ernar', age=23, sex='m')
]

def view(request):
    return render(request, 'index.html', {'students': students})