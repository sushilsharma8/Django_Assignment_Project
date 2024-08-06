# Generated by Django 5.0.7 on 2024-07-28 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_remove_assignment_due_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('student', 'Student'), ('teacher', 'Teacher'), ('principal', 'Principal')], default='student', max_length=20),
        ),
    ]