from rest_framework import viewsets
from comments.serializers import CommentSerializer
from comments.models import Comment

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer