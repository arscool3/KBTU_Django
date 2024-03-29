import django_filters
from blogApi.models import post
class post_filter(django_filters.FilterSet):
    class Meta:
        model = post.Post
        fields = ['date', 'category']