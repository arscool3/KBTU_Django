from rest_framework_simplejwt.views import TokenObtainPairView

from .models import User

from rest_framework.views import APIView

from .serializers import UserSerializer, CustomTokenObtainPairSerializer
from orders.models import Order
from rest_framework.response import Response



class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        if serializer.data["user_type"] == "Customer":
            new_order = Order(user=User.objects.get(id=serializer.data["id"]))
            new_order.save()

        return Response(serializer.data)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
