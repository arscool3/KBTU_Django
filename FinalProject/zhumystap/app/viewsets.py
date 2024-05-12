from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import User, Company, Skill, Vacancy, Resume, Response
from .serializers import UserSerializer, CompanySerializer, SkillSerializer, VacancySerializer, ResumeSerializer, \
    ResponseSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class VacancyViewSet(viewsets.ModelViewSet):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer

    @action(detail=True, methods=['post'])
    def activate(self, request, pk=None):
        vacancy = self.get_object()
        vacancy.is_active = True
        vacancy.save()
        return Response({'status': 'Vacancy activated'}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def deactivate(self, request, pk=None):
        vacancy = self.get_object()
        vacancy.is_active = False
        vacancy.save()
        return Response({'status': 'Vacancy deactivated'}, status=status.HTTP_200_OK)


class ResumeViewSet(viewsets.ModelViewSet):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer


class ResponseViewSet(viewsets.ModelViewSet):
    queryset = Response.objects.all()
    serializer_class = ResponseSerializer
