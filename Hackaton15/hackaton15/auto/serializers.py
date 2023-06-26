# Django REST Framework
from rest_framework import serializers
# Model
from auto.models import Auto


class AutoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auto
        fields = (
            'pk',
            'modelo',
            'anio',
            'serial',
            'color',
            'motor',
            'transmision',
            'tipo',
            'marca'
        )

class AutoSerializer(serializers.Serializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    modelo = serializers.CharField(max_length=25)
    anio = serializers.IntegerField()
    serial = serializers.CharField(max_length=25)
    color = serializers.CharField(max_length=25)
    motor = serializers.CharField(max_length=25)
    transmision = serializers.CharField(max_length=25)
    tipo = serializers.IntegerField()
    marca = serializers.IntegerField()

    def create(self, data):
        auto = Auto.objects.create(**data)
        return auto
