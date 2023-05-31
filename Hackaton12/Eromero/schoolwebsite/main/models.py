from django.db import models
from django.contrib.auth.models import User

class Profesor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100, null=True)
    apellido = models.CharField(max_length=100, null=True)
    titulo = models.CharField(max_length=100)
    departamento = models.CharField(max_length=100)
    fecha_contratacion = models.DateField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    def save(self, *args, **kwargs):
        if not self.id:
            self.user_id = self.user.id
        super(Profesor, self).save(*args, **kwargs)



class Estudiante(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100, null=True)
    apellido = models.CharField(max_length=100, null=True)
    fecha_inscripcion = models.DateField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class CursoLibre(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    estudiantes = models.ManyToManyField(Estudiante)

    def __str__(self):
        return self.nombre


class SalaDeClase(models.Model):
    nombre = models.CharField(max_length=100)
    curso_libre = models.ForeignKey(CursoLibre, on_delete=models.CASCADE)
    estudiantes = models.ManyToManyField(Estudiante)
    capacidad_maxima = models.IntegerField()

    def __str__(self):
        return self.nombre
