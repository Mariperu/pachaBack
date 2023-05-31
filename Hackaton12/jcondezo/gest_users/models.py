import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Alumno(models.Model):
    nombre = models.CharField(max_length=200)
    dni = models.CharField(max_length=15)
    edad = models.IntegerField(default=0)
    celular = models.CharField(max_length=9)
    estado = models.CharField(max_length=3)

    def __str__(self):
        return self.nombre

class Profesor(models.Model):
    nombre = models.CharField(max_length=200)
    dni = models.CharField(max_length=15)
    edad = models.IntegerField(default=0)
    celular = models.CharField(max_length=9)
    estado = models.CharField(max_length=3)

    def __str__(self):
        return self.nombre

class Curso(models.Model):
    nombre = models.CharField(max_length=200)
    estado = models.CharField(max_length=3)

    def __str__(self):
        return self.nombre

class Salon(models.Model):
    nombre = models.CharField(max_length=200)
    periodo = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Matricula(models.Model):
    fecha = models.DateTimeField("date matricula")
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    salon = models.ForeignKey(Salon, on_delete=models.CASCADE)

    def tuition(self):
        return self.fecha >= timezone.now()