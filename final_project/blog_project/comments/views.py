from rest_framework.decorators import api_view
from rest_framework.response import Response
from blog_project.utils import handle_get_request, handle_post_request, handle_update_request, handle_delete_request


from .serializers import *

@api_view(['GET'])
def get_all_comments(request):
    return handle_get_request(Post, CommentSerializer, request.query_params.dict())

@api_view(['POST'])
def create_comment(request):
    return handle_post_request(CommentSerializer, request.data)

@api_view(['POST'])
def update_comment(request, pk):
    return handle_update_request(Comment, CommentSerializer, pk, request.data)

@api_view(['DELETE'])
def delete_comment(request, pk):
    return handle_delete_request(Comment, pk)