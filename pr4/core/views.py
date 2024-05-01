from django.shortcuts import render

from KBTU_Django.pr4.core.models import Lesson, Student


# Create your views here.
def get_lessons(request):
    lessons = Lesson.objects.get_pp1().all()
    return render(request, 'lesson.html', {'lessons': lessons})


def get_students(request):
    students = Student.objects.get_by_name().all()
    return render(request, 'index.html', {'students': students})