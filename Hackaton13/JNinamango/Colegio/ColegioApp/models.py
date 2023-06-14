from django.db import models
from django import forms
from django.contrib.auth.models import User, AbstractUser
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
# Create your models here.
class UsuarioApp(models.Model):
    ROL_CHOICES = [('ADMIN', 'admin'), ('PROFESOR', "profesor"), ("ALUMNO", "alumno")]

    rol = models.CharField(max_length=100, choices=ROL_CHOICES)

class UsuarioAppForm(forms.ModelForm):
    class Meta:
        model = UsuarioApp
        fields = ['username', 'password','rol']



class Alumno(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    correo = models.EmailField()
    edad = models.IntegerField(blank=True)
    
class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['nombre', 'correo', 'edad']
        
class Profesor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    correo = models.EmailField()
    edad = models.IntegerField(blank=True)

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ['nombre', 'correo', 'edad']


class Notas(models.Model):
    id = models.AutoField(primary_key=True)
    nota = models.IntegerField()

class NotasForm(forms.ModelForm):
    class Meta:
        model = Notas
        fields = ['nota']

class Asistencia(models.Model):
    id = models.AutoField(primary_key=True)
    asistencia = models.BooleanField()

class AsistenciaForm(forms.ModelForm):
    class Meta:
        model = Asistencia
        fields = ['asistencia']
        
        