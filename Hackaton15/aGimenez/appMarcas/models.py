from django.db import models

# Create your models here.
class Marca(models.Model):
    nombre = models.CharField(max_length=100)
    pais_origen = models.CharField(max_length=100)
    año_fundacion = models.IntegerField()

    def __str__(self):
        return self.nombre