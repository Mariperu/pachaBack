from django.db import models
from django.utils import timezone

class Curso(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(blank=True,max_length=200)
      
    def __str__(self):
        return self.nombre

class Alumno(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(blank=True,max_length=200)
    edad = models.IntegerField(blank=True)
    correo = models.EmailField(blank=True,max_length=200)
    publishedTime = models.DateField(blank=True, null=True)
    matriculado = models.BooleanField(blank=True, null=True)
    curso = models.ForeignKey("Curso", on_delete=models.CASCADE)

    def publish(self):
        self.publishedTime = timezone.now()
        self.save()
    def __str__(self):
        return self.nombre
    
class Profesor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(blank=True,max_length=200)
    edad = models.IntegerField(blank=True)
    correo = models.EmailField(blank=True,max_length=200)
    publishedTime = models.DateField(blank=True, null=True)
    curso = models.ForeignKey("Curso", on_delete=models.CASCADE)

    def publish(self):
        self.publishedTime = timezone.now()
        self.save()
    def __str__(self):
        return self.nombre