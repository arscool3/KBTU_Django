from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Artifact
from .serializers import ArtifactSerializer

class ArtifactListCreate(generics.ListCreateAPIView):
    queryset = Artifact.objects.all()
    serializer_class = ArtifactSerializer

class ArtifactRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artifact.objects.all()
    serializer_class = ArtifactSerializer