# yourapp/urls.py


from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    path("admin/", admin.site.urls),
    path("practice_4/", include("practice_4.urls"))
]
