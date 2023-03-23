from django.urls import include, path
from rest_framework import routers
from restapi.app.views import *

#устанавливаем пути
router = routers.DefaultRouter()
router.register("user/search", UserSearchViewSet)
router.register("chats", ChatViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls))
]
