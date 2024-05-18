from django_filters import rest_framework as filters
from .models import Room

class RoomFilter(filters.FilterSet):
    hotel_name = filters.CharFilter(field_name='hotel__name', lookup_expr='icontains')

    class Meta:
        model = Room
        fields = ['hotel_name', 'type', 'available']