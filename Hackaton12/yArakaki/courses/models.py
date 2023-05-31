from django.db import models

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    limite_estudiantes = models.IntegerField(default=20)

    def __str__(self):
        return self.nombre

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    dni = models.IntegerField(max_length=8)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    dni = models.IntegerField(max_length=8)
    curso = models.OneToOneField(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre