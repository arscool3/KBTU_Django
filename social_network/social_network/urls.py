"""social_network URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('core.urls', namespace='core')),

    # path('api-auth/', include('rest_framework.urls')),

    # path('/api/auth/register'),
    # path('/api/auth/login'),
    # path('/api/auth/refresh'),
    #
    # path('/api/posts/'),
    # path('/api/posts/<post_id>/like'),
    # path('/api/posts/<post_id>/dislike'),
    # path('/api/posts/<post_id>/'),
    # path('/api/users/<user_id>/posts/'),
    # path('/api/users/<user_id>/liked_posts/'),

]
