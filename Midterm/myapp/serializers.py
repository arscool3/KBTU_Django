from rest_framework import serializers
from .models import User, Category, Post, Comment, Like, Chat, Message


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'image']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    categories = CategorySerializer(many=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'description', 'author', 'image', 'categories', 'created_at']


class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'text', 'timestamp']


class LikeSerializer(serializers.ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = Like
        fields = ['id', 'post', 'author']


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ['id', 'title', 'members', 'created_at']


class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer()

    class Meta:
        model = Message
        fields = ['id', 'chat', 'sender', 'content', 'timestamp']
