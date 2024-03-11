from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, get_user_model
from .models import Vacancy, Company, User, Resume
from .forms import UserProfileForm, UserRegistrationForm, UserLoginForm, ResumeForm, ResponseForm, ChangePasswordForm


# GET
def home(request):
    return render(request, 'home.html')


def vacancy_list(request):
    vacancies = Vacancy.objects.all()
    return render(request, 'vacancy_list.html', {'vacancies': vacancies})


def vacancy_detail(request, vacancy_id):
    vacancy = get_object_or_404(Vacancy, id=vacancy_id)
    return render(request, 'vacancy_detail.html', {'vacancy': vacancy})


def company_list(request):
    companies = Company.objects.all()
    return render(request, 'company_list.html', {'companies': companies})


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

            messages.success(request, 'Profile and password successfully updated.')
            return redirect('user_profile', user_id=user.id)
        else:
            messages.error(request, 'Error updating profile or password. Please check your input.')
    else:
        profile_form = UserProfileForm(instance=user)
        password_form = ChangePasswordForm()

    return render(request, 'edit_profile.html', {'user': user, 'profile_form': profile_form, 'password_form': password_form})



# POST
def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались. Теперь вы можете войти в систему.')
            return redirect('login')
        else:
            messages.error(request, 'Ошибка при регистрации. Пожалуйста, проверьте введенные данные.')
    else:
        form = UserRegistrationForm()

    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            print(user)  # Добавьте эту строку для отладки
            if user is not None:
                login(request, user)
                messages.success(request, 'Вы успешно вошли в систему.')
                return redirect('vacancy_list')
            else:
                messages.error(request, 'Неверное имя пользователя или пароль.')
        else:
            messages.error(request, 'Ошибка при входе. Пожалуйста, проверьте введенные данные.')
    else:
        form = UserLoginForm()

    return render(request, 'login.html', {'form': form})


def create_resume(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST)
        if form.is_valid():
            resume = form.save(commit=False)
            resume.user = get_user_model().objects.get(id=request.user.id)  # Прямое присвоение пользователя
            resume.save()
            messages.success(request, 'Резюме успешно создано.')
            return redirect('user_profile', user_id=request.user.id)
        else:
            messages.error(request, 'Ошибка при создании резюме. Пожалуйста, проверьте введенные данные.')
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
            messages.success(request, 'Отклик успешно отправлен.')
            return redirect('home')
        else:
            messages.error(request, 'Ошибка при отправке отклика. Пожалуйста, проверьте введенные данные.')
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
            messages.success(request, 'Резюме успешно обновлено.')
            return redirect('user_profile', user_id=request.user.id)
        else:
            messages.error(request, 'Ошибка при обновлении резюме. Пожалуйста, проверьте введенные данные.')
    else:
        form = ResumeForm(instance=resume)

    return render(request, 'edit_resume.html', {'form': form, 'resume': resume})
