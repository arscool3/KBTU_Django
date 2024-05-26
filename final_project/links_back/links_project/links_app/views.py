from rest_framework import viewsets, generics, status
from django.db import models
from rest_framework.permissions import AllowAny, IsAuthenticated
from links_app.permissions import IsAdminOrReadOnly, IsAdminUser
from .models import User, Link, Click, Category, Tag, LinkUsage
from .serializers import (
    CustomTokenObtainPairSerializer,
    CustomTokenRefreshSerializer,
    UserSerializer,
    LinkSerializer,
    ClickSerializer,
    CategorySerializer,
    TagSerializer,
    LinkUsageSerializer,
    RegisterSerializer,
)
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

class CustomLoginView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    permission_classes = [AllowAny]

class RefreshTokenView(TokenRefreshView):
    serializer_class = CustomTokenRefreshSerializer
    permission_classes = [AllowAny]

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]

class LinkViewSet(viewsets.ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny]
        elif self.action == 'destroy':
            self.permission_classes = [IsAuthenticated, IsAdminUser]
        else:
            self.permission_classes = [IsAuthenticated, IsAdminOrReadOnly]
        return super().get_permissions()

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def click(self, request, pk=None):
        link = self.get_object()
        Click.objects.create(link=link)
        link.usage.clicks += 1
        link.usage.save()
        return Response({'status': 'link clicked'})

    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def top_links(self, request):
        top_links = Link.objects.annotate(click_count=models.Count('clicks')).order_by('-click_count')[:10]
        serializer = self.get_serializer(top_links, many=True)
        return Response(serializer.data)

class LinkCreateView(generics.CreateAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

class ClickViewSet(viewsets.ModelViewSet):
    queryset = Click.objects.all()
    serializer_class = ClickSerializer

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAuthenticated, IsAdminOrReadOnly]
        return super().get_permissions()

class LinkUsageViewSet(viewsets.ModelViewSet):
    queryset = LinkUsage.objects.all()
    serializer_class = LinkUsageSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]
