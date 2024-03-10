from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Vacancy, Company, User, Resume, Response
from .forms import UserRegistrationForm, UserProfileForm, ResumeForm, ResponseForm

# GET Views
def home(request):
    return render(request, 'home.html')

def vacancy_list(request):
    vacancies = Vacancy.objects.all()
    return render(request, 'vacancy_list.html', {'vacancies': vacancies})

def vacancy_detail(request, vacancy_id):
    vacancy = get_object_or_404(Vacancy, pk=vacancy_id)
    return render(request, 'vacancy_detail.html', {'vacancy': vacancy})

def company_list(request):
    companies = Company.objects.all()
    return render(request, 'company_list.html', {'companies': companies})

@login_required
def user_profile(request):
    user = request.user
    return render(request, 'user_profile.html', {'user': user})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('user_profile')
    else:
        form = UserProfileForm(instance=request.user)
    return render(request, 'edit_profile.html', {'form': form})

# POST Views
def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def user_login(request):
    # Your login view logic here
    return render(request, 'registration/login.html')

@login_required
def create_resume(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST)
        if form.is_valid():
            resume = form.save(commit=False)
            resume.user = request.user
            resume.save()
            return redirect('user_profile')
    else:
        form = ResumeForm()
    return render(request, 'create_resume.html', {'form': form})

@login_required
def apply_to_vacancy(request, vacancy_id):
    vacancy = get_object_or_404(Vacancy, pk=vacancy_id)
    if request.method == 'POST':
        form = ResponseForm(request.POST)
        if form.is_valid():
            response = form.save(commit=False)
            response.vacancy = vacancy
            response.resume = request.user.resume
            response.save()
            return redirect('vacancy_detail', vacancy_id=vacancy_id)
    else:
        form = ResponseForm()
    return render(request, 'apply_to_vacancy.html', {'form': form, 'vacancy': vacancy})

@login_required
def save_vacancy(request, vacancy_id):
    vacancy = get_object_or_404(Vacancy, pk=vacancy_id)
    request.user.saved_vacancies.add(vacancy)
    return redirect('vacancy_detail', vacancy_id=vacancy_id)

@login_required
def edit_resume(request):
    resume = request.user.resume
    if request.method == 'POST':
        form = ResumeForm(request.POST, instance=resume)
        if form.is_valid():
            form.save()
            return redirect('user_profile')
    else:
        form = ResumeForm(instance=resume)
    return render(request, 'edit_resume.html', {'form': form})
