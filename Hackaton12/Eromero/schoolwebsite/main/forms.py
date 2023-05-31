from django import forms
from .models import Profesor, Estudiante, CursoLibre

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ['nombre', 'apellido', 'titulo', 'departamento', 'fecha_contratacion']

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre', 'apellido', 'fecha_inscripcion']

class CursoLibreForm(forms.ModelForm):
    class Meta:
        model = CursoLibre
        fields = ['nombre', 'descripcion', 'profesor']
