# myapp/admin.py
from django.contrib import admin
from .models import Assignment, CustomUser
from django.contrib.auth.admin import UserAdmin

admin.site.register(Assignment)
admin.site.register(CustomUser, UserAdmin)
