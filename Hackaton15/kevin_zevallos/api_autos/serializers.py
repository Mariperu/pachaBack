from rest_framework import serializers
from .models import Tipo,Marca,Auto
class TipoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tipo
        fields = '__all__'

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Marca
        fields = '__all__'

class AutoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Auto
        fields = '__all__'