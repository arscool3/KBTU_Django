# views.py
from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student

def student_list(request):
    students = Student.objects.all()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')  # Redirect to the same page after form submission
    else:
        form = StudentForm()
    return render(request, 'student_list.html', {'students': students, 'form': form})