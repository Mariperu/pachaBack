from rest_framework import serializers
from .models import Tipo, Marca, Auto

class TipoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tipo 
        fields = '__all__'
        read_only_fields =  ('id', )

class MarcaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = '__all__'
        read_only_fields =  ('id', )

class AutoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Auto
        fields = '__all__'
        read_only_fields =  ('id', )

    