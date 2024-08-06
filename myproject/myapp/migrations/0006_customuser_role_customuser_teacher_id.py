# Generated by Django 5.0.7 on 2024-08-05 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_remove_assignment_grade_remove_assignment_teacher_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('student', 'Student'), ('teacher', 'Teacher'), ('principal', 'Principal')], default='student', max_length=10),
        ),
        migrations.AddField(
            model_name='customuser',
            name='teacher_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]