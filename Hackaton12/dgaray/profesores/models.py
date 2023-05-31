import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Alumnos(models.Model):
    alumnos_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    def __str__(self):
        return self.alumnos_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
class Profesores(models.Model):
    profesores_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    def __str__(self):
        return self.profesores_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
class Cursos(models.Model):
    cursos_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    def __str__(self):
        return self.cursos_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Clases(models.Model):
    profesor = models.ForeignKey(Profesores, on_delete=models.CASCADE)
    alumno = models.ForeignKey(Alumnos, on_delete=models.CASCADE)
    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE)
    curso_text = models.CharField(max_length=200)
    def __str__(self):
        return self.curso_text