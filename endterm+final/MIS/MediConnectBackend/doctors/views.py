import datetime
from rest_framework import generics
from .models import Doctor, Appointment, Patient
from .serializers import EnhancedDoctorSerializer, AppointmentSerializer
from .permissions import IsCustomUserAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from services.models import Specialty
import pytz
from rest_framework.views import APIView
from django.http import JsonResponse, Http404
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import api_view, permission_classes
from .tasks import send_reminder_email

def get_profile_id_by_doctor_id(request, doctor_id):
    try:
        doctor = Doctor.objects.get(pk=doctor_id)
        return JsonResponse({'profile_id': doctor.profile.id}, status=200)
    except Doctor.DoesNotExist:
        return JsonResponse({'error': 'Doctor not found'}, status=404)


class DoctorListView(generics.ListAPIView):
    serializer_class = EnhancedDoctorSerializer

    def get_queryset(self):
        profile_id = self.request.query_params.get('profile')
        specialty_name = self.request.query_params.get('specialty')
        if profile_id is not None:
            return Doctor.objects.filter(profile__id=profile_id)
        elif specialty_name is not None:
            specialty = Specialty.objects.filter(name=specialty_name).first()
            if specialty is not None:
                return Doctor.objects.filter(specialty=specialty)
            else:
                return Doctor.objects.none()
        else:
            return Doctor.objects.all()
    

class DoctorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = EnhancedDoctorSerializer


class VerifyDoctorLicenseView(APIView):
    def post(self, request):
        profile_id = request.data.get('id')
        print(profile_id)
        
        try:
            doctor = Doctor.objects.get(profile_id=profile_id)
        except Doctor.DoesNotExist:
            return Response({'error': 'Doctor not found'}, status=status.HTTP_404_NOT_FOUND)
        
        request.data['license_status'] = 'Pending Verification'

        serializer = EnhancedDoctorSerializer(doctor, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class DoctorAppointmentListView(generics.ListCreateAPIView):
    serializer_class = AppointmentSerializer
    permission_classes = [IsCustomUserAuthenticated]

    def get_queryset(self):
        profile_id = self.kwargs['doctor_profile_id']
        doctor = Doctor.objects.filter(profile_id=profile_id)[0]
        return Appointment.objects.filter(doctor=doctor)
    
    def get_available_slots(self, doctor_id):
        doctor = Doctor.objects.get(pk=doctor_id)
        start_date = datetime.datetime.now().date() + datetime.timedelta(days=1)
        end_date = start_date + datetime.timedelta(days=7)
        appointments = Appointment.objects.filter(doctor=doctor, date_and_time__range=(start_date, end_date))
        available_slots = []
        while start_date <= end_date:
            if start_date.weekday() < 5:
                for hour in range(9, 18):
                    local_time = datetime.datetime.combine(start_date, datetime.time(hour))
                    local_timezone = pytz.timezone('Asia/Almaty')
                    utc_time = local_timezone.localize(local_time).astimezone(pytz.utc)
                    if not appointments.filter(date_and_time=utc_time).exists() and hour != 13:
                        available_slots.append(utc_time)
            start_date += datetime.timedelta(days=1)
        return available_slots
    
    def list(self, request, *args, **kwargs):
        profile_id = self.kwargs['doctor_profile_id']
        doctor = Doctor.objects.filter(profile_id=profile_id)[0]
        if 'slots' in request.query_params:
            available_slots = self.get_available_slots(doctor.id)
            return Response({'available_slots': available_slots})
        else:
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        appointment_data = request.data
        serializer = self.get_serializer(data=appointment_data)
        if serializer.is_valid():
            appointment = serializer.save()
            send_reminder_email.send(appointment.id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DoctorAppointmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [IsCustomUserAuthenticated]

    def get_object(self):
        if self.request.method in ['PUT', 'DELETE']:
            appointment_id = self.kwargs.get('pk')
            try:
                return Appointment.objects.get(pk=appointment_id)
            except Appointment.DoesNotExist:
                raise Http404("No Appointment matches the given query.")
        else:
            return super().get_object()

    def put(self, request, *args, **kwargs):
        appointment = self.get_object()
        serializer = self.get_serializer(appointment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class AppointmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [IsCustomUserAuthenticated]

class AppointmentUpdateGoogleMeetLinkView(APIView):
    def patch(self, request, pk):
        google_meet_link = request.data.get('google_meet_link')

        try:
            appointment = Appointment.objects.get(pk=pk)
            appointment.google_meet_link = google_meet_link
            appointment.save()
            return Response({'message': 'Google Meet link updated successfully'}, status=status.HTTP_200_OK)
        except Appointment.DoesNotExist:
            return Response({'error': 'Appointment not found'}, status=status.HTTP_404_NOT_FOUND)