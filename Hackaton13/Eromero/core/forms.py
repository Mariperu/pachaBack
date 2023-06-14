from django import forms
from .models import User, Curso, Asistencia, Nota

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'role']

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre', 'profesor']

class AsistenciaForm(forms.ModelForm):
    class Meta:
        model = Asistencia
        fields = ['alumno', 'curso', 'fecha', 'presente']

class NotaForm(forms.ModelForm):
    class Meta:
        model = Nota
        fields = ['alumno', 'curso', 'nota']
