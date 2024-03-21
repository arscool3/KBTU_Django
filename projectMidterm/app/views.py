from django.shortcuts import render, redirect, HttpResponse
from .forms import WorkoutFilterByTrainerForm, WorkoutFilterByTypeForm
from .models import Workout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Member, Trainer, Workout, MembershipPlan
from django.contrib.auth import authenticate, login, logout, forms, decorators

def register_view(request):
    if request.method == 'POST':
        form = forms.UserCreationForm(request.POST)
        
    else:
        form = forms.UserCreationForm()
    
    return render(request, 'register.html', {'form': form})


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


@decorators.login_required(login_url='login')
def filter_workouts_by_trainer(request):
    form = WorkoutFilterByTrainerForm(request.GET or None)
    workouts = []

    if form.is_valid():
        workouts = form.filter_workouts()

    return render(request, 'workouts_filtered.html', {'form': form, 'workouts': workouts})

@decorators.login_required(login_url='login')
def filter_workouts_by_type(request):
    form = WorkoutFilterByTypeForm(request.GET or None)
    workouts = []

    if form.is_valid():
        workouts = form.filter_workouts()

    return render(request, 'workouts_filtered.html', {'form': form, 'workouts': workouts})

@decorators.login_required(login_url='login')
def get_all_members(request):
    members = Member.objects.all()
    data = [{'id': member.id, 'name': member.name} for member in members]
    return JsonResponse(data, safe=False)

@decorators.login_required(login_url='login')
def get_member_details(request, id):
    member = Member.objects.get(pk=id)
    data = {'id': member.id, 'name': member.name, 'age': member.age, 'address': member.address}  # Add more fields as needed
    return JsonResponse(data)


@csrf_exempt
def add_member(request):
    if request.method == 'POST':
        data = request.POST
        member = Member.objects.create(name=data['name'], age=data['age'], address=data['address'])  # Add more fields as needed
        return JsonResponse({'id': member.id, 'name': member.name, 'age': member.age, 'address': member.address}, status=201)
    return JsonResponse({'error': 'Invalid request'}, status=400)


def get_all_trainers(request):
    trainers = Trainer.objects.all()
    data = [{'id': trainer.id, 'name': trainer.name} for trainer in trainers]
    return JsonResponse(data, safe=False)


def get_trainer_details(request, id):
    trainer = Trainer.objects.get(pk=id)
    data = {'id': trainer.id, 'name': trainer.name, 'specialty': trainer.specialty}  # Add more fields as needed
    return JsonResponse(data)


@csrf_exempt
def add_trainer(request):
    if request.method == 'POST':
        data = request.POST
        trainer = Trainer.objects.create(name=data['name'], specialty=data['specialty'])  # Add more fields as needed
        return JsonResponse({'id': trainer.id, 'name': trainer.name, 'specialty': trainer.specialty}, status=201)
    return JsonResponse({'error': 'Invalid request'}, status=400)


def get_all_workouts(request):
    workouts = Workout.objects.all()
    data = [{'id': workout.id, 'name': workout.name, 'type': workout.type} for workout in workouts]
    return JsonResponse(data, safe=False)


def get_workout_details(request, id):
    workout = Workout.objects.get(pk=id)
    data = {'id': workout.id, 'name': workout.name, 'type': workout.type, 'trainer_id': workout.trainer_id}  # Add more fields as needed
    return JsonResponse(data)


@csrf_exempt
def add_workout(request):
    if request.method == 'POST':
        data = request.POST
        workout = Workout.objects.create(name=data['name'], type=data['type'], trainer_id=data['trainer_id'])  # Add more fields as needed
        return JsonResponse({'id': workout.id, 'name': workout.name, 'type': workout.type, 'trainer_id': workout.trainer_id}, status=201)
    return JsonResponse({'error': 'Invalid request'}, status=400)

def get_all_membership_plans(request):
    membership_plans = MembershipPlan.objects.all()
    data = [{'id': plan.id, 'name': plan.name, 'price': plan.price} for plan in membership_plans]
    return JsonResponse(data, safe=False)

def get_membership_plan_details(request, id):
    membership_plan = MembershipPlan.objects.get(pk=id)
    data = {'id': membership_plan.id, 'name': membership_plan.name, 'price': membership_plan.price, 'duration_months': membership_plan.duration_months}  # Add more fields as needed
    return JsonResponse(data)

@csrf_exempt
def add_membership_plan(request):
    if request.method == 'POST':
        data = request.POST
        plan = MembershipPlan.objects.create(name=data['name'], price=data['price'], duration_months=data['duration_months'])  # Add more fields as needed
        return JsonResponse({'id': plan.id, 'name': plan.name, 'price': plan.price, 'duration_months': plan.duration_months}, status=201)
    return JsonResponse({'error': 'Invalid request'}, status=400)
