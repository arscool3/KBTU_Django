from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import InstructorForm, MemberForm, GymForm, MembershipForm, EquipmentForm, WorkoutForm, InstructorFilterForm, GymFilterForm
from .models import Instructor, Gym
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm


# Create your views here.


def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

# views.py



def add_instructor(request):
    if request.method == 'POST':
        form = InstructorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('instructorpage')  # Replace 'instructor_list' with the URL name for listing instructors
    else:
        form = InstructorForm()
    return render(request, 'main/add_instructor.html', {'form': form})

def add_member(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('memberpage')  # Replace 'member_list' with the URL name for listing members
    else:
        form = MemberForm()
    return render(request, 'main/add_member.html', {'form': form})

def add_gym(request):
    if request.method == 'POST':
        form = GymForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gym_list')  # Replace 'gym_list' with the URL name for listing gyms
    else:
        form = GymForm()
    return render(request, 'main/add_gym.html', {'form': form})

def add_membership(request):
    if request.method == 'POST':
        form = MembershipForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('membership_list')  # Replace 'membership_list' with the URL name for listing memberships
    else:
        form = MembershipForm()
    return render(request, 'main/add_membership.html', {'form': form})

def add_equipment(request):
    if request.method == 'POST':
        form = EquipmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('equipment_list')  # Replace 'equipment_list' with the URL name for listing equipment
    else:
        form = EquipmentForm()
    return render(request, 'main/add_equipment.html', {'form': form})

def add_workout(request):
    if request.method == 'POST':
        form = WorkoutForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('workout_list')  # Replace 'workout_list' with the URL name for listing workouts
    else:
        form = WorkoutForm()
    return render(request, 'main/add_workout.html', {'form': form})


def filter_instructors(request):
    if request.method == 'GET':
        form = InstructorFilterForm(request.GET)
        if form.is_valid():
            specialization = form.cleaned_data.get('specialization')
            gender = form.cleaned_data.get('gender')
            instructors = Instructor.objects.all()
            if specialization:
                instructors = instructors.filter(specialization=specialization)
            if gender:
                instructors = instructors.filter(gender=gender)

            # Фильтрация по букве "А"
            instructors = instructors.filter(instructor_name__istartswith='A')

            return render(request, 'main/instructor_list.html', {'instructors': instructors, 'form': form})
    else:
        form = InstructorFilterForm()
    return render(request, 'main/filter_instructors.html', {'form': form})


def filter_gyms(request):
    if request.method == 'GET':
        form = GymFilterForm(request.GET)
        if form.is_valid():
            location = form.cleaned_data.get('location')
            gyms = Gym.objects.all()
            if location:
                gyms = gyms.filter(location=location)
            return render(request, 'main/gym_list.html', {'gyms': gyms, 'form': form})
    else:
        form = GymFilterForm()
    return render(request, 'main/filter_gyms.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('mainpage')
    else:
        form = UserCreationForm()
    return render(request, 'main/register.html', {'form': form})

@login_required
def custom_logout(request):
    logout(request)
    return redirect('')


from django.http import JsonResponse
from .models import Instructor, Member, Gym, Membership, Equipment, Workout

def get_instructors(request):
    instructors = Instructor.objects.all()
    data = [{'instructor_id': instructor.instructor_id, 'instructor_name': instructor.instructor_name,
             'specialization': instructor.specialization, 'gender': instructor.gender} for instructor in instructors]
    return JsonResponse(data, safe=False)

def get_members(request):
    members = Member.objects.all()
    data = [{'member_id': member.member_id, 'name': member.name,
             'age': member.age, 'membership_type': member.membership_type} for member in members]
    return JsonResponse(data, safe=False)

def get_gyms(request):
    gyms = Gym.objects.all()
    data = [{'gym_id': gym.gym_id, 'gym_name': gym.gym_name,
             'location': gym.location} for gym in gyms]
    return JsonResponse(data, safe=False)

def get_memberships(request):
    memberships = Membership.objects.all()
    data = [{'membership_id': membership.membership_id, 'name': membership.name,
             'price': membership.price} for membership in memberships]
    return JsonResponse(data, safe=False)

def get_equipment(request):
    equipment = Equipment.objects.all()
    data = [{'equipment_id': item.equipment_id, 'name': item.name,
             'quantity': item.quantity} for item in equipment]
    return JsonResponse(data, safe=False)

def get_workouts(request):
    workouts = Workout.objects.all()
    data = [{'workout_id': workout.workout_id, 'name': workout.name,
             'description': workout.description} for workout in workouts]
    return JsonResponse(data, safe=False)


from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Instructor

def show_instructor(request, instructor_id):
    instructor = get_object_or_404(Instructor, pk=instructor_id)
    data = {
        'instructor_id': instructor.instructor_id,
        'instructor_name': instructor.instructor_name,
        'specialization': instructor.specialization,
        'gender': instructor.gender
    }
    return JsonResponse(data)

from django.http import JsonResponse
from .models import Instructor

def delete_instructor(request, instructor_id):
    instructor = Instructor.objects.filter(pk=instructor_id)
    if instructor.exists():
        instructor.delete()
        return JsonResponse({'message': 'Instructor deleted successfully'})
    else:
        return JsonResponse({'message': 'Instructor not found'}, status=404)



