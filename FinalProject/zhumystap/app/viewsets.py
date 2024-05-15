import rest_framework.status
from rest_framework import viewsets, status
from rest_framework.decorators import action
import rest_framework.response
from .models import User, Company, Skill, Vacancy, Resume, Response
from .serializers import UserSerializer, CompanySerializer, SkillSerializer, VacancySerializer, ResumeSerializer, \
    ResponseSerializer
from .dramatiq_tasks import activate_vacancy_notification


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

    @action(detail=True, methods=['POST'])
    def activate(self, request, pk=None, *args, **kwargs):
        vacancy = self.get_object()
        vacancy.is_active = True
        vacancy.save()
        activate_vacancy_notification.send(vacancy={
            "title": vacancy.title,
            "description": vacancy.description,
        })
        return rest_framework.response.Response({'status': 'Vacancy activated'}, status=rest_framework.status.HTTP_200_OK, )

    @action(detail=True, methods=['post'])
    def deactivate(self, request, pk=None):
        vacancy = self.get_object()
        vacancy.is_active = False
        vacancy.save()
        return rest_framework.response.Response({'status': 'Vacancy deactivated'}, status=status.HTTP_200_OK)


class ResumeViewSet(viewsets.ModelViewSet):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer


class ResponseViewSet(viewsets.ModelViewSet):
    queryset = Response.objects.all()
    serializer_class = ResponseSerializer
