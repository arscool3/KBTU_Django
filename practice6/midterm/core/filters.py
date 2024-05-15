import django_filters
from .models import CounterStrikeGame

class CounterStrikeGameFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = CounterStrikeGame
        fields = ['name']
