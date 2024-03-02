from django.db import models

class TaskManager(models.Manager):
    def urgent_tasks(self):
        return self.filter(priority='URGENT')

    def completed_tasks(self):
        return self.filter(status='COMPLETED')

class UserManager(models.Manager):
    def active_users(self):
        return self.filter(is_active=True)

    def inactive_users(self):
        return self.filter(is_active=False)
