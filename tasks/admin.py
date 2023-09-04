from django.contrib import admin

from .models import Task, TaskAssigned

admin.site.register(Task)
admin.site.register(TaskAssigned)