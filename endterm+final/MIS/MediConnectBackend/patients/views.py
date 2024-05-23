from rest_framework import generics, status
from .models import Patient, PatientMedicalRecord
from .serializers import PatientSerializer, PatientMedicalRecordSerializer
from doctors.serializers import AppointmentSerializer
from doctors.permissions import IsCustomUserAuthenticated
from doctors.models import Appointment
from rest_framework.response import Response
from rest_framework.views import APIView


class PatientListView(generics.ListAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class PatientDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class PatientMedicalRecordDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PatientMedicalRecord.objects.all()
    serializer_class = PatientMedicalRecordSerializer

class PatientAppointmentListView(generics.ListAPIView):
    serializer_class = AppointmentSerializer
    permission_classes = [IsCustomUserAuthenticated]

    def get_queryset(self):
        profile_id = self.kwargs['profile_id']
        patient = Patient.objects.filter(profile_id=profile_id)[0]
        return Appointment.objects.filter(patient=patient)
    
    
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class GetPatientIdByProfileIdView(APIView):
    def get(self, request, profile_id):
        try:
            patient = Patient.objects.get(profile_id=profile_id)
            return Response({'patient_id': patient.id}, status=status.HTTP_200_OK)
        except Patient.DoesNotExist:
            return Response({'error': 'Patient with the given profile ID does not exist'}, status=status.HTTP_404_NOT_FOUND)
