from .models import User
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

        fields = ['id', 'first_name', 'last_name', 'username', 'email', 'user_type', 'phone_number', 'password']
        extra_kwargs = {
            'password': {'write_only': True}  # for hiding password
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)

        if password is not None:
            instance.set_password(password)

        instance.save()
        return instance


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def get_token(cls, user):
        token = super().get_token(user)
        token['user_type'] = user.user_type

        return token
