from django.db import models
from django.db.models import Count
from django.contrib.auth.models import BaseUserManager


# Не нужная по итогу вещь
class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, email, password, **extra_fields)


class CategoryManager(models.Manager):
    def get_by_name(self, name):
        return self.filter(name__icontains=name)

    def get_with_posts(self):
        return self.annotate(posts_count=Count('posts')).filter(posts_count__gt=0)

    def get_without_posts(self):
        return self.annotate(posts_count=Count('posts')).filter(posts_count=0)


class PostManager(models.Manager):
    def get_same_categories(self):
        return self.select_related('author').prefetch_related('categories')

    def get_by_author(self, author_id):
        return self.filter(author__id=author_id)

    def get_by_title(self, title):
        return self.filter(title__icontains=title)

    def get_latest_posts(self, count=5):
        return self.order_by('-created_at')[:count]


class CommentManager(models.Manager):
    def get_comments_for_post(self, post_id):
        return self.filter(post__id=post_id)

    def get_comments_by_author(self, author_id):
        return self.filter(author__id=author_id)

    def get_latest_comments(self, count=5):
        return self.order_by('-timestamp')[:count]


class LikeManager(models.Manager):
    def get_likes_for_post(self, post_id):
        return self.filter(post__id=post_id)

    def get_likes_by_author(self, author_id):
        return self.filter(author__id=author_id)


class ChatManager(models.Manager):
    def get_by_title(self, title):
        return self.filter(title__icontains=title)

    def get_latest_chats(self, count=5):
        return self.order_by('-created_at')[:count]

    def get_chats_by_member(self, member_id):
        return self.filter(members__id=member_id)


class MessageManager(models.Manager):
    def get_messages_by_chat(self, chat_id):
        return self.filter(chat__id=chat_id)

    def get_messages_by_sender(self, sender_id):
        return self.filter(sender__id=sender_id)

    def get_latest_messages(self, count=5):
        return self.order_by('-timestamp')[:count]
