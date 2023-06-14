from rest_framework import serializers
from .models import Asistencia, Notas, Curso

class AssistenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asistencia
        fields = '__all__'

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class NotasSerializer(serializers.ModelSerializer):
    curso = CursoSerializer()
    class Meta:
        model = Notas
        fields = '__all__'