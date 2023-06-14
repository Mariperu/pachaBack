from django.forms import ModelForm
from .models import Matricula

class MatriculaForm(ModelForm):
    class Meta:
        model = Matricula
        fields = '__all__'
