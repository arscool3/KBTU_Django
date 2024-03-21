from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required, permission_required
from core.models import *
from core.forms import *

def get_all_courses(request):
    if request.method == 'GET':
        courses = Course.objects.all()
        return render(request, 'index.html', {
            'iterable_name': 'Course',
            'iterable': courses})


@login_required(login_url='login')
def student_courses(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            student = Student.objects.get(user=request.user)
            return render(request, 'index.html', {
                'iterable_name': 'Course',
                'iterable': student.courses})
        else: 
            return HttpResponse("you need to login")
        
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = AddCourseForm(request.POST)
            if form.is_valid():
                selected_courses = form.cleaned_data['courses']
                user = request.user
                student = Student.objects.get(user=user)
                student.courses.add(selected_courses)
                return redirect('/student/courses') 
        else:
            form = AddCourseForm()
    return render(request, 'form_choice.html', {'form': AddCourseForm()})

@login_required(login_url='login')
def instructor_courses(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            instructor = Instructor.objects.get(user=request.user)
            courses = Course.objects.get_course_by_instructor(instructor=instructor)
            return render(request, 'index.html', {
                'iterable_name': 'Course',
                'iterable': courses})
        else: 
            return HttpResponse("you need to login")
    
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = CourseForm(request.POST)
            if form.is_valid():
                form.save()
                
            else:
                raise Exception(f"Some Exception {form.errors}")
            return redirect("/course/all")
        else: 
            return HttpResponse("you need to login")
    
    return render(request, 'form.html', {
        'form_name': 'Add Course',
        'form': CourseForm()
        })
    