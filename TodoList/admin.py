from django.contrib import admin

from TodoList.models import Task, Profile

# Register your models here.

admin.site.register(Task)

admin.site.register(Profile)