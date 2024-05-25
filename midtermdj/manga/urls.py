from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import user_profile, edit_user_profile, upload_manga, add_chapter, upload_page, manga_detail, register, \
    logout_view
from django.contrib.auth.views import LoginView
urlpatterns = [
    path('', views.manga_list, name='manga_list'),
    path('manga/<int:manga_id>/', views.manga_detail, name='manga_detail'),
    path('chapter/<int:chapter_id>/', views.chapter_detail, name='chapter_detail'),
    path('profile/<str:username>/', views.user_profile, name='user_profile'),
    path('profile/<str:username>/edit/', views.edit_user_profile, name='edit_user_profile'),
    path('upload/', views.upload_manga, name='upload_manga'),
    path('manga/<int:manga_id>/add_chapter/', views.add_chapter, name='add_chapter'),
    path('chapter/<int:chapter_id>/upload_pages/', views.upload_page, name='upload_page'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', logout_view, name='logout'),
    path('', include('manga.api_urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
