from django.contrib.auth import authenticate, login, decorators, logout, forms
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from coursera.forms import StudentRegistrationForm, CourseForm, InstructorForm, EnrollmentForm, ReviewForm, LessonForm
from coursera.models import *

from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from coursera.serializers import CourseSerializer


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_field = 'id'

    @action(detail=True, methods=['get'])
    def get_course(self, request, id: int):
        course = self.get_object()
        if course.prerequisite is not None:
            return Response("Course have prerequisite")
        return Response('Course does not have prerequisite')


@login_required(login_url='login')
def get_courses(request):
    courses = Course.objects.all()
    return render(request, 'courses.html', {'courses': courses})


@login_required(login_url='login')
def get_course_details(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'course_details.html', {'course': course})


@login_required(login_url='login')
@permission_required('coursera.add_course', login_url='login')
def create_course(request):
    return add_model(request, CourseForm, 'add_genre', 'genre')


@login_required(login_url='login')
@permission_required('coursera.add_enrollment', login_url='login')
def get_enrollments(request):
    student_id = request.GET.get('student_id')
    if student_id:
        enrollments = Enrollment.objects.get_enrollments_of_student(student_id)
        return render(request, 'enrollments.html', {'enrollments': enrollments})

    enrollments = Enrollment.objects.all()
    return render(request, 'enrollments.html', {'enrollments': enrollments})


@login_required(login_url='login')
def get_course_enrollments(request, course_id):
    enrollments = Enrollment.objects.get_enrollments_of_course(course_id)
    return render(request, 'enrollments.html', {'enrollments': enrollments})


@login_required(login_url='login')
def create_enrollment(request):
    return add_model(request, EnrollmentForm, 'add_enrollment', 'enrollment')


@login_required(login_url='login')
def get_instructors(request):
    instructors = Instructor.objects.all()
    return render(request, 'instructors.html', {'instructors': instructors})


@login_required(login_url='login')
def create_instructor(request):
    return add_model(request, InstructorForm, 'add_instructor', 'instructor')


@login_required(login_url='login')
def get_reviews(request):
    course_id = request.GET.get('course_id')
    if course_id:
        reviews = Review.objects.get_reviews(course_id)
        return render(request, 'reviews.html', {'reviews': reviews})

    reviews = Review.objects.all()
    return render(request, 'reviews.html', {'reviews': reviews})


@login_required(login_url='login')
def create_review(request):
    return add_model(request, ReviewForm, 'add_review', 'review')


@login_required(login_url='login')
def get_lessons(request):
    lessons = Lesson.objects.all()
    return render(request, 'lessons.html', {'lessons': lessons})


@login_required(login_url='login')
def create_lesson(request):
    return add_model(request, LessonForm, 'add_lesson', 'lesson')


@login_required(login_url='login')
def get_students(request):
    students = Student.objects.all()
    return render(request, 'students.html', {'students': students})


def add_model(request, given_form, given_url, name):
    if request.method == "POST":
        form = given_form(request.POST)
        if form.is_valid():
            form.save()
        else:
            raise Exception(f"Some Exception {form.errors}")
        return HttpResponse(f'OK, {name} was created')

    return render(request, 'index.html', {'form': given_form(), 'given_url': given_url})


def register_student(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']

            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            student = Student.objects.create(user=user)
            student.name = form.cleaned_data['username']
            student.email = form.cleaned_data['email']
            student.save()

            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = StudentRegistrationForm()
    return render(request, 'index.html', {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponse("You have logout")


def login_view(request):
    if request.method == 'POST':
        form = forms.AuthenticationForm(data=request.POST)
        if form.is_valid():
            try:
                user = authenticate(**form.cleaned_data)
                login(request, user)
                if next := request.GET.get("next"):
                    return redirect(next)
                return HttpResponse("everything is ok")
            except Exception:
                return HttpResponse("something is not ok")
        else:
            raise Exception(f"some erros {form.errors}")
    return render(request, 'index.html', {'form': forms.AuthenticationForm()})
