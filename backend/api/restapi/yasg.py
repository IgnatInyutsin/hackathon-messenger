from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Инициализация автодокументирования

schema_view = get_schema_view(
    openapi.Info(
        title="Insult App API",
        default_version='v1',
        description='Сервис инфраструктуры MTG Ladder, отвечающий за взаимодействие с пользователями портала',
        license=openapi.License(name='GNU License')
    ),
    public=True,
    permission_classes=(permissions.AllowAny,)
)

urlpatterns = [
    path('api/documentation(?P<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('api/documentation/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]