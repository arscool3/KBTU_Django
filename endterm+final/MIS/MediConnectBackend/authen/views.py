from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .serializers import UserRegistrationSerializer
from django.contrib.auth import authenticate, login
from .serializers import UserLoginSerializer
from .models import Profile
from .serializers import ProfileSerializer

class ProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfileListView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class UserRegistrationView(generics.CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = UserRegistrationSerializer

    def get(self, request, *args, **kwargs):
        return Response({"message": "GET request received."}, status=status.HTTP_200_OK)


class UserLoginView(generics.CreateAPIView):
    serializer_class = UserLoginSerializer

    def get(self, request, *args, **kwargs):
        return Response({"message": "GET request received."}, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data.get('email')
        password = serializer.validated_data.get('password')

        try:
            profile = Profile.objects.get(email=email)
            if profile.password == password:
                return Response({"profile_id": profile.id}, status=status.HTTP_200_OK)
            else:
                return Response({"message": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED)
        except Profile.DoesNotExist:
            return Response({"message": "Invalid email."}, status=status.HTTP_401_UNAUTHORIZED)
