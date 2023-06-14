from django.contrib import admin
from .models import Alumno, UsuarioColegio, Ciclo, Curso, Rol, Asistencia, Aula, Matricula, Notas
# Register your models here.
admin.site.register(Alumno)
admin.site.register(UsuarioColegio)
admin.site.register(Ciclo)
admin.site.register(Curso)
admin.site.register(Rol)
admin.site.register(Asistencia)
admin.site.register(Aula)
admin.site.register(Matricula)
admin.site.register(Notas)
