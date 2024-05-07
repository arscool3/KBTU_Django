from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import *
@login_required(login_url='/app/auth/sign_in/')
def create_education(request):
    if request.method == 'POST':
        form = EducationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/app/create_education/')  
    else:
        form = EducationForm()

    return render(request, 'create_education.html', {'form': form})

@login_required(login_url='/app/auth/sign_in/')
def create_country(request):
    if request.method == 'POST':
        form = CountryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/app/create_country/')  
    else:
        form = CountryForm()

    return render(request, 'create_country.html', {'form': form})

@login_required(login_url='/app/auth/sign_in/')
def create_city(request):
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/app/create_city/')  
    else:
        form = CityForm()

    return render(request, 'create_city.html', {'form': form})

@login_required(login_url='/app/auth/sign_in/')
def create_foreign_language(request):
    if request.method == 'POST':
        form = ForeignLanguageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/app/create_foreign_language/') 
    else:
        form = ForeignLanguageForm()

    return render(request, 'create_foreign_language.html', {'form': form})

@login_required(login_url='/app/auth/sign_in/')
def create_resume_employment_type(request):
    if request.method == 'POST':
        form = ResumeEmploymentTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/app/create_resume_employment_type/')  
    else:
        form = ResumeEmploymentTypeForm()

    return render(request, 'create_resume_employment_type.html', {'form': form})

@login_required(login_url='/app/auth/sign_in/')
def create_employment_type(request):
    if request.method == 'POST':
        form = EmploymentTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/app/create_employment_type/')  
    else:
        form = EmploymentTypeForm()

    return render(request, 'create_resume_employment_type.html', {'form': form})


@login_required(login_url='/app/auth/sign_in/')
def create_working_history(request):
    if request.method == 'POST':
        form = WorkingHistoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/app/create_working_history/') 
    else:
        form = WorkingHistoryForm()

    return render(request, 'create_working_history.html', {'form': form})

@login_required(login_url='/app/auth/sign_in/')
def create_resume(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/app/create_resume/')  
        else:
            print('Form errors:', form.errors)
    else:
        form = ResumeForm()

    return render(request, 'create_resume.html', {'form': form})

@login_required(login_url='/app/auth/sign_in/')
def get_resumes(request):
    resumes = Resume.objects.all()
    return render(request, 'resume_list.html', {'resumes': resumes})

@login_required(login_url='/app/auth/sign_in/')
@api_view(['GET'])
def get_resume_by_id(request, resume_id):
    resume = get_object_or_404(Resume, pk=resume_id)
    serializer = ResumeSerializer(resume)
    return Response(serializer.data)
    return render(request, 'resume.html', {'resume': resume})

@login_required(login_url='/app/auth/sign_in/')
def get_all_countries(request):
    countries = Country.objects.all()
    return render(request, 'country_list.html', {'countries': countries})

@login_required(login_url='/app/auth/sign_in/')
def get_country_by_id(request, country_id):
    country = get_object_or_404(Country, pk=country_id)
    return render(request, 'country_detail.html', {'country': country})

@login_required(login_url='/app/auth/sign_in/')
def get_all_working_histories(request):
    working_histories = WorkingHistory.objects.all()
    return render(request, 'working_history_list.html', {'working_histories': working_histories})

@login_required(login_url='/app/auth/sign_in/')
def get_working_history_by_id(request, working_history_id):
    working_history = get_object_or_404(WorkingHistory, pk=working_history_id)
    return render(request, 'wh.html', {'working_history': working_history})

@login_required(login_url='/app/auth/sign_in/')
def delete_country(request, country_id):
    if request.method == 'POST':
        form = CountryDeleteForm(request.POST)
        if form.is_valid():
            country_id = form.cleaned_data['country_id']
            country = Country.objects.get(pk=country_id)
            country.delete()
            return redirect('/') 
    else:
        initial_data = {'country_id': country_id}
        form = CountryDeleteForm(initial=initial_data)
    return render(request, 'delete_country.html', {'form': form})

@login_required(login_url='/app/auth/sign_in/')
def update_country(request, country_id):
    country = Country.objects.get(pk=country_id)
    if request.method == 'POST':
        form = CountryUpdateForm(request.POST, instance=country)
        if form.is_valid():
            form.save()
            return redirect('update_country.html') 
    else:
        form = CountryUpdateForm(instance=country)
    return render(request, 'update_country.html', {'form': form})

@login_required(login_url='/app/auth/sign_in/')
def country_list_query(request):
    query = request.GET.get('q')
    countries = None  
    if query:
        countries = Country.objects.filter(name__icontains=query)

    return render(request, 'country_query.html', {'countries': countries})