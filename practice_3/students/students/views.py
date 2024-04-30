from django.http import HttpResponse
from django.shortcuts import render, redirect
from students import models, forms


def add_student(request):
    if request.method == 'POST':
        form = forms.StudentForm(request.POST)
        if form.is_valid():
            form.save()  # Save the data to the database
            
        return HttpResponse('OK')
    else:
        form = forms.StudentForm()
        students = models.Student.objects.all()
    
    return render(request, 'students/student_list.html', {'students': students, 'form': form})