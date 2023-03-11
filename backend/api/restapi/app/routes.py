from django.urls import include, path
from rest_framework import routers
from restapi.app.views import WeatherViewSet, ClothViewSet, RecommendationViewSet

#устанавливаем пути
router = routers.DefaultRouter()
router.register('weather', WeatherViewSet)
router.register("clothes", ClothViewSet)
router.register("weather/recommendation", RecommendationViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls))
]
