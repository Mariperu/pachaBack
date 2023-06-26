# Django REST Framework
from rest_framework import serializers
# Model
from tipo.models import Tipo

class TipoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo
        fields = (
            'pk',
            'nombre',
            'descripcion',
        )

class TipoSerializer(serializers.Serializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    nombre = serializers.CharField(max_length=250)
    descripcion = serializers.CharField(max_length=10000)

    def create(self, data):
        tipo = Tipo.objects.create(**data)
        return tipo

