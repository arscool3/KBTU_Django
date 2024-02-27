from django.db import models

# Create your models here.
class Text(models.Model):
    text = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        abstract = True


class UserrQuerySet(models.QuerySet):
    def get_users(self):
        return self.all()

    def get_users_asc(self):
        return self.order_by('full_name')

    def does_user_exist(self, email):
        return self.filter(email=email).exists()
class UserrManager(models.Manager):
    def get_queryset(self):
        return UserrQuerySet(self.model, using=self._db)

    def get_users(self):
        return self.get_queryset().get_users()

    def get_users_asc(self):
        return self.get_queryset().get_users_asc()

    def does_user_exist(self, email):
        return self.get_queryset().does_user_exist(email)
class Userr(models.Model):
    full_name = models.TextField(max_length=200)
    email = models.TextField(max_length=200, unique=True)
    objects = UserrManager()

    def __str__(self):
        return self.full_name


class OfficialAnswer(Text):
    user = models.ForeignKey(Userr, on_delete=models.CASCADE, related_name='answer')

    def __str__(self):
        return self.text + " " + self.created_at.date().__str__()


class CommentaryType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class CommentaryQuerySet(models.QuerySet):
    def public_commentaries(self):
        return self.filter(public=True)

    def private_commentaries(self):
        return self.filter(public=False)

    def get_commentaries_asc(self):
        return self.order_by('created_at')

    def get_commentaries_desc(self):
        return self.order_by('-created_at')


class CommentaryManager(models.Manager):
    def get_queryset(self):
        return CommentaryQuerySet(self.model, using=self._db)

    def public_commentaries(self):
        return self.get_queryset().public_commentaries()

    def private_commentaries(self):
        return self.get_queryset().private_commentaries()

    def get_commentaries_asc(self):
        return self.get_queryset().get_commentaries_asc()

    def get_commentaries_desc(self):
        return self.get_queryset().get_commentaries_desc()

class Commentary(Text):
    user = models.ForeignKey(Userr, on_delete=models.CASCADE, related_name='commentary')
    official_answer = models.OneToOneField(OfficialAnswer, on_delete=models.CASCADE)
    commentary_type_id = models.ForeignKey(CommentaryType, on_delete=models.CASCADE)
    public = models.BooleanField(default=True)
    objects = CommentaryManager()

    def __str__(self):
        return self.user.full_name + " " + self.text + " " + self.created_at.now().__str__()



