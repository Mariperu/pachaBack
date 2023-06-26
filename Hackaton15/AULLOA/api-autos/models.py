from django.db import models

class Marca(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Tipo(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Auto(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    modelo = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    anio = models.IntegerField()
    img_apth = models.CharField(max_length=500, default="", null=True)

    def __str__(self):
        return self.modelo
