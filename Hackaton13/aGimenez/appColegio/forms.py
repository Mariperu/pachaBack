from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import *
from django.forms import ModelForm
from appColegio.models import User
class UserForm(UserCreationForm):

    role = forms.Select()

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'first_name', 'last_name', 'role', 'password1', 'password2', 'cursos']
class CursoForm(ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'
        widgets = {'nombre': forms.Select(),
                   'salon': forms.Select()
                   }

class EvaluacionForm(ModelForm):
    class Meta:
        model = Evaluacion
        fields = '__all__'
        widgets = {
            'profesor': forms.HiddenInput()
        }
class NotasAsistenciaForm(ModelForm):
    class Meta:
        model = NotasAsistencia
        fields = '__all__'
        widgets = {
            'curso': forms.HiddenInput(),
            'alumnos': forms.HiddenInput()
        }