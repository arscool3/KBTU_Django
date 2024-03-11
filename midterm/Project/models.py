from django.db import models


class CustomUser(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class ProjectQuerySet(models.QuerySet):
    def get_only_build_company(self):
        return self.filter(title='Build Company')

    def get_only_by_dates(self):
        return self.filter(start_date__gte='2024-01-01')


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20)

    objects = ProjectQuerySet.as_manager()

    def __str__(self):
        return self.title


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    deadline = models.DateField()
    status = models.CharField(max_length=20)
    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    assigned_to = models.ForeignKey('CustomUser', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.TextField()
    author = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    task = models.OneToOneField('Task', on_delete=models.CASCADE)

    def __str__(self):
        return f"Comment by {self.author.name}"


class Attachment(models.Model):
    filename = models.CharField(max_length=255)
    file_type = models.CharField(max_length=50)
    task = models.OneToOneField('Task', on_delete=models.CASCADE)

    def __str__(self):
        return self.filename


class Team(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField('CustomUser')
    project = models.OneToOneField('Project', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
