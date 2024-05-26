from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Test
from .serializers import TestSerializer

# Endpoint to create a new test item
@api_view(['POST'])
def create_test_item(request):
    serializer = TestSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Endpoint to retrieve all test items
@api_view(['GET'])
def get_all_test_items(request):
    tests = Test.objects.all()
    serializer = TestSerializer(tests, many=True)
    return Response(serializer.data)

# Endpoint to retrieve a single test item by ID
@api_view(['GET'])
def get_test_item(request, pk):
    try:
        test = Test.objects.get(pk=pk)
    except Test.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = TestSerializer(test)
    return Response(serializer.data)

# Endpoint to update a test item by ID
@api_view(['PUT'])
def update_test_item(request, pk):
    try:
        test = Test.objects.get(pk=pk)
    except Test.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = TestSerializer(test, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Endpoint to delete a test item by ID
@api_view(['DELETE'])
def delete_test_item(request, pk):
    try:
        test = Test.objects.get(pk=pk)
    except Test.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    test.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
