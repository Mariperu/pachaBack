from django import forms
from .models import Vuelo, TipoAsiento

class AddVuelo(forms.ModelForm):
    class Meta:
        model = Vuelo
        fields = ('fechaTakeOff','aeropuertoTakeOff','fechaLanding','aeropuertoLanding','avion')
        labels = {
            'aeropuertoTakeOff': 'Aereopuerto Origen',
            'fechaTakeOff':'Fecha de Ida',
            'fechaLanding': 'Fecha de Vuelta',
            'aeropuertoLanding':'Aereopurto Destino',
            'avion':'Avion'
        }
        widgets = {
            'aeropuertoTakeOff': forms.TextInput(attrs={'class':'form-control'}),
            'fechaTakeOff': forms.DateInput(
        format=('%Y-%m-%d'),
        attrs={'class': 'form-control', 
               'placeholder': 'Escoge el dia de tu vuelo',
               'type': 'date'
              }),
            'fechaLanding': forms.DateInput(
        format=('%Y-%m-%d'),
        attrs={'class': 'form-control', 
               'placeholder': 'Escoge el dia de retorno',
               'type': 'date'
              }),
            'aeropuertoLanding':forms.TextInput(attrs={'class':'form-control'}),
            
        }

class UpdateVuelo(forms.ModelForm):
    class Meta:
        model = Vuelo
        fields = ('fechaTakeOff','aeropuertoTakeOff','fechaLanding','aeropuertoLanding','avion')
        labels = {
            'aeropuertoTakeOff': 'Aereopuerto Origen',
            'fechaTakeOff':'Fecha de Ida',
            'fechaLanding': 'Fecha de Vuelta',
            'aeropuertoLanding':'Aereopurto Destino',
            'avion':'Avion'
        }
        widgets = {
            'aeropuertoTakeOff': forms.TextInput(attrs={'class':'form-control'}),
            'fechaTakeOff': forms.DateInput(
        format=('%Y-%m-%d'),
        attrs={'class': 'form-control', 
               'placeholder': 'Escoge el dia de tu vuelo',
               'type': 'date'
              }),
            'fechaLanding': forms.DateInput(
        format=('%Y-%m-%d'),
        attrs={'class': 'form-control', 
               'placeholder': 'Escoge el dia de retorno',
               'type': 'date'
              }),
            'aeropuertoLanding':forms.TextInput(attrs={'class':'form-control'}),
            
        }

class AddTipoAsiento(forms.ModelForm):
    class Meta:
        model = TipoAsiento
        fields = ('nombre',)
        labels = {
            'nombre': 'Tipo de Asiento',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            
        }
class UpdateTipoAsiento(forms.ModelForm):
    class Meta:
        model = TipoAsiento
        fields = ('nombre',)
        labels = {
            'nombre': 'Tipo de Asiento',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            
        }
