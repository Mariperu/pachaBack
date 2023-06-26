from django.db import models
from appMarcas.models import Marca
from appTipos.models import Tipo


class Modelo(models.Model):
    nombre = models.CharField(max_length=100)
    año_fabricacion = models.IntegerField()
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
