from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import
from myapp.serializers import *
# Create your views here.

class get_users(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
    queryset = User.objects.all()

class create_user(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
    def perform_create(self, serializer):
        name = self.request.data.get("name")
        login = self.request.data.get("login")
        age = self.request.data.get("age")
        serializer.save(name=name, login=login, age=age)

class delete_user(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
    lookup_url_kwarg = "user_id"

    def get_queryset(self):
        return User.objects.filter(id = self.kwargs.get('user_id'))

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

    def perform_destroy(self, instance):
        instance.delete()

