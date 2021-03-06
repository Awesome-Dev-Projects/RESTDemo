"""restdemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
]

# auth urls
urlpatterns += [
    path('api/v1/auth/', include('rest_framework.urls')),
]

# demo urls
urlpatterns += [
    path('api/v1/demo/', include('demo.urls')),
]

# users urls
urlpatterns += [
    path('api/v1/users/', include('users.urls')),
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns +=  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = "utils.views.error_404"
handler500 = "utils.views.error_500"


schema_view = get_schema_view(
    openapi.Info(
        title="RESTDemo API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.restdemo.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns += [
    path('', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
                                       cache_timeout=0), name='schema-redoc'),
]

