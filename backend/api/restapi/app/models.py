from django.db import models
from django.contrib.auth.models import User

CHAT_TYPE = (
    ("gm", "Groupe Chat"),
    ("pm", "Private Chat")
)
PROMPT_TYPE = (
    ("f", "file"),
    ("s", "sound"),
    ("i", "image")
)
class Chat(models.Model):
    name = models.TextField()
    type = models.CharField(max_length=3,
                            choices=CHAT_TYPE)
    members = models.ManyToManyField(User)

class Message(models.Model):
    text = models.TextField()
    forward_message = models.ForeignKey("Message",
                                        on_delete=models.CASCADE,
                                        null=True,
                                        blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name="messages")

class Prompt(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    type = models.CharField(max_length=2, choices=PROMPT_TYPE)
    file = models.FileField(upload_to="uploads/")