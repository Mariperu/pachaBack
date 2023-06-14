from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Sexo(models.Model):
    id = models.AutoField(primary_key=True)
    sexo = models.CharField(max_length=1, null=True)
    def __str__(self):
        return self.sexo


class Nacionalidad(models.Model):
    id = models.AutoField(primary_key=True)
    pais = models.CharField(max_length=200)

    def __str__(self):
        return self.pais


class DocumentoIdentidad(models.Model):
    id = models.AutoField(primary_key=True)
    tipoDocumento = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.tipoDocumento


class Administrador(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    nacionalidad = models.ForeignKey('Nacionalidad', on_delete=models.CASCADE, null=True)
    tipoDocumento = models.ForeignKey('DocumentoIdentidad', on_delete=models.CASCADE, null=True)
    numeroDocumento = models.CharField(max_length=13)
    sexo = models.ForeignKey('Sexo', on_delete=models.CASCADE, null=True)
    estado = models.CharField(max_length=3)

    def __str__(self):
        return self.tipoDocumento


class Alumno(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    nacionalidad = models.ForeignKey('Nacionalidad', on_delete=models.CASCADE, null=True)
    tipoDocumento = models.ForeignKey('DocumentoIdentidad', on_delete=models.CASCADE, null=True)
    numeroDocumento = models.CharField(max_length=13)
    sexo = models.ForeignKey('Sexo', on_delete=models.CASCADE, null=True)
    estado = models.CharField(max_length=3)

    def __str__(self):
        return self.nombre


class Curso(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    estado = models.CharField(max_length=3)

    def __str__(self):
        return self.nombre


class Profesor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    nacionalidad = models.ForeignKey('Nacionalidad', on_delete=models.CASCADE, null=True)
    tipoDocumento = models.ForeignKey('DocumentoIdentidad', on_delete=models.CASCADE, null=True)
    numeroDocumento = models.CharField(max_length=13)
    sexo = models.ForeignKey('Sexo', on_delete=models.CASCADE, null=True)
    estado = models.CharField(max_length=3)

    def __str__(self):
        return self.nombre


class Periodo(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=10)
    Anio = models.IntegerField()
    Mes = models.IntegerField()

    def __str__(self):
        return self.nombre


class Notas(models.Model):
    id = models.AutoField(primary_key=True)
    profesor = models.ForeignKey('Profesor', on_delete=models.CASCADE, null=True)
    periodo = models.ForeignKey('Periodo', on_delete=models.CASCADE, null=True)
    curso = models.ForeignKey('Curso', on_delete=models.CASCADE, null=True)
    alumno = models.ForeignKey('Alumno', on_delete=models.CASCADE, null=True)
    nota1 = models.FloatField(max_length=4, null=True, blank=True)
    nota2 = models.FloatField(max_length=4, null=True, blank=True)
    nota3 = models.FloatField(max_length=4, null=True, blank=True)
    nota4 = models.FloatField(max_length=4, null=True, blank=True)
    promedio = models.FloatField(max_length=4, null=True, blank=True)
    
    # def __str__(self):
    #     return self.profesor


class Asistencia(models.Model):
    id = models.AutoField(primary_key=True)
    profesor = models.ForeignKey('Profesor', on_delete=models.CASCADE, null=True)
    periodo = models.ForeignKey('Periodo', on_delete=models.CASCADE, null=True)
    curso = models.ForeignKey('Curso', on_delete=models.CASCADE, null=True)
    alumno = models.ForeignKey('Alumno', on_delete=models.CASCADE, null=True)
    a1 = models.CharField(max_length=2, null=True, blank=True)
    a2 = models.CharField(max_length=2, null=True, blank=True)
    a3 = models.CharField(max_length=2, null=True, blank=True)
    a4 = models.CharField(max_length=2, null=True, blank=True)

    # def __str__(self):
    #     return self.profesor