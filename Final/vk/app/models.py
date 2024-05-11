from django.conf import settings
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class UserInfoQuerySets(models.QuerySet):
    def just_registrated(self, u):
        ui = self.create(user=u)
        ui.save()

    def getinfo(self, u):
        return self.get(user=u)


class UserInfo(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    phone_number = PhoneNumberField(region='KZ')
    photo = models.ImageField(upload_to="user_photos/%Y/%m/%d/")
    objects = UserInfoQuerySets.as_manager()

    def __str__(self):
        return self.user.username + 'info'

class ImageQuerySets(models.QuerySet):
    def getPostImage(self, p):
        return self.get(post=p)

class Image(models.Model):
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    objects = ImageQuerySets.as_manager()

    def __str__(self):
        return 'photo' + str(self.id)


class PostQuerySets(models.QuerySet):
    def getPostImage(self, p):
        return self.get(post=p)

    def getPersonPosts(self, u_id):
        return self.filter(user=u_id)

    def getGroupPosts(self, g_id):
        return self.filter(group=g_id)


class Post(models.Model):
    text = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    group = models.ForeignKey('Group', models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    objects = PostQuerySets.as_manager()

    def __str__(self):
        return self.user.username + '_' + str(self.created_at)


class ComQuerySets(models.QuerySet):
    def amount(self, p):
        return self.filter(post=p).count()

    def getPostComs(self, p):
        return self.filter(post=p).order_by('-created_at')


class Comment(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    post = models.ForeignKey('Post', models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    objects = ComQuerySets.as_manager()

    def __str__(self):
        return self.user.username + '_' + str(self.created_at)


class LikeQuerySets(models.QuerySet):
    def amount(self, p):
        return self.filter(post=p).count()


class Like(models.Model):
    post = models.ForeignKey('Post', models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    objects = LikeQuerySets.as_manager()

    class Meta:
        unique_together = ('post', 'user',)

    def __str__(self):
        return self.post.user.username + '_' + str(self.post.created_at) + '_' + self.user.username



class Group(models.Model):
    photo = models.ImageField(upload_to="group_photos/%Y/%m/%d/")
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class SubsQuerySets(models.QuerySet):
    def amount(self, g):
        return self.filter(group=g).count()


class Subscription(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    group = models.ForeignKey('Group', models.CASCADE)
    objects = SubsQuerySets.as_manager()

    class Meta:
        unique_together = ('group', 'user',)

    def __str__(self):
        return self.user.username + '_' + self.group.name