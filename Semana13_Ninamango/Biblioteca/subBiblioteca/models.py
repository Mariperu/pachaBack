from django.db import models
from django.contrib.auth.models import User

class UserApp(User):

    nacionalidad = models.ForeignKey('Nacionalidad', on_delete=models.CASCADE, null=True)
    documentoIdentidad = models.ForeignKey('DocumentoIdentidad', on_delete=models.CASCADE, null=True)
    sexo = models.ForeignKey('Sexo', on_delete=models.CASCADE, null=True)


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    author = models.ManyToManyField('Autor')

    def __str__(self):
        return self.name

class Autor(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    books = models.ManyToManyField('Book')
    nacionalidad = models.ForeignKey('Nacionalidad', on_delete=models.CASCADE, null=True)
    documentoIdentidad = models.ForeignKey('DocumentoIdentidad', on_delete=models.CASCADE, null=True)
    sexo = models.ForeignKey('Sexo', on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.name
    
class Nacionalidad(models.Model):
    id = models.AutoField(primary_key=True)
    pais = models.CharField(max_length=200)

    def __str__(self):
        return self.pais
    
class Sexo(models.Model):
    id = models.AutoField(primary_key=True)
    sexo = models.CharField(max_length=1, null=True)
    def __str__(self):
        return self.sexo

class DocumentoIdentidad(models.Model):
    id = models.AutoField(primary_key=True)
    tipoDocumento = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.tipoDocumento

class RegistroLibro(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey('UserApp', on_delete=models.CASCADE)
    fechaPrestamo = models.DateField()
    diasPrestamo = models.IntegerField()
    entregado = models.BooleanField()

    def __str__(self):
        return self.fechaPrestamo