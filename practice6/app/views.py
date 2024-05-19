from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.shortcuts import get_object_or_404
from .models import Vacancy, Company, User, Resume
from .serializers import (
    VacancySerializer, CompanySerializer, UserSerializer, ResumeSerializer,
    UserProfileSerializer, ChangePasswordSerializer, ResponseSerializer
)
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse

# GET
@api_view(['GET'])
def home(request):
    return Response({'message': 'Welcome to the home page'})


class VacancyListCreateAPIView(generics.ListCreateAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class VacancyRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CompanyListAPIView(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [permissions.AllowAny]


class CompanyDetailAPIView(generics.RetrieveAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [permissions.AllowAny]


class UserRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


class ChangePasswordAPIView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = ChangePasswordSerializer
    permission_classes = [permissions.IsAuthenticated]


class ResumeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ResumeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    permission_classes = [permissions.IsAuthenticated]


# POST
class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreationForm

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save(commit=False)
            user.password = make_password(serializer.validated_data.get('password'))
            user.save()
            return JsonResponse({'message': 'User registered successfully'})
        return JsonResponse(serializer.errors, status=400)


@api_view(['POST'])
def user_login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return Response({'message': 'User logged in successfully'})
    else:
        return Response({'message': 'Invalid credentials'}, status=400)


@api_view(['POST'])
def create_resume(request):
    serializer = ResumeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response({'message': 'Resume created successfully'})
    return Response(serializer.errors, status=400)


@api_view(['POST'])
def apply_for_vacancy(request, vacancy_id):
    vacancy = get_object_or_404(Vacancy, id=vacancy_id)

    serializer = ResponseSerializer(data=request.data)
    if serializer.is_valid():
        response = serializer.save(vacancy=vacancy, resume=request.user.resume)
        return Response({'message': 'Application submitted successfully'})
    return Response(serializer.errors, status=400)
