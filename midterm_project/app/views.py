from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required

from .forms import CourseForm, LessonForm
from .models import UserProfile, Course, Lesson, Enrollment, Instructor, Quiz


@login_required
def list_courses(request):
    query = request.GET.get('query')
    courses = Course.objects.all()

    if query:
        courses = courses.filter(title__icontains=query)

    sort_by = request.GET.get('sort_by')
    if sort_by == 'created_at':
        courses = courses.order_by('-created_at')

    return render(request, 'courses_list.html', {'courses': courses})


@login_required
def course_detail(request, course_id):
    course = Course.objects.get(id=course_id)
    return render(request, 'course_detail.html', {'course': course})


@login_required
def lesson_detail(request, lesson_id):
    lesson = Lesson.objects.get(id=lesson_id)
    return render(request, 'lesson_detail.html', {'lesson': lesson})


@login_required
def user_profile(request):
    profile = UserProfile.objects.get(user=request.user)
    return render(request, 'profile_detail.html', {'profile': profile})


# POST запросы

@login_required
def enrollment_form(request, course_id):
    if request.method == 'POST':
        course = Course.objects.get(id=course_id)
        Enrollment.objects.create(user=request.user, course=course)
        return HttpResponse("You have been enrolled successfully!")
    else:
        return render(request, 'enrollment_form.html', {'course_id': course_id})


@login_required
def create_course(request):
    if request.method == 'POST':
        instructor = Instructor.objects.get(user=request.user)
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.instructor = instructor
            course.save()
            return HttpResponse("Course created successfully!")
    else:
        # Отображение формы для создания курса
        return render(request, 'create_course_form.html')


@login_required
def create_lesson(request, course_id):
    if request.method == 'POST':
        course = Course.objects.get(id=course_id)
        form = LessonForm(request.POST)
        if form.is_valid():
            lesson = form.save(commit=False)
            lesson.course = course
            lesson.save()
            return HttpResponse("Lesson created successfully!")
    else:
        return render(request, 'create_lesson_form.html', {'course_id': course_id})


@login_required
def take_quiz(request, quiz_id):
    if request.method == 'POST':
        return HttpResponse("Quiz results submitted!")
    else:
        quiz = Quiz.objects.get(id=quiz_id)
        return render(request, 'quiz_detail.html', {'quiz': quiz})
