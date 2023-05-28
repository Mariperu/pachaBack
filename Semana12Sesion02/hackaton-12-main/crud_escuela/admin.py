from django.contrib import admin
from .models import Alumno, Curso, Matricula, Ciclo, Aula, Profesor
# Register your models here.
admin.site.register(Alumno)
admin.site.register(Curso)
admin.site.register(Matricula)
admin.site.register(Ciclo)
admin.site.register(Aula)
admin.site.register(Profesor)
