from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions

from .tasks import send_booking_confirmation
from .permissions import IsAdminUserOrReadOnly, IsBookingClient, IsManager, IsManagerOrReadOnly
from .models import Manager, Barber, Client, Barbershop, BookingRequest, ApplicationRequest, User
from .serializers import ManagerSerializer, BarberSerializer, ClientSerializer, BarbershopSerializer, BookingRequestSerializer, ApplicationRequestSerializer, UserSerializer
from rest_framework.permissions import IsAdminUser

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
    
class BookingModelViewSet(viewsets.ModelViewSet):
    queryset = BookingRequest.objects.all()
    serializer_class = BookingRequestSerializer
    permission_classes = [permissions.IsAuthenticated, IsBookingClient]

    # Custom action to handle listing bookings
    def list_bookings(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return render(request, "bookings_list.html", context={"bookings": serializer.data})

    # Override the list method to use custom action
    def list(self, request, *args, **kwargs):
        return self.list_bookings(request)

class ApplicationRequestViewSet(viewsets.ModelViewSet):
    queryset = ApplicationRequest.objects.all()
    serializer_class = ApplicationRequestSerializer
    permission_classes = [permissions.IsAuthenticated, IsManager]
