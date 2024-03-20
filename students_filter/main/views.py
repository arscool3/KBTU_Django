from django.shortcuts import render
from .models import Student


def student_list(request):
    students = Student.objects.all()
    return render(request, 'sindex.html', {'students': students})


def index(request):
    # Create three instances of the Student class
    student1 = Student(name="John Doe", age=20, email="john@example.com")
    student2 = Student(name="Jane Smith", age=22, email="jane@example.com")
    student3 = Student(name="Michael Brown", age=21, email="michael@example.com")

    # Save the instances to the database (if necessary)
    student1.save()
    student2.save()
    student3.save()

    # Query all students from the database
    students = Student.objects.all()

    return render(request, 'main/index.html', {'students': students})
