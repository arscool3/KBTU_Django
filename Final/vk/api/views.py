from django.http import JsonResponse
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from app.models import Post, UserInfo, Image, Comment, Like, Group, Subscription
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.


class PostViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    lookup_field = 'id'

    @action(detail=True, methods=['get'])
    def postImages(self, request, id: int):
        imgs = ImageSerializer(Image.objects.getPostImage(id), many=True)
        return Response(imgs.data)

    @action(detail=True, methods=['get'])
    def likeAmount(self, request, id: int):
        return Response(Like.objects.filter(post=id).count())

    @action(detail=True, methods=['get'])
    def commentAmount(self, request, id: int):
        return Response(Comment.objects.filter(post=id).count())

    @action(detail=True, methods=['get'])
    def postComments(self, request, id: int):
        coms = CommentSerializer(Comment.objects.filter(post=id), many=True)
        return Response(coms.data)


class UserInfoViewSet(ModelViewSet):
    serializer_class = UserInfoSerializer
    queryset = UserInfo.objects.all()


class ImageViewSet(ModelViewSet):
    serializer_class = ImageSerializer
    queryset = Image.objects.all()


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class LikeViewSet(ModelViewSet):
    serializer_class = LikeSerializer
    queryset = Like.objects.all()



class GroupViewSet(ModelViewSet):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()


class SubscriptionViewSet(ModelViewSet):
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()


