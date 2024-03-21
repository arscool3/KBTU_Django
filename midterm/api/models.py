from django.contrib.auth.models import AbstractUser, User
from django.db import models
from django.db.models import Count


class MessageQuerySet(models.QuerySet):
    def get_all_messages(self):
        return self.all()

class MessageManager(models.Manager):
    def get_queryset(self):
        return MessageQuerySet(self.model, using=self._db)

    def get_all_messages(self):
        return self.get_queryset().get_all_messages()

class ChatRoomQuerySet(models.QuerySet):
    def count_messages(self):
        return self.annotate(message_count=Count('messages'))


class ChatRoomManager(models.Manager):
    def get_queryset(self):
        return ChatRoomQuerySet(self.model, using=self._db)

    def count_messages(self):
        return self.get_queryset().count_messages()


class NotificationQuerySet(models.QuerySet):
    def unread(self):
        return self.filter(is_read=False)


class NotificationManager(models.Manager):
    def get_queryset(self):
        return NotificationQuerySet(self.model, using=self._db)

    def unread(self):
        return self.get_queryset().unread()


class OnlineUserQuerySet(models.QuerySet):
    def online(self):
        return self.filter(is_online=True)

    def offline(self):
        return self.filter(is_online=False)


class OnlineUserManager(models.Manager):
    def get_queryset(self):
        return OnlineUserQuerySet(self.model, using=self._db)

    def online(self):
        return self.get_queryset().online()

    def offline(self):
        return self.get_queryset().offline()


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    time = models.CharField(max_length=100, default="")

    objects = MessageManager()
    def __str__(self):
        return f"{self.sender}, content: {self.content}"

class ChatRoom(models.Model):
    name = models.CharField(max_length=255)
    members = models.ManyToManyField(User, related_name='chat_rooms')
    messages = models.ManyToManyField(Message, related_name='chat_room_messages')

    objects = ChatRoomManager()
    def get_all_messages(self):
        return self.messages.all()
    def __str__(self):
        return self.name

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = NotificationManager()
    def __str__(self):
        return f"{self.user}: {self.message}"


class Attachment(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name='attachments')
    file = models.FileField(upload_to='attachments/')
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = NotificationManager()
    def __str__(self):
        return f"Attachment for {self.message}"


class OnlineUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='online_status')
    last_activity = models.DateTimeField(auto_now=True)
    is_online = models.BooleanField(default=False)

    objects = OnlineUserManager()
    def __str__(self):
        return f"{self.user} - Online: {self.is_online}"