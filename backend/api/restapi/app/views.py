from rest_framework import viewsets, mixins, permissions
from restapi.app.serializers import *
from restapi.app.models import *
from rest_framework.serializers import ValidationError
from datetime import datetime
from django.db import transaction
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q

class UserSearchViewSet(mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSearchSerializer
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        queryset = self.queryset
        # фильтр по имени пользователя
        if "username" in self.request.query_params:
            queryset = queryset.filter(Q(name__icontains=self.request.query_params.get("username")) |
                                       Q(english_name__icontains=self.request.query_params.get("username")))
        return queryset