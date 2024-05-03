from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpRequest
from base.models import Article,Topic,Profile,ReadingList,Comment,Follow,Like
from base.serializers import ArticleSerializer, ProfileSerializer, TopicSerializer, ReadingListSerializer, CommentSerializer, FollowSerializer, LikeSerializer
from rest_framework import status
@api_view(['GET'])  
def getProfiles(request: HttpRequest):
    profiles = Profile.objects.all()
    serializer = ProfileSerializer(profiles, many=True)
    return Response(serializer.data)

@api_view(['GET'])  
def getArticles(request: HttpRequest):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)
@api_view(['POST'])  
def addArticles(request: HttpRequest):
    serializer=ArticleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])  
def delArticles(request: HttpRequest):
  try:
    article_id = request.data.get('id')
    if article_id:
        article = Article.objects.get(pk=article_id)
        article.delete()
        return Response({'message': 'Article deleted successfully'})
    else:
        return Response({'message': 'Please provide the article ID'}, status=status.HTTP_400_BAD_REQUEST)
  except Article.DoesNotExist:
    return Response({'message': 'Article does not exist'}, status=status.HTTP_404_NOT_FOUND)
  
@api_view(['PUT'])  # Allow both POST and PUT requests
def updArticles(request: HttpRequest):
    try:
        article_id = request.data.get('id')
        if article_id:
            article = Article.objects.get(pk=article_id)
            serializer = ArticleSerializer(instance=article, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'Article updated successfully'})
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message': 'Please provide the article ID'}, status=status.HTTP_400_BAD_REQUEST)
    except Article.DoesNotExist:
        return Response({'message': 'Article does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
@api_view(['GET'])  
def getTopics(request: HttpRequest):
    topics = Topic.objects.all()
    serializer = TopicSerializer(topics, many=True)
    return Response(serializer.data)

@api_view(['POST'])  
def addTopics(request: HttpRequest):
    serializer=TopicSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def delTopics(request: HttpRequest):
    try:
        topic_id = request.data.get('id')
        if topic_id:
            topic = Topic.objects.get(pk=topic_id)
            topic.delete()
            return Response({'message': 'Topic deleted successfully'})
        else:
            return Response({'message': 'Please provide the topic ID'}, status=status.HTTP_400_BAD_REQUEST)
    except Topic.DoesNotExist:
        return Response({'message': 'Topic does not exist'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def updTopics(request: HttpRequest):
    try:
        topic_id = request.data.get('id')
        if topic_id:
            topic = Topic.objects.get(pk=topic_id)
            serializer = TopicSerializer(instance=topic, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'Topic updated successfully'})
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message': 'Please provide the topic ID'}, status=status.HTTP_400_BAD_REQUEST)
    except Topic.DoesNotExist:
        return Response({'message': 'Topic does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
@api_view(['GET'])  
def getReadingLists(request: HttpRequest):
    readinglists = ReadingList.objects.all()
    serializer = ReadingListSerializer(readinglists, many=True)
    return Response(serializer.data)
@api_view(['GET'])  
def getComments(request: HttpRequest):
    comments = Comment.objects.all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)
@api_view(['GET'])  
def getFollows(request: HttpRequest):
    follows = Follow.objects.all()
    serializer = FollowSerializer(follows, many=True)
    return Response(serializer.data)


@api_view(['GET'])  
def getLikes(request: HttpRequest):
    likes= Like.objects.all()
    serializer = LikeSerializer(likes, many=True)
    return Response(serializer.data)
#etc


