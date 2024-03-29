from django.urls import path
from blogApi.views import category_views, comments_view, post_view, auth

urlpatterns = [
    path('',post_view.get),
    path('add',post_view.post),
    path('<int:pk>/', post_view.post_detail),
    path('list/', post_view.post_list),

    path('categories',category_views.get),
    path('categories/add', category_views.post),
    path('review/<int:pk>/', comments_view.AddComments.as_view(), name="add_comments"),

    path('register/', auth.register_view, name='register'),
    path('login/', auth.login_view, name='login'),
    path('logout/', auth.logout_view, name='logout'),
    path('check/', auth.check_view, name='check')
]