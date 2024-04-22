from .models import Profile, Topic, Article, ReadingList, Comment, Follow, Like
from django.contrib.auth.models import User
from rest_framework import serializers

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'user', 'bio']
        read_only_fields = ['user']

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ['id', 'name']

class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    topic = serializers.PrimaryKeyRelatedField(queryset=Topic.objects.all())

    class Meta:
        model = Article
        fields = ['id', 'title', 'author', 'short_description', 'topic', 'body', 'date_created']
        read_only_fields = ['author', 'date_created']

class ReadingListSerializer(serializers.ModelSerializer):
    articles = serializers.PrimaryKeyRelatedField(queryset=Article.objects.all())

    class Meta:
        model = ReadingList
        fields = ['id', 'profile', 'articles']

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    article = serializers.PrimaryKeyRelatedField(queryset=Article.objects.all())

    class Meta:
        model = Comment
        fields = ['id', 'article', 'user', 'body', 'date_created']
        read_only_fields = ['user', 'date_created']

class FollowSerializer(serializers.ModelSerializer):
    follower = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    followed_user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Follow
        fields = ['id', 'follower', 'followed_user']

class LikeSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    article = serializers.PrimaryKeyRelatedField(queryset=Article.objects.all())

    class Meta:
        model = Like
        fields = ['id', 'user', 'article']
