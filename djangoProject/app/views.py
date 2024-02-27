from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Post, Comment

def posts_list(request):
    posts = Post.objects.all()
    posts_data = [{'id': post.id, 'title': post.title, 'body': post.body, 'author_id': post.author_id} for post in posts]
    return JsonResponse(posts_data, safe=False)

def post_detail(request, pk):
    post = Post.objects.filter(pk=pk).first()
    if post:
        post_data = {'id': post.id, 'title': post.title, 'body': post.body, 'author_id': post.author_id}
        return JsonResponse(post_data)
    else:
        return JsonResponse({'error': 'Post not found'}, status=404)

def comments_list(request, post_pk):
    comments = Comment.objects.filter(post_id=post_pk)
    comments_data = [{'id': comment.id, 'name': comment.name, 'email': comment.email, 'body': comment.body, 'post_id': comment.post_id} for comment in comments]
    return JsonResponse(comments_data, safe=False)

def comment_detail(request, post_pk, pk):
    comment = Comment.objects.filter(post_id=post_pk, pk=pk).first()
    if comment:
        comment_data = {'id': comment.id, 'name': comment.name, 'email': comment.email, 'body': comment.body, 'post_id': comment.post_id}
        return JsonResponse(comment_data)
    else:
        return JsonResponse({'error': 'Comment not found'}, status=404)

@csrf_exempt
def create_post(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        post = Post.objects.create(title=data.get('title'), body=data.get('body'), author_id=data.get('author_id'))
        return JsonResponse({'message': 'Post created successfully', 'post_id': post.id}, status=201)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

@csrf_exempt
def create_comment(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        comment = Comment.objects.create(post_id=data.get('post_id'), name=data.get('name'), email=data.get('email'), body=data.get('body'))
        return JsonResponse({'message': 'Comment created successfully', 'comment_id': comment.id}, status=201)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
