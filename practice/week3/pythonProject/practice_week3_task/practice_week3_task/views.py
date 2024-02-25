from django.shortcuts import render, redirect
from .forms import MyForm

def students_list(request):
    students = ['Ali Zhumataev', 'Ali Madiyar', 'Zhilkibaev Ernar', 'Mauletkhan Nurbek']
    return render(request, 'students_list.html', {'students': students})


def teachers_list(request):
    teachers = ['Bobur','Ali','Askar', 'Baisak', 'Pacman']
    return render(request, 'teachers_list.html', {'teachers': teachers})


def my_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            # Process the form data
            # For demonstration purposes, you can save the form data to the database here
            form.save()
            return redirect('my_template.html')
    else:
        form = MyForm()

    return render(request, 'my_template.html', {'form': form})
