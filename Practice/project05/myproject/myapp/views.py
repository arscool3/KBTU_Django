from rest_framework import viewsets
from .models import Test
from .serializers import TestSerializer

class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
