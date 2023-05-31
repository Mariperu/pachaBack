from django.contrib import admin
from .models import Curso, Estudiante, Profesor
# Register your models here.
@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    pass

@admin.register(Estudiante)
class CursoAdmin(admin.ModelAdmin):
    pass

@admin.register(Profesor)
class CursoAdmin(admin.ModelAdmin):
    pass