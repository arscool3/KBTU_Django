# serializers.py
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from .models import User, Link, Click, Category, Tag, LinkUsage

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Use a default value for the email if it's not provided
        email = validated_data.get('email', '')
        user = User.objects.create_user(validated_data['username'], email, validated_data['password'])
        return user

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        
        # Add custom claims
        token['username'] = user.username
        token['email'] = user.email
        token['isAdminUser'] = user.is_staff  # Add isAdminUser field
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        
        # Add custom response data here
        data.update({'user': {
            'id': self.user.id,
            'username': self.user.username,
            'email': self.user.email,
            'isAdminUser': self.user.is_staff,  # Include isAdminUser in response data
        }})
        
        return data


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

class CustomTokenRefreshSerializer(TokenRefreshSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        
        # Decode the access token to get user information
        refresh_token = attrs['refresh']
        refresh = RefreshToken(refresh_token)
        
        user_id = refresh['user_id']
        user_instance = User.objects.get(id=user_id)
        
        # Generate new tokens
        new_refresh = str(refresh)
        new_access = str(refresh.access_token)

        # Add custom response data
        data.update({
            'access': new_access,  # Include new access token in the response
            'refresh': new_refresh,  # Include new refresh token in the response
            'user': {
                'id': user_instance.id,
                'username': user_instance.username,
                'email': user_instance.email,
                'isAdminUser': user_instance.is_staff
            }
        })
        
        return data
    
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ['id', 'url', 'title', 'description', 'category', 'tags', 'created_by']

class ClickSerializer(serializers.ModelSerializer):
    class Meta:
        model = Click
        fields = '__all__'

class LinkUsageSerializer(serializers.ModelSerializer):
    class Meta:
        model = LinkUsage
        fields = '__all__'
