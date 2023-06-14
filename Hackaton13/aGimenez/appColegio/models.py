from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    role_choices = (
        ('Profesor', 'Profesor'),
        ('Alumno', 'Alumno'),
        ('Administrador', 'Administrador')
    )
    role = models.CharField(max_length=15, choices=role_choices)
    cursos = models.ManyToManyField('Curso', related_name='usuarios')

    # Puedes agregar más campos personalizados según tus necesidades

class Curso(models.Model):
    CURSOS_CHOICE = (
        ("Algebra", "Algebra"),
        ("Algoritmos y Estructura de Datos", "Algoritmos y Estructura de Datos"),
        ("Algoritmos y Estructura de Datos II", "Algoritmos y Estructura de Datos II"),
        ("Probabilidad y Estadistica", "Probabilidad y Estadistica"),
        ("Administracion", "Administracion"),
        ("Sistemas y Organizaciones", "Sistemas y Organizaciones"),
        ("Logica y Matematica Computacional", "Logica y Matematica Computacional"),
        ("Base de Datos", "Base de Datos")
    )

    SALON_CHOICE = (
        ("102", "102"),
        ("103", "103"),
        ("104", "104"),
        ("105", "105"),
        ("106", "106"),
        ("107", "107"),
        ("108", "108"),
        ("109", "109"),
        ("110", "110"),
        ("111", "111"),
        ("112", "112")
    )

    nombre = models.CharField("Nombre Curso", max_length=50, choices=CURSOS_CHOICE)
    salon = models.CharField("Nombre Salon", max_length=5, choices=SALON_CHOICE)

    def __str__(self):
        return f"{self.nombre}, Salon: {self.salon}"

class Evaluacion(models.Model):
    tipo_choices= (
        ('Oral', 'Oral'),
        ('Escrito', 'Escrito')
    )
    profesor = models.ForeignKey('User', on_delete=models.CASCADE)
    curso = models.ForeignKey('Curso', on_delete=models.CASCADE)
    fecha = models.DateField()
    tipo = models.CharField(choices= tipo_choices)

    def __str__(self):
        return f'Curso {self.curso}'
class NotasAsistencia(models.Model):
    curso = models.ForeignKey('Evaluacion', on_delete=models.CASCADE)
    alumnos = models.ForeignKey('User', on_delete=models.CASCADE)
    asistencia_choices = (
        ('Inasistencia', 'Inasistencia'),
        ('Tardanza', 'Tardanza'),
        ('Asistencia', 'Asistencia')
    )
    asistencia = models.CharField(choices=asistencia_choices)
    nota = models.IntegerField()

    def __str__(self):
        return f' Asistencia: {self.asistencia}, Nota: {self.nota}'


