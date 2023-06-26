from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    role_choices = (
        ('Cajero', 'Cajero'),
        ('Administrador', 'Administrador')
    )
    role = models.CharField(max_length=15, choices=role_choices)


class Cliente(models.Model):
    identificador = models.CharField(max_length=15)
    puntos = models.IntegerField()

class Producto(models.Model):
    nombre = models.CharField(max_length=20)
    descripcion = models.TextField(max_length=50)
    laboratorio = models.CharField(max_length=20)
    stock = models.IntegerField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.nombre



class Factura(models.Model):
    numero_factura = models.CharField(max_length=50, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    cliente = models.CharField(max_length=100)

    def __str__(self):
        return f'Factura {self.numero_factura} {self.created} {self.cliente}'



class DetalleFactura(models.Model):
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    precio = models.FloatField()
    cantProducto = models.IntegerField()

    @property
    def subtotal(self):
        return self.cantProducto * self.precio

    def __str__(self):
        return f'DetalleFactura {self.nombre} {self.precio} {self.factura} {self.cantProducto} {self.subtotal}'
