from django.shortcuts import render,redirect
from .forms import StudentForm
class Student:
    def __init__(self, FirstName, LastName, StudentID, Faculty):
        self.FirstName = FirstName
        self.LastName = LastName
        self.StudentID = StudentID
        self.Faculty = Faculty

students = [
    Student(FirstName='Aruzhan', LastName='Orynbay', StudentID='21B030707', Faculty='School of Information Technologies and Engineering'),
    Student(FirstName='Aisha', LastName='Ospanova', StudentID='21B030706', Faculty='School of Information Technologies and Engineering'),
    Student(FirstName='Madina', LastName='Suleimenova', StudentID='21B050607', Faculty='School of Information Technologies and Engineering'),
]


def view(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        students.append(Student(
            FirstName=form.cleaned_data['FirstName'],
            LastName=form.cleaned_data['LastName'],
            StudentID=form.cleaned_data['StudentID'],
            Faculty=form.cleaned_data['Faculty']
        ))
        return redirect('index')  # Redirect to the same page after adding the student

    context = {
        'students': students,
        'form': form,
    }
    return render(request, 'index.html', context)


