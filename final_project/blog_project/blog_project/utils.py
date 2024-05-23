# Here I decided to write request handling functions to reduce code duplication

from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist

#Universal functions to handle the similar requests
def handle_get_request(model, serializer, query_params=None):
    objects = model.objects.filter(**query_params) if query_params else model.objects.all()
    if objects:
        serialized_objects = serializer(objects, many=True)
        return Response(serialized_objects.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
def handle_post_request(serializer_class, data):
    serializer = serializer_class(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
def handle_update_request(model, serializer_class, pk, data):
    try:
        instance = model.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = serializer_class(instance=instance, data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
def handle_delete_request(model, pk):
    try:
        instance = model.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    instance.delete()
    return Response(status=status.HTTP_202_ACCEPTED)
