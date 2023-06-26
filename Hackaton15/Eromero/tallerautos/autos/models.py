from django.db import models

class Marca(models.Model):
    nombre = models.CharField(max_length=100)

class Tipo(models.Model):
    nombre = models.CharField(max_length=100)

class Auto(models.Model):
    nombre = models.CharField(max_length=100)
    marca = models.ForeignKey(Marca, related_name='autos', on_delete=models.CASCADE)
    tipo = models.ForeignKey(Tipo, related_name='autos', on_delete=models.CASCADE)
