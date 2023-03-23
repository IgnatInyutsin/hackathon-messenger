from rest_framework import serializers
from django.contrib.auth.models import User
from restapi.app.models import Chat
from django.shortcuts import get_object_or_404

class UserSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username"]



class UserForChatCreateSetializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    class Meta:
        model = User
        fields = ["id"]

class ChatCreateSerializer(serializers.ModelSerializer):
    members = UserForChatCreateSetializer(many=True)
    class Meta:
        model = Chat
        fields = ["name", "type", "members"]

    def create(self, validated_data):
        # собираем список пользователей
        members = [get_object_or_404(User, id=validated_data["members"][i].get("id", -1))
                    for i in range(len(validated_data["members"]))]

        chat = Chat(name=validated_data["name"],
             type = validated_data["type"])

        # сохраняем для получения id чтобы реализовать many-to-many
        chat.save()

        # добавляем пользователей
        for i in range(len(members)):
            chat.members.add(members[i])

        chat.save()

        return chat



class UserForChatGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username"]

class ChatGetSerializer(serializers.ModelSerializer):
    members = UserForChatGetSerializer(many=True)
    class Meta:
        model = Chat
        fields = ["id", "name", "type", "members"]