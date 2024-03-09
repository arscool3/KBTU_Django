from django.contrib.auth.models import AbstractUser, User
from django.db import models

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    time = models.CharField(max_length=100, default="")
    def __str__(self):
        return f"{self.sender}, content: {self.content}"

class ChatRoom(models.Model):
    name = models.CharField(max_length=255)
    members = models.ManyToManyField(User, related_name='chat_rooms')
    messages = models.ManyToManyField(Message, related_name='chat_room_messages')
    def get_all_messages(self):
        return self.messages.all()
    def __str__(self):
        return self.name

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}: {self.message}"

class Attachment(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name='attachments')
    file = models.FileField(upload_to='attachments/')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Attachment for {self.message}"

class OnlineUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='online_status')
    last_activity = models.DateTimeField(auto_now=True)
    is_online = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user} - Online: {self.is_online}"