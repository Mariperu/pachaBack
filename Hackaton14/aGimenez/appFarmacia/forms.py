from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import formset_factory
from .models import *
from django.forms import ModelForm
from appFarmacia.models import User


class UserForm(UserCreationForm):
    role = forms.Select()
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'role', 'password1', 'password2']


class AddProducto(ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'


class UpdateProducto(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'


class AddFactura(ModelForm):
    class Meta:
        model = Factura
        fields = '__all__'


class DetalleFacturaForm(forms.Form):
    nombre = forms.CharField(label='Nombre Producto')
    precio = forms.FloatField(label='Precio')
    cantProducto = forms.IntegerField(label='cantProducto')


class FacturaForm(forms.Form):
    numero_factura = forms.CharField(label='Número de Factura')
    cliente = forms.CharField(label='Cliente')
    detalles = forms.formsets.formset_factory(DetalleFacturaForm)


DetalleFacturaFormSet = formset_factory(DetalleFacturaForm, extra=1)