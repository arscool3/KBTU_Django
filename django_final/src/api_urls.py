from django.urls import path, include

urlpatterns = [
    path('v1/', include('api_urls.v1')),
]
