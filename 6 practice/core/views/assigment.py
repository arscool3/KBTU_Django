from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required, permission_classes
from core.models import *
from core.forms import AssignmentForm
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


@api_view(['GET'])
@login_required(login_url='login')
def get_student_assignements(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            student = Student.objects.get(user=request.user)
            courses = student.courses
            
            return render(request, 'course.html', {'courses': student.courses})



@api_view(['POST'])
@permission_classes((IsAuthenticated,))
# @permission_required('can_add_courses')
def instructor_create_assignment(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = AssignmentForm(request.POST)
            if form.is_valid():
                form.save()
                
            else:
                raise Exception(f"Some Exception {form.errors}")
            return redirect("/course/all")
        else: 
            return HttpResponse("you need to login")
    
    return render(request, 'form.html', {
        'form_name': 'Add Course',
        'form': AssignmentForm()
        })