from django.db import models
import uuid
# Create your models here.
class Rol(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Producto(models.Model):
    name = models.CharField(max_length=100,null=False)
    stock = models.PositiveSmallIntegerField(null=False, default=100)
    price = models.FloatField(null=False)

class Usuario(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100,null=False)
    email = models.CharField(max_length=100,unique=True)
    password = models.CharField(max_length=10,null=False,default='1111111111')
    def __str__(self):
        return self.name
class FarmaciaUser(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    rol = models.ForeignKey(Rol, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100,null=False)
    email = models.CharField(max_length=100,unique=True,null=False)
    password = models.CharField(max_length=10,null=False,default='1111111111')
    def __str__(self):
        return self.name

class Pedido(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    producto = models.ForeignKey(Producto, on_delete=models.DO_NOTHING)
    cantidad = models.IntegerField(default=1,null=False)
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
    total = models.FloatField(null=False)