from django.db import models
from users.models import User
from marca.models import Marca
from tipo.models import Tipo
# django-ckeditor
from ckeditor.fields import RichTextField

class Auto(models.Model):
    modelo = models.CharField(max_length=30)
    anio = models.IntegerField()
    serial = models.CharField(max_length=25)
    color = models.CharField(max_length=25)
    motor = models.CharField(max_length=25)
    transmision = models.CharField(max_length=25)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE, related_name='tipo')
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, related_name='marca')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='auto')

    def __str__(self):
        return f'{self.modelo}'