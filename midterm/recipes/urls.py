from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('', views.home, name='home'),
    path('recipes/', views.RecipeList.as_view(), name='recipes'),
    path('recipe/<int:id>/', views.RecipeDetail.as_view(), name='recipe'),
    path('recipe/create', views.RecipeCreate.as_view(), name='recipe-create'),
    path('recipe/update/<int:id>/', views.RecipeUpdate.as_view(), name='recipe-update'),
    path('recipe/delete/<int:id>/', views.RecipeDelete.as_view(), name='recipe-delete'),
]
