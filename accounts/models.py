from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    ROLES = (
        ('TEJEDOR', 'Tejedor / Artesano'),
        ('CLIENTE', 'Cliente / Comprador'),
        ('ADMIN', 'Administrador'),
    )
    rol = models.CharField(max_length=10, choices=ROLES, default='CLIENTE')
    telefono = models.CharField(max_length=20, blank=True, null=True)
    ubicacion = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.username} ({self.get_rol_display()})"