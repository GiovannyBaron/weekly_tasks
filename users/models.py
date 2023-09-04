from django.db import models
from django.contrib.auth.models import User    

class UserRole(models.Model):
    ROLE_CHOICES = [
        ('observer', 'Observador'),
        ('admin', 'Administrador')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=255, choices=ROLE_CHOICES)

    def __str__(self):
        return self.role