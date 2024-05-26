from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets

from .serializers import GroupSerializer, UserSerializer
from django.http import HttpResponse
from django.shortcuts import render

from .forms import MyForm


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


def main(request):
    return HttpResponse("This is main page")

def more(request):
    return HttpResponse("This is more page")

def test(request):
    return HttpResponse("This is test page")

def html(request):
    return HttpResponse("This is test page")

def my_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            print('ok')
    else:
        form = MyForm()

    return render(request, 'my_template.html', {'form': form})