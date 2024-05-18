from django.shortcuts import get_object_or_404, render, redirect
from rest_framework import viewsets
from rest_framework import permissions

from .tasks import send_booking_confirmation
from .permissions import IsAdminUserOrReadOnly, IsBookingClient, IsManager, IsManagerOrReadOnly
from .models import Manager, Barber, Client, Barbershop, BookingRequest, ApplicationRequest, User
from .serializers import ManagerSerializer, BarberSerializer, ClientSerializer, BarbershopSerializer, BookingRequestSerializer, ApplicationRequestSerializer, UserSerializer
from rest_framework.permissions import IsAdminUser

from django.shortcuts import render
from .models import Manager, Barbershop, User

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
from django.contrib import messages


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('homepage')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

def homepage(request):
    return render(request, 'homepage.html')

def managers_list(request):
    managers = Manager.objects.all()
    return render(request, 'managers_list.html', {'managers': managers})

def barbers_list(request):
    barbers = Barber.objects.all()
    return render(request, 'barbers_list.html', {'barbers': barbers})

def barbershops_list(request):
    barbershops = Barbershop.objects.all()
    return render(request, 'barbershops_list.html', {'barbershops': barbershops})

def users_list(request):
    users = User.objects.all()
    return render(request, 'users_list.html', {'users': users})

def user_detail(request, user_id):
    try:
        user = get_object_or_404(User, id=user_id)
        return render(request, 'user_detail.html', {'user': user})
    except: 
        return render(request, '404.html')


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]


class ManagerViewSet(viewsets.ModelViewSet):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer
    permission_classes = [permissions.IsAuthenticated, IsManagerOrReadOnly | IsAdminUser]

class BarberViewSet(viewsets.ModelViewSet):
    queryset = Barber.objects.all()
    serializer_class = BarberSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminUserOrReadOnly]

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminUserOrReadOnly]

class BarbershopViewSet(viewsets.ModelViewSet):
    queryset = Barbershop.objects.all()
    serializer_class = BarbershopSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminUserOrReadOnly]

class BookingRequestViewSet(viewsets.ModelViewSet):
    queryset = BookingRequest.objects.all()
    serializer_class = BookingRequestSerializer
    permission_classes = [IsBookingClient, IsManagerOrReadOnly]
    
    def perform_create(self, serializer):
        booking = serializer.save(client=self.request.user.client, status="pending")
        send_booking_confirmation.send(booking.client.user.email, booking.id)

class ApplicationRequestViewSet(viewsets.ModelViewSet):
    queryset = ApplicationRequest.objects.all()
    serializer_class = ApplicationRequestSerializer
    permission_classes = [permissions.IsAuthenticated, IsManager]
