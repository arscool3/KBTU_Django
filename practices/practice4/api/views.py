from django.shortcuts import render,redirect
from .models import Student, Faculty
from .forms import StudentForm


def stipendia_students_view(request):
    stipendia_students = Student.stipendiaManager.get_students_by_stipendia()
    print(stipendia_students)
    return render(request, 'base.html', {'stipendia_students': stipendia_students})

def non_stipendia_students_view(request):
    non_stipendia_students = Student.stipendiaManager.get_students_by_nonstipendia()
    return render(request, 'base.html', {'non_stipendia_students': non_stipendia_students})

def fit_students_view(request):
    fit = Faculty.objects.get(name='FIT')
    fit_students = Student.facultyManager.get_students_of_fit(fit)
    print(fit_students)
    return render(request, 'base.html', {'fit_students': fit_students})


def bs_students_view(request):
    bs = Faculty.objects.get(name='BS')
    bs_students = Student.facultyManager.get_students_of_bs(bs)
    return render(request, 'base.html', {'bs_students': bs_students})

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
