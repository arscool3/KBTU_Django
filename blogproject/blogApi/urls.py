from django.urls import path
from blogApi.views import postView, categoryViews, commentsView, auth

urlpatterns = [
    path('',postView.get),
    path('add',postView.post),
    path('<int:pk>/', postView.post_detail),

    path('categories',categoryViews.get),
    path('categories/add', categoryViews.post),
    path('review/<int:pk>/', commentsView.AddComments.as_view(), name="add_comments"),

    path('register/', auth.register_view, name='register'),
    path('login/', auth.login_view, name='login'),
    path('logout/', auth.logout_view, name='logout'),
    path('check/', auth.check_view, name='check')
]