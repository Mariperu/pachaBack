from django.db import models
from appModelos.models import Modelo


class Auto(models.Model):
    numero_serie = models.CharField(max_length=100)
    año_fabricacion = models.IntegerField()
    color = models.CharField(max_length=50)
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)

    def __str__(self):
        return self.numero_serie
