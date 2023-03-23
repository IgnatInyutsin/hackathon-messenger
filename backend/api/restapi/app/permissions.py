from rest_framework import permissions
from restapi.app.models import Chat
class ChatMemberPermission(permissions.BasePermission):
    """
    Право читать чат только его членам
    """

    def has_permission(self, request, view):
        # сверяем количество чатов с членстом этого пользователя, у которых id равен запрашиваемому
        return len(Chat.objects.filter(id=request.resolver_match.kwargs.get('pk'), members__in=[request.user])) == 1