from django.contrib import admin
from .models import Nacionalidad, Sexo, DocumentoIdentidad, Administrador, Alumno, Curso, Profesor, Periodo, Notas
# Register your models here.
admin.site.register(Sexo)
admin.site.register(Nacionalidad)
admin.site.register(DocumentoIdentidad)
admin.site.register(Administrador)
admin.site.register(Alumno)
admin.site.register(Curso)
admin.site.register(Profesor)
admin.site.register(Periodo)
admin.site.register(Notas)
