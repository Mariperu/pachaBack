from django import forms
from .models import Notas, Asistencia

class NotaForm(forms.ModelForm):
    class Meta:
        model = Notas
        fields = ['periodo','curso','alumno', 'nota1', 'nota2','nota3', 'nota4', 'promedio']


class AsistenciaForm(forms.ModelForm):
    class Meta:
        model = Asistencia
        fields = ['periodo','curso','alumno', 'a1', 'a2','a3', 'a4']
