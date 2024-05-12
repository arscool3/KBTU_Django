from django.shortcuts import render
from rest_framework import generics
from .models import Location, Tour, Review, Request, Rating
from .permissions import IsOwnerOrReadOnly, IsAdminOrReadOnly
from .serializers import LocationSerializer, TourSerializer, ReviewSerializer, RequestSerializer, UserSerializer, \
    RatingSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny
from django.contrib.auth.models import User


# Create your views here.

# list of Locations
class LocationAPIView(generics.ListAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = (IsOwnerOrReadOnly,)


# Location detail
class LocationAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = (IsOwnerOrReadOnly,)


# list of tours
class TourAPIView(generics.ListAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer
    permission_classes = (IsOwnerOrReadOnly,)


# tour detail
class TourAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer
    permission_classes = (IsOwnerOrReadOnly,)


# list of review
class ReviewAPIView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (IsOwnerOrReadOnly,)


# create review
class ReviewCreateAPIView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (IsOwnerOrReadOnly,)


# review detail
class ReviewAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class RequestAPICreate(generics.CreateAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class RegistrationAPICreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class RatingAPIView(generics.ListAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class RatingCreateAPIView(generics.CreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = (IsOwnerOrReadOnly,)


# review detail
class RatingAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = (IsOwnerOrReadOnly,)
