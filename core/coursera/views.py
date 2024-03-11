from django.contrib.auth import authenticate, login, decorators, logout, forms
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

from coursera.forms import StudentRegistrationForm, CourseForm
from coursera.models import Course, Student


# Create your views here.

def get_courses(request):
    courses = Course.objects.all()
    return render(request, 'courses.html', {'courses': courses})


def create_course(request):
    return add_model(request, CourseForm, 'add_genre', 'genre')


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

            # Creating User instance with username and email
            user = User.objects.create(username=username, email=email)

            # Saving User instance
            user.save()

            # Now create the student linked to this user
            student = Student.objects.create(user=user)

            # Optionally, you can set other attributes of the Student model based on the form data
            student.name = form.cleaned_data['name']
            # Set other attributes if needed

            # Save the student instance
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
