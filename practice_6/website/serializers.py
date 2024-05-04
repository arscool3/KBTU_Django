from rest_framework import serializers
from .models import Novel, UserProfile, Chapter, Review, Bookmark

class NovelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Novel
        fields = ['id', 'title', 'author', 'summary', 'publish_date', 'cover_image']

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['user', 'bio', 'profile_picture']

class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = ['novel', 'title', 'content', 'chapter_number']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['novel', 'user', 'rating', 'comment', 'date_posted']

class BookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = ['user', 'novel', 'chapter']
