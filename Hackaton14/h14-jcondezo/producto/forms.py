from django import forms
from .models import Producto, Factura

class AddProducto(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('nombre', 'descripcion', 'cantidad', 'marca', 'precio', 'categoria')
        labels = {
            'nombre': 'Ingrese Nombre',
            'descripcion':'Ingrese Descripción',
            'cantidad': 'Ingrese Cantidad',
            'marca':'Ingrese Marca',
            'precio':'Ingrese Precio',
            'categoria': 'Seleccione Categoria'
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'descripcion': forms.TextInput(attrs={'class':'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class':'form-control'}),
            'marca': forms.TextInput(attrs={'class':'form-control'}),
            'precio': forms.TextInput(attrs={'class':'form-control'}),
            'categoria':forms.Select(attrs={'class':'form-control'}),
        }


class UpdateProducto(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('nombre', 'descripcion', 'cantidad', 'marca', 'precio', 'categoria')
        labels = {
            'nombre': 'Ingrese Nombre',
            'descripcion':'Ingrese Descripción',
            'cantidad': 'Ingrese Cantidad',
            'marca':'Ingrese Marca',
            'precio':'Ingrese Precio',
            'categoria': 'Seleccione Categoria'
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'descripcion': forms.TextInput(attrs={'class':'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class':'form-control'}),
            'marca': forms.TextInput(attrs={'class':'form-control'}),
            'precio': forms.TextInput(attrs={'class':'form-control'}),
            'categoria':forms.Select(attrs={'class':'form-control'}),
        }


class AddFactura(forms.ModelForm):
    class Meta:
        model = Factura
        fields = ('fecha', 'cliente', 'producto', 'Cantidad')
        labels = {
            'fecha': 'Ingrese Fecha',
            'cliente':'Ingrese Cliente',
            'producto': 'Ingrese Producto',
            'Cantidad':'Ingrese Cantidad',
            # 'MontoTotal': 'Ingrese MontoTotal'
        }
        widgets = {
            'fecha': forms.DateInput(
                format=('%d/%m/%Y'),
                attrs={'class': 'form-control', 
                       'placeholder': 'Select a date',
                       'type': 'date'  # <--- IF I REMOVE THIS LINE, THE INITIAL VALUE IS DISPLAYED
                      }),
            'cliente': forms.Select(attrs={'class':'form-control'}),
            'producto': forms.Select(attrs={'class':'form-control'}),
            'Cantidad': forms.NumberInput(attrs={'class':'form-control'}),
            # 'MontoTotal': forms.TextInput(attrs={'class':'form-control'}),
        }
