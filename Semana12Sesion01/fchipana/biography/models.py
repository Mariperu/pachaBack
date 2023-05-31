from django.db import models
from django.utils import timezone

# Create your models here.
class Biografia(models.Model):
    id= models.AutoField(primary_key=True)
    nombre_nacimiento = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    nombre_completo = models.CharField(max_length=200,blank=True,null=True)
    fecha_nacimiento = models.DateField(blank=True,null=True)
    nacionalidad = models.ForeignKey('biography.Nacionalidad',on_delete=models.CASCADE)
    religion = models.CharField(max_length=200)
    educado_en = models.TextField()
    ocupacion = models.TextField()
    empleador = models.TextField()
    sitio_web = models.CharField(max_length=200)
    created_date = models.DateField(default=timezone.now)

    # def publish(self):
    #     self.published_date = timezone.now
    #     self.save()

    def __str__(self):
        return str(self.nombre_completo)
    
class Nacionalidad(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_pais = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre_pais

