
from rest_framework import serializers
from .models import User, Bookmark
from recipe.serializers import RecipeSerializer


class BookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = ['user', 'recipe']


class UserSerializer(serializers.ModelSerializer):
    saved_recipes = RecipeSerializer(read_only=True, many=True)

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'username', 'password', 'saved_recipes', 'photo')
        read_only_fields = ['id']

    def create(self, validated_data):
        user = User.objects.create(email=validated_data['email'],
                                   first_name=validated_data['first_name'],
                                   last_name=validated_data['last_name'],
                                   )
        user.set_password(validated_data['password'])
        user.save()
        return user
