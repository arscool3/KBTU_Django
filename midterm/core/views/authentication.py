from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, decorators, logout, forms
from django.http import JsonResponse
from core.forms import StudentRegistrationForm, InstructorRegistrationForm
import jwt

def register_student_view(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("/student/courses")
        else:
            raise Exception(f"some erros {form.errors}")
    return render(request, 'form.html', {
        'form_name': 'Register Student',
        'form': StudentRegistrationForm()
        })


def register_instructor_view(request):
    if request.method == 'POST':
        form = InstructorRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("OK")
        else:
            raise Exception(f"some erros {form.errors}")
    return render(request, 'form.html', {
        'form_name': 'Register Instructor',
        'form': InstructorRegistrationForm()
        })


@decorators.login_required(login_url='login')
def get_user(request):
    if request.user.is_authenticated:
        user = request.user
        return render(request, 'user.html', {'user': user})
    raise Exception(f"{request.user} is not authenticated")

def login_view(request):
    if request.method == 'POST':
        form = forms.AuthenticationForm(data=request.POST)
        if form.is_valid():
            try:
                user = authenticate(**form.cleaned_data)
                login(request, user)
                payload = {
                    'user_id': request.user.id
                }
                token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')
                return JsonResponse('token', token)
            except Exception:
                return HttpResponse("something is not ok")
        else:
            raise Exception(f"some erros {form.errors}")
    return render(request, 'form.html', {
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