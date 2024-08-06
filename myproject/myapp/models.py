from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    STUDENT = 'student'
    TEACHER = 'teacher'
    PRINCIPAL = 'principal'

    ROLE_CHOICES = [
        (STUDENT, 'Student'),
        (TEACHER, 'Teacher'),
        (PRINCIPAL, 'Principal'),
    ]

    student_id = models.IntegerField(null=True, blank=True)
    teacher_id = models.IntegerField(null=True, blank=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default=STUDENT)

    def __str__(self):
        return self.username

class Assignment(models.Model):
    student_id = models.IntegerField()
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    # due_date = models.DateTimeField()
    grade = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    feedback = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
