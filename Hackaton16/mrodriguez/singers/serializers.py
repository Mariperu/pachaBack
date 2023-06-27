from rest_framework import serializers
from .models import Singer


class SingerModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Singer
        fields = "__all__"


class SingerSerilaizer(serializers.Serializer):
    def create(self, data):
        singer = Singer.objects.create(**data)
        return singer
