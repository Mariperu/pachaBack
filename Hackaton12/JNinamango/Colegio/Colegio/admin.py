from django.contrib import admin
from .models import  Curso,Alumno,Profesor
# Register your models here.
admin.site.register(Curso)
admin.site.register(Alumno)
admin.site.register(Profesor)