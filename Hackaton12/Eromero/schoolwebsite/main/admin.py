from django.contrib import admin
from .models import Profesor, Estudiante, CursoLibre, SalaDeClase

admin.site.register(Profesor)
admin.site.register(Estudiante)
admin.site.register(CursoLibre)
admin.site.register(SalaDeClase)
