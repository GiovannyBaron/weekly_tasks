from django.db import models
from users.models import User


class Task(models.Model):
    TASK_CHOICES = [
        ('documentar', 'Documentar'),
        ('reportes', 'Escribir reportes'),
        ('reunion', 'Reunión'),
        ('operacion', 'Operacion'),
        ('capacitacion', 'Capacitacion'),
    ]
    task = models.CharField(max_length=255, choices=TASK_CHOICES)

    def __str__(self):
        return self.task


class TaskAssigned(models.Model):
    STATUS_CHOICES = [
        ('proceso', 'En proceso'),
        ('finalizado', 'Finalizada')
    ]
    creator_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_tasks')
    user_who_owns = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_tasks')
    task = models.ForeignKey(Task, null=True, on_delete=models.CASCADE)
    status = models.CharField(max_length=255, choices=STATUS_CHOICES)
    week = models.IntegerField(null=True)

    def __str__(self):
        return str(self.user_who_owns)
