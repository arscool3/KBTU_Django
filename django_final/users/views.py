from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from users import services, serializers
from users.models import User


class UserViewSet(ViewSet):
    user_services: services.UserServicesInterface = services.UserServicesV1()

    authentication_classes = (JWTAuthentication, )

    @swagger_auto_schema(
        request_body=serializers.CreateUserSerializer(),
        responses={
            status.HTTP_201_CREATED: serializers.CreateUserSerializer(),
            status.HTTP_400_BAD_REQUEST: serializers.VerifyUserSerializer(),
        }
    )
    def create_user(self, request, *args, **kwargs):
        serializer = serializers.CreateUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        session_id = self.user_services.create_user(data=serializer.validated_data)

        return Response({'session_id': session_id}, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(request_body=serializers.VerifyUserSerializer)
    def verify_user(self, request, *args, **kwargs):
        serializer = serializers.VerifyUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = self.user_services.verify_user(data=serializer.validated_data)
        if user is None:
            return Response(user, status=status.HTTP_400_BAD_REQUEST)

        user_data = serializers.CreateUserSerializer(user).data

        return Response(user_data, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(request_body=serializers.CreateTokenSerializer)
    def create_token(self, request, *args, **kwargs):
        serializer = serializers.CreateTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        tokens = self.user_services.create_token(data=serializer.data)

        if tokens is None:
            return Response({"detail": 'Invalid username or password'}, status=status.HTTP_403_FORBIDDEN)

        return Response(tokens)

    @swagger_auto_schema(request_body=serializers.GetUserSerializer)
    def get_user(self, request, *args, **kwargs):
        # serializer = serializers.GetUserSerializer(data=request.data)
        # serializer.is_valid(raise_exception=True)

        # u = self.user_services.get_user(data=serializer.data)
        user_from_db = User.objects.get(id=request.user.id)
        user = serializers.GetUserInfoSerializer(user_from_db)

        return Response(user.data)

    @swagger_auto_schema(request_body=serializers.UpdateUserSerializer)
    def update_user(self, request, *args, **kwargs):
        serializer = serializers.UpdateUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = self.user_services.update_user(data=serializer.data, user_id=request.user.id)

        user = serializers.GetUserInfoSerializer(user)

        return Response(user.data)
