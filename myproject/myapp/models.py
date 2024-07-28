from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    student_id = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.username

class Assignment(models.Model):
    student_id = models.IntegerField()
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    # due_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
