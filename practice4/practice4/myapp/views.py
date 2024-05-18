from django.shortcuts import render, redirect

from django.db.models import Q
from django.http import HttpResponse

from myapp.models import Teacher,Course,Student
from .forms import TeacherForm
def get_teacher_by_name(request):
    teachers = Teacher.objects
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = TeacherForm()
        if name := request.GET.get('name'):
            teachers = teachers.filter(name=name.capitalize())
        teachers = teachers.all()
        return render(request, "main.html", {"iterable": teachers, "object": "teachers", 'form': form})