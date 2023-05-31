from django.contrib import admin

# Register your models here.
from .models import Alumno, Profesor, Salon, Curso, Matricula
admin.site.register(Alumno)
admin.site.register(Profesor)
admin.site.register(Salon)
admin.site.register(Curso)
admin.site.register(Matricula)
