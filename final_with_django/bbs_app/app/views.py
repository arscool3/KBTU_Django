from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets
from rest_framework import permissions

from .tasks import send_booking_confirmation
from .permissions import IsAdminUserOrReadOnly, IsBookingClient, IsManager, IsManagerOrReadOnly
from .models import Manager, Barber, Client, Barbershop, BookingRequest, ApplicationRequest, User
from .serializers import ManagerSerializer, BarberSerializer, ClientSerializer, BarbershopSerializer, BookingRequestSerializer, ApplicationRequestSerializer, UserSerializer
from rest_framework.permissions import IsAdminUser

from django.shortcuts import render
from .models import Manager, Barbershop, User

def homepage(request):
    return render(request, 'homepage.html')

def managers_list(request):
    managers = Manager.objects.all()
    return render(request, 'managers_list.html', {'managers': managers})

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
    permission_classes = [permissions.IsAuthenticated, IsBookingClient | IsManager]
    
    def perform_create(self, serializer):
        booking = serializer.save(client=self.request.user.client, status="pending")
        send_booking_confirmation.send(booking.client.user.email, booking.id)

class ApplicationRequestViewSet(viewsets.ModelViewSet):
    queryset = ApplicationRequest.objects.all()
    serializer_class = ApplicationRequestSerializer
    permission_classes = [permissions.IsAuthenticated, IsManager]
