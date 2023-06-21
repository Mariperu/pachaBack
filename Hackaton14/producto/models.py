from django.db import models

# Create your models here.
class Rol(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre


class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=400, null=True, blank=True)
    cantidad = models.IntegerField()
    marca = models.CharField(max_length=100)
    precio = models.FloatField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    dni = models.CharField(max_length=12)
    celular = models.CharField(max_length=9)
    direccion = models.CharField(max_length=200)
    puntos = models.IntegerField(null=True, blank=True, default=0)

    def __str__(self):
        return self.nombre


class Factura(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    # user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    producto= models.ForeignKey(Producto, on_delete=models.CASCADE)
    Cantidad = models.IntegerField()
    montoTotal = models.FloatField(null=True)

    def __str__(self):
        return self.id
