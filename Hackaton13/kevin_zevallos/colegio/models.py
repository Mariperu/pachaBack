from django.db import models
import uuid
from datetime import date
from django.core.validators import MinValueValidator

# Create your models here.
class Rol(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Ciclo(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Aula(models.Model):
    name = models.CharField(max_length=150, null=False, default='')
    max_student = models.PositiveSmallIntegerField(null=False, default=10)
    grade = models.ForeignKey(Ciclo, on_delete=models.DO_NOTHING)
    def __str__(self):
        return self.name

class Curso(models.Model):
    name = models.CharField(max_length=150, null=False, default='')
    description = models.CharField(max_length=200, null=True)
    grade = models.ForeignKey(Ciclo, on_delete=models.DO_NOTHING)
    availability = models.PositiveSmallIntegerField(null=False, default=5)
    img_path = models.CharField(max_length=500, null=True)
    
    def __str__(self):
        return self.name
    
class Alumno(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150, null=False, default='')
    dni = models.CharField(max_length=10,null=False, default='72443245')
    email = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=200, null=True)
    img_path = models.CharField(max_length=500, null=True)
    availability = models.PositiveSmallIntegerField(null=False, default=5)
    password = models.CharField(max_length=10,null=False, default='1111111')

    def __str__(self):
        return self.name
    
class UsuarioColegio(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150, null=False, default='')
    dni = models.CharField(max_length=10,null=False, default='72443245')
    email = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=200, null=True)
    img_path = models.CharField(max_length=500, null=True)
    availability = models.PositiveSmallIntegerField(null=False, default=5)
    password = models.CharField(max_length=10,null=False, default='1111111')
    rol = models.ForeignKey(Rol, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name
    
class Matricula(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student = models.ForeignKey(Alumno, on_delete=models.DO_NOTHING)
    teacher = models.ForeignKey(UsuarioColegio, on_delete=models.DO_NOTHING)
    section = models.ForeignKey(Aula, on_delete=models.DO_NOTHING)
    grade = models.ForeignKey(Ciclo, on_delete=models.DO_NOTHING)
    course = models.ForeignKey(Curso, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return str(self.id)

class Asistencia(models.Model):
    student = models.ForeignKey(Alumno, on_delete=models.DO_NOTHING)
    teacher = models.ForeignKey(UsuarioColegio, on_delete=models.DO_NOTHING)
    registration = models.DateField(default=date.today)
    attendance = models.BooleanField(default=False)

    def __str__(self):
        return str(self.registration)
    
class Notas(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.DO_NOTHING)
    nota = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(0)])
    student = models.ForeignKey(Alumno, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.nota)
     