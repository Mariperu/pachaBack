from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class Usuario(AbstractUser):
    ROLES = (
        ('A', 'Administrador'),
        ('C', 'Cajero'),
    )
    rol = models.CharField(max_length=1, choices=ROLES, default='C')
    groups = models.ManyToManyField(Group, related_name="usuario_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="usuario_permissions", blank=True)

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.IntegerField(default=0)
    generico = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)

class Cliente(models.Model):
    nombre = models.CharField(max_length=200)
    identificador = models.CharField(max_length=50, unique=True)
    puntos = models.IntegerField(default=0)

class Compra(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    fecha = models.DateTimeField(auto_now_add=True)
