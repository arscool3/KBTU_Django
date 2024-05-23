from django.urls import path
from .views import (
    RegistrationAPIView, LoginAPIView, UserRetrieveUpdateAPIView,
    UserProfileRetrieveUpdateAPIView, SeeChannelAPIView, AddCommentAPIView,
    SubscribeAPIView, VideoListCreateAPIView, VideoDetailAPIView,
    PlaylistListCreateAPIView, PlaylistDetailAPIView, LiveStreamAPIView
)

urlpatterns = [
    path('register/', RegistrationAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('user/', UserRetrieveUpdateAPIView.as_view(), name='user'),
    path('userprofile/', UserProfileRetrieveUpdateAPIView.as_view(), name='userprofile'),
    path('channel/<int:channel_id>/', SeeChannelAPIView.as_view(), name='seeChannel'),
    path('video/<int:video_id>/comment/', AddCommentAPIView.as_view(), name='addComment'),
    path('channel/<int:channel_id>/subscribe/', SubscribeAPIView.as_view(), name='subscribe'),
    path('videos/', VideoListCreateAPIView.as_view(), name='video-list-create'),
    path('videos/<int:pk>/', VideoDetailAPIView.as_view(), name='video-detail'),
    path('playlists/', PlaylistListCreateAPIView.as_view(), name='playlist-list-create'),
    path('playlists/<int:pk>/', PlaylistDetailAPIView.as_view(), name='playlist-detail'),
    path('live/', LiveStreamAPIView.as_view(), name='live-stream'),
]
