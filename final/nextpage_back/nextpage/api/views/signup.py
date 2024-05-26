from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework_jwt.serializers import JSONWebTokenSerializer
# noinspection PyUnresolvedReferences
from api.serializers import UserSerializer


class RegistrationAPIView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
            except Exception as e:
                return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)

            token_serializer = JSONWebTokenSerializer(data=serializer.data)
            token = token_serializer.validate(request.data).get('token')
            return Response({'token': token})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)