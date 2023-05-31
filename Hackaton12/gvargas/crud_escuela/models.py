from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Alumno(models.Model):
    nombre = models.CharField(max_length=200, null=False, default='')
    dni = models.BigIntegerField(null=False, default=1111111)
    edad = models.PositiveIntegerField(null=True, validators=[MinValueValidator(1)])
    email = models.CharField(max_length=200, null=False, default='')
    descripcion = models.CharField(max_length=200, null=True)
    creado_por = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nombre
    
class Ciclo(models.Model):
    nombre = models.CharField(max_length=200, null=False, default='')
    creado_por = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.nombre

class Curso(models.Model):
    nombre = models.CharField(max_length=200, null=False, default='')
    descripcion = models.CharField(max_length=200, null=True)
    ciclo = models.ForeignKey(Ciclo, on_delete=models.DO_NOTHING)
    creado_por = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nombre

class Profesor(models.Model):
    nombre = models.CharField(max_length=200, null=False, default='')
    dni = models.BigIntegerField(null=False, default=1111111)
    edad = models.PositiveIntegerField(null=True, validators=[MinValueValidator(1)])
    email = models.CharField(max_length=200, null=False, default='')
    descripcion = models.CharField(max_length=200, null=True)
    creado_por = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(default=timezone.now)
    curso = models.ForeignKey(Curso, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.nombre
    
class Aula(models.Model):
    nombre = models.CharField(max_length=200, null=False, default='')
    ciclo = models.ForeignKey(Ciclo, on_delete=models.DO_NOTHING)
    max_estudiante = models.PositiveIntegerField(null=True, validators=[MinValueValidator(1)])
    def __str__(self):
        return self.nombre
    
class Matricula(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.DO_NOTHING)
    profesor = models.ForeignKey(Profesor, on_delete=models.DO_NOTHING)
    curso = models.ForeignKey(Curso, on_delete=models.DO_NOTHING)
    ciclo = models.ForeignKey(Ciclo, on_delete=models.DO_NOTHING)
    aula = models.ForeignKey(Aula, on_delete=models.DO_NOTHING)
    creado_por = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.created)
