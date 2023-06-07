
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}
from django.db import models
from django.contrib.auth.models import User


class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    # Añade los campos adicionales necesarios


class Salon(models.Model):
    nombre = models.CharField(max_length=100)
    cursos = models.ManyToManyField(Curso)
    # Añade los campos adicionales necesarios


class Asistencia(models.Model):
    fecha = models.DateField()
    alumno = models.ForeignKey(User, on_delete=models.CASCADE)
    # Añade los campos adicionales necesarios


class Nota(models.Model):
    fecha = models.DateField()
    alumno = models.ForeignKey(User, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    nota = models.FloatField()
    # Añade los campos adicionales necesarios


class Administrador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Añade los campos adicionales necesarios


class Profesor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cursos = models.ManyToManyField(Curso)
    # Añade los campos adicionales necesarios


class Alumno(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    salon = models.ForeignKey(Salon, on_delete=models.CASCADE)
    # Añade los campos adicionales necesarios
