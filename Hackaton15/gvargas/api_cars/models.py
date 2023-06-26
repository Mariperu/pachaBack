from django.db import models

# Create your models here.
class Marca(models.Model):
    nombre = models.CharField(max_length=100, null=False, default='')

    def __str__(self):
        return self.nombre

class Tipo(models.Model):
    nombre = models.CharField(max_length=100, null=False, default='')

    def __str__(self):
        return self.nombre

class Auto(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    color = models.CharField(max_length=100, null=False, default='')
    year = models.IntegerField()
    modelo = models.CharField(max_length=150)
    img_apth = models.CharField(max_length=500, default="", null=True)

    def __str__(self):
        return self.modelo
