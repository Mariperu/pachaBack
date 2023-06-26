from .models import Marca, Tipo, Auto
from rest_framework import viewsets, permissions
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MarcaSerializers, TipoSerializers, AutoSerializers
from rest_framework import generics

class MarcaViewSet(viewsets.ModelViewSet):
    queryset = Marca.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = MarcaSerializers

class TipoViewSet(viewsets.ModelViewSet):
    queryset = Tipo.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TipoSerializers

@api_view(['GET'])
def TipoGetFilterView(request, marca):
    # Realiza el filtrado utilizando los parámetros proporcionados
    tipos = Auto.objects.filter(marca=marca)

    # Serializa los resultados
    serializer = AutoSerializers(tipos, many=True)

    # Devuelve la respuesta con los datos serializados
    return Response(serializer.data)

@api_view(['GET'])
def TipoGetView(request):
    tipos = Tipo.objects.all()
    serializer = TipoSerializers(tipos, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def TipoPostView(request):
    tipo_nombre = request.data.get('nombre')

    # Validación de los datos enviados en la solicitud
    if not tipo_nombre:
        return Response({'message': 'Los campos "nombre" es obligatorio.'}, status=400)

    # Crear el nuevo tipo
    tipo = Tipo(nombre=tipo_nombre)
    tipo.save()

    return Response({'message': 'Tipo creado correctamente'})

@api_view(['PUT'])
def TipoUpdateView(request, id):
    tipo = get_object_or_404(Tipo, id=id)
    tipo.nombre = request.data.get('nombre')
    tipo.save()
    return Response({'message': 'Tipo actualizado correctamente'})


@api_view(['DELETE'])
def TipoDeleteView(request, id):
    tipo = get_object_or_404(Tipo, id=id)
    tipo.delete()
    return Response({'message': 'Tipo eliminado correctamente'})


class AutoViewSet(viewsets.ModelViewSet):
    queryset = Auto.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = AutoSerializers