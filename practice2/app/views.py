from django.shortcuts import render

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
    return render(request, 'index.html', {'students': students})
