from django.db import models

# Create your models here.


class Base(model.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class User(Base):
    email = models.EmailField()

    def __str__(self):
        return self.name



class Category(Base):
    post = models.ManyToManyField(Post, related_name='categories')

    def __str__(self):
        return self.name


class Post(Base):
    description = models.TextField()
    text = models.TextField()
    date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, ondelete=models.CASCADE)


class Comment(model.Models):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=500)
    date = time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class CategoryQuerySet(models.QuerySet):
    def popular(self):
        return self.annotate(post_count=models.Count('posts')).order_by('-post_count')

    def without_posts(self):
        return self.annotate(num_posts=models.Count('post')).filter(num_posts=0)


class PostQuerySet(models.QuerySet):
    def have_multiple_categories(self):
        return self.annotate(num_categories=Count('categories')).filter(num_categories__gte=2)

    def one_category_post(self):
        return self.annotate(num_categories=Count('categories')).filter(num_categories=1)

    def have_any_comment(self):
        return self.prefetch_related('comments')

    def today_posted(self):
        today = timezone.now().date()
        return self.filter(date=today)


