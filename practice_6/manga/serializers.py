from rest_framework import serializers
from .models import Manga, Chapter, Page, Review, UserProfile

class MangaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manga
        fields = '__all__'

class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = '__all__'

class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'
