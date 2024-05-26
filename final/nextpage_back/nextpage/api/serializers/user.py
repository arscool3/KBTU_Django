from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        return user


class UserUpdatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'first_name', 'last_name', 'email',)
        read_only_fields = ('id', 'username',)