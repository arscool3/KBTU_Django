from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import *
from .serializers import *


class ProjectViewSet(viewsets.ViewSet):
    def list(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)


class UserViewSet(viewsets.ViewSet):
    def list(self, request):
        users = CustomUser.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)


class TaskViewSet(viewsets.ModelViewSet):
    def list(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)


class CommentViewSet(viewsets.ModelViewSet):
    def list(self, request):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)


class AttachmentViewSet(viewsets.ModelViewSet):
    def list(self, request):
        attachment = Attachment.objects.all()
        serializer = AttachmentSerializer(attachment, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = AttachmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)


class TeamViewSet(viewsets.ModelViewSet):
    def list(self, request):
        teams = Team.objects.all()
        serializer = TeamSerializer(teams, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = TeamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)



@api_view(['GET'])
def get_only_build_company(request):
    projects = Project.objects.get_only_build_company().all()

    # status = request.GET.get('pending')
    # if status:
    #     projects = Project.objects.filter(status=status)

    return render(request, 'index.html', {'projects': projects})


@api_view(['GET'])
def get_projects_from_january(request):
    projects = Project.objects.get_only_by_dates().all()

    return render(request, 'index.html', {'projects': projects})


def get_projects_by_date():
    return None