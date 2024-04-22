from rest_framework.generics import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action

from core.models import Weather
from core.serializers import WeatherSerializer


class WeatherViewSet(ModelViewSet):
    serializer_class = WeatherSerializer
    queryset = Weather.objects.all()
    lookup_field = 'id'

    @action(detail=True, methods=["get"])
    def umbrella(self, request, id: int):
        weather = self.get_object()
        if weather.temp < -5 or weather.description == 'rainy':
            return Response("You need an umbrella")
        return Response("You don't need an umbrella")



# ApiView -> allowed methods (get, post, put, delete, ...)
# define always

# GenericApiView -> ApiView + serializer_class, queryset
# YourView(GenericApiView, UpdateModelMixin)

# Create Read Update Delete
# ModelViewSet -> GenericApiView, Get, Post, Put, Delete
# define queryset, serializer, lookup_field ?


# Router instead of path('weather/.....) -> SimpleRouter
