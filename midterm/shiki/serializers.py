from rest_framework import serializers
from .models import Anime, Manga, LightNovel, Image, Genre, User, Profile

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

class AnimeSerializer(serializers.ModelSerializer):
    genre = GenreSerializer()

    class Meta:
        model = Anime
        fields = '__all__'

class MangaSerializer(serializers.ModelSerializer):
    genre = GenreSerializer()

    class Meta:
        model = Manga
        fields = '__all__'

class LightNovelSerializer(serializers.ModelSerializer):
    genre = GenreSerializer()

    class Meta:
        model = LightNovel
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'date_joined')

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = ('user', 'bio')
