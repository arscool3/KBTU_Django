from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            # Assuming you have a Student model with a 'name' field
            Student.objects.create(name=form.cleaned_data['name'])
            return redirect('students_list')  # Redirect to a new URL
    else:
        form = StudentForm()
    return render(request, 'students/add_student.html', {'form': form})
