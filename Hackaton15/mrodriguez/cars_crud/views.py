from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from .models import Brand, Type, Car
from .serializers import BrandSerializers, TypeSerializers, CarSerializers


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = BrandSerializers


class TypeViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TypeSerializers


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CarSerializers


# GET (by brand)
@api_view(["GET"])
def BrandGetFilterView(req, brand):
    brands = Car.objects.filter(brand=brand)
    serializer = CarSerializers(brands, many=True)
    return Response(serializer.data)


# GET (by model)
@api_view(["GET"])
def ModelGetFilterView(req, model):
    models = Car.objects.filter(model=model)
    serializer = CarSerializers(models, many=True)
    return Response(serializer.data)


# Type CRUD
@api_view(["GET"])
def TypeGetView(req):
    types = Type.objects.all()
    serializer = TypeSerializers(types, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def TypePostView(req):
    name = req.data.get("name")

    if not name:
        return Response({"message": "Debe ingresar tipo."}, status=404)
    type = Type(name=name)
    type.save()
    return Response({"message": "Creado correctamente."})


@api_view(["PUT"])
def TypeUpdateView(req, id):
    type = get_object_or_404(Type, id=id)
    type.name = req.data.get("name")
    type.save()
    return Response({"message": "Actualizado correctamente."})


@api_view(["DELETE"])
def TypeDeleteView(req, id):
    type = get_object_or_404(Type, id=id)
    type.delete()
    return Response({"message": "Eliminado correctamente."})


# Brand CRUD
@api_view(["GET"])
def BrandGetView(req):
    brands = Brand.objects.all()
    serializer = BrandSerializers(brands, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def BrandPostView(req):
    name = req.data.get("name")
    if not name:
        return Response({"message": "Debe ingresar marca."}, status=404)
    brand = Brand(name=name)
    brand.save()
    return Response({"message": "Creado correctamente."})


@api_view(["PUT"])
def BrandUpdateView(req, id):
    brand = get_object_or_404(Brand, id=id)
    brand.name = req.data.get("name")
    brand.save()
    return Response({"message": "Actualizado correctamente."})


@api_view(["DELETE"])
def BrandDeleteView(req, id):
    brand = get_object_or_404(Brand, id=id)
    brand.delete()
    return Response({"message": "Eliminado correctamente."})


@api_view(["GET"])
def CarGetView(req):
    cars = Car.objects.all()
    serializer = CarSerializers(cars, many=True)
    return Response(serializer.data)


@api_view(["DELETE"])
def CarDeleteView(req, id):
    car = get_object_or_404(Car, id=id)
    car.delete()
    return Response({"message": "Eliminado correctamente."})
