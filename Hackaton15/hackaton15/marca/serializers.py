# Django REST Framework
from rest_framework import serializers
# Model
from marca.models import Marca


class MarcaModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = (
            'pk',
            'nombre',
            'descripcion',
        )

class MarcaSerializer(serializers.Serializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    nombre = serializers.CharField(max_length=250)
    descripcion = serializers.CharField(max_length=10000)

    def create(self, data):
        marca = Marca.objects.create(**data)
        return marca

