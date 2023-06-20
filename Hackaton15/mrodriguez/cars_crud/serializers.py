from rest_framework import serializers
from .models import Brand, Type, Car


class BrandSerializers(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"


class TypeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = "__all__"


class CarSerializers(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"
