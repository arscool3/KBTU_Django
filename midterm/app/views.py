from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, get_user_model
from .models import Vacancy, Company, User, Resume
from .forms import UserProfileForm, UserRegistrationForm, UserLoginForm, ResumeForm, ResponseForm, ChangePasswordForm, \
    VacancyFilterForm


# GET
def home(request):
    return render(request, 'home.html')


def vacancy_list(request):
    vacancies = Vacancy.objects.all()
    vacancy_filter_form = VacancyFilterForm(request.GET)

    if vacancy_filter_form.is_valid():
        skills = vacancy_filter_form.cleaned_data.get('skills')
        if skills:
            skills_list = [skill.strip() for skill in skills.split(',')]
            vacancies = vacancies.filter(skills__name__in=skills_list)

    return render(
        request,
        'vacancy_list.html',
        {'vacancies': vacancies, 'vacancy_filter_form': vacancy_filter_form})


def vacancy_detail(request, vacancy_id):
    vacancy = get_object_or_404(Vacancy.objects.prefetch_related('skills', 'company'), id=vacancy_id)
    return render(request, 'vacancy_detail.html', {'vacancy': vacancy})

def company_list(request):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    selected_letter = request.GET.get('letter', '')

    if selected_letter and selected_letter.upper() not in alphabet:
        messages.error(request, 'Invalid letter selected.')
        return redirect('company_list')

    companies = Company.objects.all()

    if selected_letter:
        companies = companies.filter(name__istartswith=selected_letter)

    return render(request, 'company_list.html', {'companies': companies, 'alphabet': alphabet,
                                                 'selected_letter': selected_letter})


def user_profile(request, user_id):
    user = User.objects.get(id=user_id)
    return render(request, 'user_profile.html', {'user': user})


@login_required
def edit_profile(request, user_id):
    user = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, instance=user)
        password_form = ChangePasswordForm(request.POST)

        if profile_form.is_valid() and password_form.is_valid():
            profile_form.save()
            new_password = password_form.cleaned_data['new_password1']
            user.set_password(new_password)
            user.save()

            messages.success(request, 'The profile and password have been successfully updated.')
            user = User.objects.get(id=user_id)
            return redirect('user_profile', user_id=user.id)
        else:
            messages.error(request, 'An error occurred when updating the profile or password. Please check the '
                                    'entered data.')
    else:
        profile_form = UserProfileForm(instance=user)
        password_form = ChangePasswordForm()

    return render(request, 'edit_profile.html',
                  {'user': user, 'profile_form': profile_form, 'password_form': password_form})

# POST
def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully registered. You can now log in.')
            return redirect('login')
        else:
            messages.error(request, 'Error during registration. Please check the entered data.')
    else:
        form = UserRegistrationForm()

    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        print(form.errors)
        if form.is_valid():
            try:
                user = authenticate(**form.cleaned_data)
                print(user)
                login(request, user)
                if next := request.GET.get("next"):
                    return redirect(next)
                return redirect('vacancy_list')
            except Exception:
                return HttpResponse("something is not ok")
        else:
            print("error")
            messages.error(request, 'Error logging in. Please check the entered data.')
    else:
        print("lsfkndjnfjd")
        form = UserLoginForm()

    return render(request, 'login.html', {'form': form})


def create_resume(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST)
        if form.is_valid():
            resume = form.save(commit=False)
            resume.user = request.user
            resume.save()
            messages.success(request, 'The resume has been successfully created.')
            return redirect('user_profile', user_id=request.user.id)
        else:
            messages.error(request, 'An error occurred when creating a resume. Please check the entered data.')
    else:
        form = ResumeForm()

    return render(request, 'create_resume.html', {'form': form})


def apply_for_vacancy(request, vacancy_id):
    vacancy = get_object_or_404(Vacancy, id=vacancy_id)

    if request.method == 'POST':
        form = ResponseForm(request.POST)
        if form.is_valid():
            response = form.save(commit=False)
            response.vacancy = vacancy
            response.resume = request.user.resume
            response.save()
            messages.success(request, 'The response has been sent successfully.')
            return redirect('home')
        else:
            messages.error(request, 'An error occurred when sending the response. Please check the entered data.')
    else:
        form = ResponseForm()

    return render(request, 'apply_for_vacancy.html', {'form': form, 'vacancy': vacancy})


# def save_vacancy(request, vacancy_id):
#     vacancy = get_object_or_404(Vacancy, id=vacancy_id)
#
#     saved_vacancy, created = SavedVacancy.objects.get_or_create(user=request.user, vacancy=vacancy)
#
#     if created:
#         messages.success(request, 'Вакансия сохранена.')
#     else:
#         messages.info(request, 'Вы уже сохраняли эту вакансию.')
#
#     return redirect('home')
#

def edit_resume(request, resume_id):
    resume = get_object_or_404(Resume, id=resume_id)

    if request.method == 'POST':
        form = ResumeForm(request.POST, instance=resume)
        if form.is_valid():
            form.save()
            messages.success(request, 'The resume has been successfully updated.')
            return redirect('user_profile', user_id=request.user.id)
        else:
            messages.error(request, 'An error occurred when updating the resume. Please check the entered data.')
    else:
        form = ResumeForm(instance=resume)

    return render(request, 'edit_resume.html', {'form': form, 'resume': resume})
