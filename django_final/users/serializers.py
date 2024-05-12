from rest_framework import serializers

from users import models


class CreateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields = ('id', 'first_name', 'last_name', 'email', 'password', )


class VerifyUserSerializer(serializers.Serializer):
    session_id = serializers.UUIDField()
    code = serializers.CharField(max_length=4)


class CreateTokenSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=128)


class GetUserSerializer(serializers.Serializer):
    access_token = serializers.CharField(max_length=255)


class UpdateUserSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()


class GetUserInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields = ('id', 'first_name', 'last_name', 'email', "user_type")
