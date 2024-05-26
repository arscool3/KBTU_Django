from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.models import User
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_info(request):
    user = request.user
    return Response({
        'id': user.id,
        'username': user.username,
        'email': user.email,
        # other user data
    })
@api_view(['GET'])
def getUser(request,id):
    user = User.objects.get(id=id)
    return Response({
        'id': user.id,
        'username': user.username,
        'email': user.email,
    })