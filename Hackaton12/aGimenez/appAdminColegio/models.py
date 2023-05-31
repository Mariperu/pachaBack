from django.db import models

# Create your models here.
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
class Curso(models.Model):
    nombre = models.CharField("Nombre Curso", max_length=50, choices=CURSOS_CHOICE)
    salon = models.CharField("Nombre Salon", max_length=5, choices=SALON_CHOICE)

    def __str__(self):
        return f"Nombre del Curso: {self.nombre}, Nombre Salon: {self.salon}"

class Alumno(models.Model):
    nombre = models.CharField(max_length=30, verbose_name='Nombre')
    identifAlumno = models.CharField(max_length=12, verbose_name='Identificador')
    correo = models.EmailField(verbose_name='Correo')
    dni = models.IntegerField(verbose_name='DNI')
    edad = models.IntegerField(verbose_name='Edad')
    curso_id = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return f"Nombre: {self.nombre}, Identificador: {self.identifAlumno}"

class Profesor(models.Model):
    nombre = models.CharField(max_length=30, verbose_name='Nombre')
    identifProfesor = models.CharField(max_length=12, verbose_name='Identificador')
    correo = models.EmailField(verbose_name='Correo')
    dni = models.IntegerField(verbose_name='DNI')
    edad = models.IntegerField(verbose_name='Edad')
    experiencia = models.IntegerField(verbose_name='Años Experiencia')
    curso_id = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return f"Nombre: {self.nombre}, Identificador: {self.identifProfesor}"

    class Meta:
        verbose_name_plural = 'Profesores'
class Matricula(models.Model):
    nroMatricula = models.IntegerField(verbose_name='Numero Matricula')
    periodoLectivo = models.CharField(max_length=20, verbose_name='Periodo Lectivo')
    identifAlumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)

    def __str__(self):
        return f"Nro Matricula: {self.nroMatricula}, Periodo Lectivo: {self.periodoLectivo}, Identificador Alumno: {self.identifAlumno}"


