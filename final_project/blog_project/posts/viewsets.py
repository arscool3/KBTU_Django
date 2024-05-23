from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Category, Post
from .serializers import CategorySerializer, PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @action(detail=True, methods=['post'])
    def publish(self, request, pk=None):

        post = self.get_object()
        post.publish() 
        post.save()
        return Response({"status": "post published"})

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @action(detail=True, methods=['get'], url_path='post-count')
    def post_count(self, request, pk=None):
        category = self.get_object()
        count = category.post_count()  
        return Response({'post_count': count})