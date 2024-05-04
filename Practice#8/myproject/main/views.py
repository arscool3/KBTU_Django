# app/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Test
from .serializers import TestSerializer

class TestView(APIView):
    def get(self, request, pk=None):
        if pk:
            test = Test.objects.get(pk=pk)
            serializer = TestSerializer(test)
        else:
            tests = Test.objects.all()
            serializer = TestSerializer(tests, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        test = Test.objects.get(pk=pk)
        serializer = TestSerializer(test, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        test = Test.objects.get(pk=pk)
        test.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)