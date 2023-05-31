from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Alumno, Profesor, Curso, Matricula, SalaClase

admin.site.register(Alumno)
admin.site.register(Profesor)
admin.site.register(Curso)
admin.site.register(Matricula)
admin.site.register(SalaClase)
