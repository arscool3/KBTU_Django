from django.db import models

from users.models import User


class Chat(models.Model):
    participants = models.ManyToManyField(User, related_name='chats')

    def __str__(self):
        return ', '.join([str(user) for user in self.participants.all()])


class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(blank=True, auto_now_add=True)

    def __str__(self):
        return f'{self.sender.username}: {self.content}'
