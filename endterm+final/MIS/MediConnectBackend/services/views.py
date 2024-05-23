from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.http import Http404
from .models import MedicalService, Specialty
from .serializers import MedicalServiceSerializer, SpecialtySerializer

class MedicalServiceListView(generics.ListAPIView):
    queryset = MedicalService.objects.all()
    serializer_class = MedicalServiceSerializer

class MedicalServiceDetailViewByName(APIView):
    def get(self, request):
        name = request.GET.get('name')
        try:
            service = MedicalService.objects.get(name=name)
            return Response({'name': service.name, 'specialty_name': service.specialty.name})
        except MedicalService.DoesNotExist:
            return Response({'error': 'Service not found'}, status=404)    
        
class SpecialtyListView(generics.ListAPIView):
    queryset = Specialty.objects.all()
    serializer_class = SpecialtySerializer