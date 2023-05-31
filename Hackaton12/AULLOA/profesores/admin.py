from django.contrib import admin

# Register your models here.
from .models import Alumnos, Profesores, Cursos, Clases
admin.site.register(Alumnos)
admin.site.register(Profesores)
admin.site.register(Cursos)
admin.site.register(Clases)