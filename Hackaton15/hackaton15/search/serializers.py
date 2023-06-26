# Django REST Framework
from rest_framework import serializers

# Models
from users.models import User
from auto.models import Auto
from marca.models import Marca
from tipo.models import Tipo


class TipoAutomovilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo
        fields = (
            'nombre',
            'descripcion',
        )


class MarcaAutomovilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = (
            'nombre',
            'descripcion'
        )


class AutoAutomovilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auto
        fields = (
            'modelo',
            'anio',
            'serial',
            'color',
            'motor',
            'transmision',
            'tipo',
            'marca'
        )


class TiendaSerializer(serializers.ModelSerializer):

    tipo = TipoAutomovilSerializer(many=True)
    marca = MarcaAutomovilSerializer(many=True)
    auto = AutoAutomovilSerializer(many=True)

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'tipo',
            'marca',
            'auto',
        )