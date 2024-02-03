from django.urls import path
from myapp import views


urlpatterns = [
    path('users/', views.get_users.as_view()),
    path('users/add', views.create_user.as_view()),
    path('users/<int:user_id>', views.delete_user.as_view())

]