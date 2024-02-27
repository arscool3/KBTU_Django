from django.shortcuts import render

from app.models import Student, Lesson


def get_students(request):
    students = Student.objects.get_students_only_from_course_3().get_only_arslan().all()
    # SELECT * From Students where course = '3' and name = 'Arslan'
    return render(request, 'index.html', {'students': students})

def get_lessons(request):
    lessons = Lesson.objects.get_today_lessons_by_teacher(request.GET['teacher'])
    return render(request, 'lesson.html', {'lessons': lessons})

# /lessons/?teacher=Arslan