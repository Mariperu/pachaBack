from django import forms
from .models import Autor

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['name','books','nacionalidad', 'tipoDocumento', 'numeroDocumento','sexo']