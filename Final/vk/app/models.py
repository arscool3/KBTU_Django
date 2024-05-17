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

    def getAva(self, u):
        try:
            return self.get(user=u).photo.url
        except:
            return 'user_photos/'


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
        try:
            return self.get(post=p).photo.url
        except: 'user_photos/'

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
        return self.filter(user=u_id).order_by('-created_at').filter(group=None)

    def getGroupPosts(self, g_id):
        return self.filter(group=g_id).order_by('-created_at')



class Post(models.Model):
    text = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    group = models.ForeignKey('Group', models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_DEFAULT, default=2)
    objects = PostQuerySets.as_manager()

    def __str__(self):
        return self.user.username + '_' + str(self.created_at) + '_' + str(self.id)


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
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_DEFAULT, default=2)
    objects = ComQuerySets.as_manager()

    def __str__(self):
        return self.user.username + '_' + str(self.created_at)


class LikeQuerySets(models.QuerySet):
    def amount(self, p):
        return self.filter(post=p).count()

    def likeDislike(self, user, postId):
        post = Post.objects.get(id=postId)
        try:
            self.create(user=user, post=post)
        except:
            self.get(user=user, post=post).delete()


class Like(models.Model):
    post = models.ForeignKey('Post', models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_DEFAULT, default=2)
    objects = LikeQuerySets.as_manager()

    class Meta:
        unique_together = ('post', 'user',)

    def __str__(self):
        return self.post.user.username + '_' + str(self.post.created_at) + '_' + self.user.username


class GroupQuerySets(models.QuerySet):
    def myGroups(self, user):
        return self.filter(owner=user)



class Group(models.Model):
    photo = models.ImageField(upload_to="group_photos/%Y/%m/%d/")
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = GroupQuerySets.as_manager()

    def __str__(self):
        return self.name


class SubsQuerySets(models.QuerySet):
    def amount(self, g):
        return self.filter(group=g).count()

    def isSub(self, g, u):
        try:
            self.get(group=g, user=u)
            return True
        except: return False

    def subscribe(self, g, u):
        self.create(group=g, user=u)

    def unsubscribe(self, g, u):
        self.get(group=g, user=u).delete()


class Subscription(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    group = models.ForeignKey('Group', on_delete=models.CASCADE)
    objects = SubsQuerySets.as_manager()

    class Meta:
        unique_together = ('group', 'user',)

    def __str__(self):
        return self.user.username + '_' + self.group.name
