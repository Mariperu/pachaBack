from django import forms
from django.forms import ModelForm
from .models import Matricula, Curso, Alumno, Profesor

class CursoForm(ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'
        widgets = {'nombre': forms.Select(attrs={'class': 'form-control input'}),
                   'salon': forms.Select(attrs={'class': 'form-control input'})
                   }

class ProfesorForm(ModelForm):
    class Meta:
        model = Profesor
        fields = '__all__'
        widgets = {'nombre': forms.TextInput(attrs={'class': 'form-control input', 'text-transform': 'capitalize', 'placeholder': 'Nombre Profesor'}),
                   'identifProfesor': forms.TextInput(attrs={'class': 'form-control input', 'text-transform': 'capitalize'}),
                   'correo': forms.TextInput(attrs= {'class': 'form-control input'}),
                   'dni': forms.TextInput(attrs= {'type': 'number', 'class': 'form-control input'}),
                   'edad': forms.TextInput(attrs={'type': 'number','class': 'form-control input'}),
                   'experiencia': forms.TextInput(attrs={'type': 'number', 'class': 'form-control input'}),
                   'curso_id': forms.Select(attrs={'class': 'form-control input'})
                   }

class AlumnoForm(ModelForm):
    class Meta:
        model = Alumno
        fields = '__all__'
        widgets = {'nombre': forms.TextInput(attrs={'class': 'form-control input', 'text-transform': 'capitalize', 'placeholder': 'Nombre Alumno'}),
                   'identifAlumno': forms.TextInput(attrs={'class': 'form-control input', 'text-transform': 'capitalize'}),
                   'correo': forms.TextInput(attrs= {'class': 'form-control input'}),
                   'dni': forms.TextInput(attrs= {'type': 'number', 'class': 'form-control input'}),
                   'edad': forms.TextInput(attrs={'type': 'number','class': 'form-control input'}),
                   'curso_id': forms.Select(attrs={'class': 'form-control input'})
                   }

class MatriculaForm(ModelForm):
    class Meta:
        model = Matricula
        fields = '__all__'
        widgets = {'nroMatricula': forms.TextInput(attrs={'type': 'number', 'class': 'form-control input'}),
                   'periodoLectivo': forms.TextInput(attrs={'class': 'form-control input'}),
                   'identifAlumno': forms.Select(attrs={'class': 'form-control input'})
                   }