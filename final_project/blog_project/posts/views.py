from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from blog_project.utils import handle_get_request, handle_post_request, handle_update_request, handle_delete_request
from dramatiq_tasks import process_post_creation
from rest_framework import status


from .serializers import *


#Overview of endpoints
@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'Posts': '/all_posts, /create_post, /update/pk, /delete/pk',
        'Categories': '/categories, /create_category, /update_category/pk, /delete_category/pk'
    }
    return Response(api_urls)

@api_view(['GET'])
def get_all_posts(request):
    return handle_get_request(Post, PostSerializer, request.query_params.dict())

@api_view(['POST'])
def create_post(request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        post = serializer.save()  
        process_post_creation.send(post.id)  
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
def update_post(request, pk):
    return handle_update_request(Post, PostSerializer, pk, request.data)

@api_view(['DELETE'])
def delete_post(request, pk):
    return handle_delete_request(Post, pk)

@api_view(['GET'])
def get_all_categories(request):
    return handle_get_request(Category, CategorySerializer, request.query_params.dict())

@api_view(['POST'])
def create_category(request):
    return handle_post_request(CategorySerializer, request.data)

@api_view(['POST'])
def update_category(request, pk):
    return handle_update_request(Category, CategorySerializer, pk, request.data)

@api_view(['DELETE'])
def delete_category(request, pk):
    return handle_delete_request(Category, pk)



def post_list(request):
    posts = Post.objects.all().order_by('-created_at')  
    return render(request, 'blog/post_list.html', {'posts': posts})