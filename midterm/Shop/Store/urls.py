from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect
from django.urls import path
from .views import *

def home_red(request):
    return redirect('home/')

urlpatterns = [
    path('', home_red),
    path('home/', homepage, name='home'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('reg/', RegisterUser.as_view(), name='reg'),
    path('category/<int:cat_id>/', get_pr_by_cat),
    path('busket/', busket, name='busket'),
    path('purchases/', purch, name='purchases'),
    path('profil/', profil, name='profil'),
    path('addAdress/', addAdress, name='addAdress'),

    path('addBusket/<int:pr>/<int:am>/', add_Buscket, name='addBusket'),
    path('delBusket/<int:id>/', del_Buscket, name='delBusket'),
    path('buyBusket', buy_Buscket, name='buyBysket'),

    path('api/products/', ProductViewSet.as_view({'get' : 'list'})),
    path('api/categories/', CatViewSet.as_view({'get' : 'list'}))
]




urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

