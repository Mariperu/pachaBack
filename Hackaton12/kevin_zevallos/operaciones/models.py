from django.db import models

# Create your models here.
from django.db import models


class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    def __str__(self):
        return self.nombre
    # Otros campos relevantes para un alumno


class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre
    # Otros campos relevantes para un profesor


class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    def __str__(self):
        return self.nombre
    # Otros campos relevantes para un curso


class Matricula(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    fecha_matricula = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.curso
    # Otros campos relevantes para una matrícula


class SalaClase(models.Model):
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    alumnos_matriculados = models.ManyToManyField(Alumno)
    capacidad = models.IntegerField()
    def __str__(self):
        return self.curso.nombre
    # Otros campos relevantes para una sala de clase
