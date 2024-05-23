from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User, UserProfile, Channel, Video, Comment, Like, Playlist, Subscription
from .serializers import RegistrationSerializer, LoginSerializer, UserSerializer, UserProfileSerializer, ChannelSerializer, VideoSerializer, CommentSerializer, LikeSerializer, PlaylistSerializer, SubscriptionSerializer


class RegistrationAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        serializer_data = request.data.get('user', {})
        serializer = self.serializer_class(request.user, data=serializer_data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserProfileRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserProfileSerializer

    def get_object(self):
        return self.request.user.userprofile

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.get_object())
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        serializer_data = request.data.get('userprofile', {})
        serializer = self.serializer_class(self.get_object(), data=serializer_data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class SeeChannelAPIView(generics.RetrieveAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer

    def get(self, request, *args, **kwargs):
        channel_id = kwargs.get('channel_id')
        channel = self.queryset.filter(id=channel_id).first()
        if not channel:
            return Response({'error': 'Channel not found'}, status=404)
        serializer = self.serializer_class(channel)
        return Response(serializer.data, status=200)
    
class AddCommentAPIView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CommentSerializer

    def post(self, request, *args, **kwargs):
        video_id = kwargs.get('video_id')
        video = Video.objects.filter(id=video_id).first()
        if not video:
            return Response({'error': 'Video not found'}, status=404)

        comment_data = {
            'video': video.id,
            'author': request.user.id,
            'comment': request.data.get('comment')
        }
        serializer = self.serializer_class(data=comment_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class SubscribeAPIView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SubscriptionSerializer

    def post(self, request, *args, **kwargs):
        channel_id = kwargs.get('channel_id')
        channel = Channel.objects.filter(id=channel_id).first()
        if not channel:
            return Response({'error': 'Channel not found'}, status=404)

        subscription_data = {
            'user': request.user.id,
            'channel': channel.id
        }
        serializer = self.serializer_class(data=subscription_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class VideoListCreateAPIView(generics.ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(channel=self.request.user.channel)


class VideoDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]



class PlaylistListCreateAPIView(generics.ListCreateAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PlaylistDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class LiveStreamAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        if not request.user.has_perm('youtube.start_live_stream'):
            return Response({"message": "You don't have permission to start a live stream."}, status=403)
        stream_title = request.data.get('title')
        if not stream_title:
            return Response({"message": "Stream title is required."}, status=400)
        return Response({"message": f"Live stream '{stream_title}' started successfully."}, status=200)