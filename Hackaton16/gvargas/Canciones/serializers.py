from rest_framework import serializers
from .models import Song
from rest_framework import serializers, permissions

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'
        permission_classes = [permissions.AllowAny]
