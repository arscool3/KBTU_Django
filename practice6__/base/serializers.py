from rest_framework import serializers
from .models import Article, Profile, Topic, ReadingList, Comment, Follow, Like
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    
    class Meta:
        model = Profile
        fields = '__all__'

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'

class ArticleSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    topic = TopicSerializer()
    
    class Meta:
        model = Article
        fields = '__all__'

class ReadingListSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    articles = ArticleSerializer(many=True)
    
    class Meta:
        model = ReadingList
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    article = ArticleSerializer()
    
    class Meta:
        model = Comment
        fields = '__all__'

class FollowSerializer(serializers.ModelSerializer):
    follower = UserSerializer()
    followed_user = UserSerializer()
    
    class Meta:
        model = Follow
        fields = '__all__'

class LikeSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    article = ArticleSerializer()
    
    class Meta:
        model = Like
        fields = '__all__'
