from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import settings
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# swagger details
schema_view = get_schema_view(
   openapi.Info(
      title="1market API",
      default_version='v1',
      contact=openapi.Contact(email="blablabla@mail.ru"),
   ),
   public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

    path('api/', include('products.urls')),
    path('api/', include('orders.urls')),
    path('api/', include('shop.urls')),
    path('api/', include('users.urls')),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

