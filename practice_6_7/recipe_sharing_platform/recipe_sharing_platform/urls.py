"""
URL configuration for recipe_sharing_platform project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from recipes import views

urlpatterns = [
    path('account/login/', LoginView.as_view(template_name='login/login.html'), name='login'),
    path('account/signup/', views.register_view, name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('admin/', admin.site.urls),
    # GET Endpoints
    path('recipes/', views.get_all_recipes, name='get_all_recipes'),
    path('recipes/<int:recipe_id>/', views.get_recipe, name='get_recipe'),
    path('recipes/category/<int:category_id>/', views.get_recipes_by_category, name='get_recipes_by_category'),
    path('ratings/', views.get_all_ratings, name='get_all_ratings'),
    path('recipes/<int:recipe_id>/ratings/', views.get_ratings_for_recipe, name='get_ratings_for_recipe'),
    path('recipes/<int:recipe_id>/comments/', views.get_comments_for_recipe, name='get_comments_for_recipe'),

    # POST Endpoints
    path('recipes/create/', views.create_recipe, name='create_recipe'),
    path('recipes/<int:recipe_id>/rate/', views.rate_recipe, name='rate_recipe'),
    path('recipes/<int:recipe_id>/comment/', views.add_comment, name='add_comment'),
    path('recipes/<int:recipe_id>/leave-comment/', views.leave_comment, name='leave_comment'),
    path('user/update-info/', views.update_user_info, name='update_user_info'),
    path('recipes/<int:recipe_id>/update-info/', views.update_recipe_info, name='update_recipe_info'),

    path('categories/create/', views.create_category, name='create_category'),
    path('ingredients/create/', views.create_ingredient, name='create_ingredient'),

]
