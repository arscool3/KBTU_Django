from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # Admin URLs
    path('admin/', admin.site.urls),

    # Custom view URLs
    path('get_user/<int:user_id>/', views.get_user),
    path('create_user/', views.create_user),
    path('get_category/<int:category_id>/', views.get_category),
    path('create_category/', views.create_category),
    path('get_post/<int:post_id>/', views.get_post),
    path('create_post/', views.create_post),
    path('get_comment/<int:comment_id>/', views.get_comment),
    path('create_comment/', views.create_comment),
]

