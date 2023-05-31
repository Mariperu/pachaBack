from django.db import models
from django.utils import timezone
from django.contrib.postgres import fields

# Create your models here.
class New(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateField(default=timezone.now)
    published_date = models.DateField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now
        self.save()

    def __str__(self):
        return self.title
    

class Persona(models.Model): #id, nombre, apellido, numero, correo, contraseña, fecha de nacimiento, sexo, 
    id = models.AutoField(primary_key=True)
    new = models.ForeignKey('New', on_delete=models.CASCADE)
    lista = models.BinaryField(editable=True, default=["a","a","a"])
    nombre = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateField(default=timezone.now)
    published_date = models.DateField(blank=True, null=True)
    sexo = models.BooleanField()
    gmail = models.EmailField()

    def publish(self):
        self.published_date = timezone.now
        self.save()

    def __str__(self):
        return self.nombre