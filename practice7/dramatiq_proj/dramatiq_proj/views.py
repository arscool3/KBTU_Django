# views.py
from rest_framework import viewsets
from .models import Feedback
from .serializers import FeedbackSerializer
from .tasks import process_feedback
class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer


    def perform_create(self, serializer):
        instance = serializer.save()
        process_feedback.send(instance.id)