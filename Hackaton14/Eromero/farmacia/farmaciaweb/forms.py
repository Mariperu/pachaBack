from django import forms
from .models import Compra, Producto, Cliente

class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ['producto', 'cantidad']
        widgets = {
            'producto': forms.Select(choices=Producto.objects.all()),
            'cantidad': forms.NumberInput(attrs={'min': 1, 'max': 100, 'value': 1}),
        }
