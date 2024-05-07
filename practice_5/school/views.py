from datetime import datetime

from django.shortcuts import render, redirect
from .models import Course, Student, Enrollment, Teacher
from .forms import StudentForm, TeacherForm, CourseForm, EnrollmentForm
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@require_http_methods(["POST", "GET"])
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            return JsonResponse({"message": "Student added", "student_id": student.id})
    else:
        form = StudentForm()
    return render(request, 'add_student.html', {'form': form})

@csrf_exempt
@require_http_methods(["POST", "GET"])
def add_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            teacher = form.save()
            return JsonResponse({"message": "Teacher added", "teacher_id": teacher.id})
    else:
        form = TeacherForm()
    return render(request, 'add_teacher.html', {'form': form})

@csrf_exempt
@require_http_methods(["POST", "GET"])
def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save()
            return JsonResponse({"message": "Course added", "course_id": course.id})
    else:
        form = CourseForm()
    return render(request, 'add_course.html', {'form': form})

@csrf_exempt
@require_http_methods(["POST", "GET"])
def enroll_student(request):
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            enrollment = form.save(commit=False)
            enrollment.date_joined = datetime.now()  # Set the enrollment date to now
            enrollment.save()
            return JsonResponse({"message": "Enrollment successful"})
    else:
        form = EnrollmentForm()
    return render(request, 'enroll_student.html', {'form': form})

# Existing GET methods
@require_http_methods(["GET"])
def get_student(request, student_id):
    student = Student.objects.get(id=student_id)
    return render(request, 'student_detail.html', {'student': student})


@require_http_methods(["GET"])
def list_courses(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})


# New GET methods
@require_http_methods(["GET"])
def get_course(request, course_id):
    course = Course.objects.get(id=course_id)
    return render(request, 'course_detail.html', {'course': course})


@require_http_methods(["GET"])
def get_teacher(request, teacher_id):
    teacher = Teacher.objects.get(id=teacher_id)
    return render(request, 'teacher_detail.html', {'teacher': teacher})
