from django.db import models

class Marca(models.Model):
    nombre = models.CharField(max_length=100)
    # Otros campos de tu modelo

class Tipo(models.Model):
    nombre = models.CharField(max_length=100)
    # Otros campos de tu modelo
