from rest_framework import serializers
from .models import User


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserSerilaizer(serializers.Serializer):
    def create(self, data):
        user = User.objects.create(**data)
        return user
