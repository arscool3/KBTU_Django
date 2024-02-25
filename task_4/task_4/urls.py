from django.urls import path , include
from store import urls as store_urls


urlpatterns = [
    path('store/', include(store_urls)),

]
