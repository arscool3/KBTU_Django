from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, decorators, logout, forms
from core.forms import StudentRegistrationForm, InstructorRegistrationForm
from rest_framework.decorators import api_view, permission_classes
from core.models import Role
from rest_framework.permissions import AllowAny, IsAuthenticated

def register_student_view(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = Role.STUDENT.name
            user.save()
            return redirect("/student/courses")
        else:
            raise Exception(f"some erros {form.errors}")
    return render(request, 'authorization.html', {
        'form_name': 'Register Student',
        'form': StudentRegistrationForm()
        })


@api_view(['GET'])
def sign_up_choice(request):
    return render(request, 'sign_up.html')


def register_instructor_view(request):
    if request.method == 'POST':
        form = InstructorRegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = Role.INSTRUCTOR.name
            user.save()
            return redirect("/instructor/courses")
        else:
            raise Exception(f"some erros {form.errors}")
    return render(request, 'authorization.html', {
        'form_name': 'Register Instructor',
        'form': InstructorRegistrationForm()
        })


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user(request):
    if request.user.is_authenticated:
        user = request.user
        return render(request, 'user.html', {'user': user})
    raise Exception(f"{request.user} is not authenticated")


@api_view(['POST'])
def login_view(request):
    if request.method == 'POST':
        form = forms.AuthenticationForm(data=request.POST)
        if form.is_valid():
            try:
                user = authenticate(**form.cleaned_data)
                login(request, user)
                return redirect("/course/all")
            except Exception:
                return HttpResponse("something is not ok")
        else:
            raise Exception(f"some erros {form.errors}")
    return render(request, 'authorization.html', {
        'form_name': 'Authentication',
        'form': forms.AuthenticationForm()})


@decorators.login_required(login_url='login')
def check_view(request):
    if request.user.is_authenticated:
        return HttpResponse(f"{request.user} is authenticated")
    raise Exception(f"{request.user} is not authenticated")


def logout_view(request):
    logout(request)
    return redirect('/login')