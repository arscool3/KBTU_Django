from django.urls import path, include
from .routers import router

urlpatterns = [
    path('', include(router.urls)),
    path('drf-auth', include('rest_framework.urls')),
    # # get full
    # path('', UserView.as_view(), name="users_default"),
    # path('users/', UserView.as_view(), name="users"),
    # path('categories/', CategoryView.as_view(), name="categories"),
    # path('posts/', PostView.as_view(), name="posts"),
    # path('comments/', CommentView.as_view(), name="comments"),
    # path('likes/', LikeView.as_view(), name="likes"),
    # path('chats/', ChatView.as_view(), name="chats"),
    # path('messages/', MessageView.as_view(), name="messages"),
    # #post
    # # path('create_user', UserView.as_view()), спрошу у препода, не забыть
    # path('create_category/', create_category, name="create_category"),
    # path('create_post/', create_post, name="create_post"),
    # path('create_comment/', create_comment, name="create_comment"),
    # path('create_like/', create_like, name="create_like"),
    # path('create_chat/', create_chat, name="create_chat"),
    # path('create_message/', create_message, name="create_message"),
    # # get managers(чуть лень поэтому только 3 решил сделать а не всех сделанные querySet'ы)
    # path('categories_with_posts/', CategoriesWithPostsView.as_view(), name="categories_with_posts"),
    # path('latest_comments/', latest_comments, name="latest_comments"),
    # path('chats_by_member/<int:id>/', chats_by_member, name="chats_by_member"),
    # #update, delete. Тоже стало лень все делать, поэтому только пост, что самое сложное типа
    # path('update_post/<int:id>/', update_post, name="update_post"),
    # path('delete_post/<int:id>/', delete_post, name="delete_post"),
    # # auth
    # path('register/', register, name='register'),
    # path('login/', logIn, name='login'),
    # path('profile/', profile, name='profile'),
    # path('logout/', logOut, name="logout"),
    # -----------------------------------
    # -----------------------------------
    # auth
    # path('login/', logIn, name='login'),
    # path('profile/', ProfileView.as_view(), name='profile'),
]
