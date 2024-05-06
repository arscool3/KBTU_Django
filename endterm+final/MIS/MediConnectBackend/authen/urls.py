from django.urls import path
from .views import UserRegistrationView, UserLoginView, ProfileDetailView, ProfileListView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profiles/', ProfileListView.as_view(), name='profiles'),
    path('profiles/<int:pk>/', ProfileDetailView.as_view(), name='profile-detail'),
]
