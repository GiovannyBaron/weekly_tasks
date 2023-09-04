from rest_framework import serializers
from users.models import User
from .models import Task, TaskAssigned


class TaskAssignedSerializer(serializers.ModelSerializer):
    creator_user = serializers.CharField(source='creator_user.username')
    user_who_owns = serializers.CharField(source='user_who_owns.username')
    task = serializers.CharField(source='task.task')

    class Meta:
        model = TaskAssigned
        fields = ('creator_user', 'user_who_owns', 'task', 'status', 'week')
