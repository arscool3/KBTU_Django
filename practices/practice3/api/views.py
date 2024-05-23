from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student
def studentVIew(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = StudentForm()
    return render(request, 'student.html', {'form': form})

def home(request):
    students = Student.objects.all()
    return render(request, 'list.html', {"students" : students})
