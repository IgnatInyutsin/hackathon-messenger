from rest_framework import serializers
from django.contrib.auth.models import User
from restapi.app.models import Chat

class UserSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username"]

class UserForChatCreateSetializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id"]
class ChatCreateSerializer(serializers.ModelSerializer):
    members = UserForChatCreateSetializer(read_only=True, many=True)
    class Meta:
        model = Chat
        fields = ["name", "type", "members"]