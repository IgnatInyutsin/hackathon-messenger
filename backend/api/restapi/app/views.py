from rest_framework import viewsets, mixins, permissions
from restapi.app.serializers import *
from restapi.app.models import *
from rest_framework.serializers import ValidationError
from datetime import datetime
from django.db import transaction
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from restapi.app.permissions import ChatMemberPermission

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

class ChatViewSet(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatCreateSerializer
    permission_classes = (permissions.IsAuthenticated, ChatMemberPermission)

    def get_serializer_class(self): # Разные методы - разные сериализаторы
        if self.action == "list":
            return ChatGetSerializer
        elif self.action == "retrieve":
            return ChatRetrieveSerializer
        else:
            return ChatCreateSerializer

    def get_queryset(self): # Особенная область значений для list
        if self.action == "list":
            return Chat.objects.filter(members__in=[self.request.user])
        return self.queryset