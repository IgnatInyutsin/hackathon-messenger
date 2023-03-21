from django.contrib import admin
from django.urls import path, include
from .yasg import urlpatterns as doc_urls

urlpatterns = []

urlpatterns += doc_urls

urlpatterns += [
    path('api/auth/admin/', admin.site.urls),
    path('api/auth/api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.authtoken')),
    path('api/auth/', include('djoser.urls.jwt')),
    path('api/', include('restapi.app.routes'))
]