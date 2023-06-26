from django.shortcuts import get_list_or_404, render
from .serializer import *
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.decorators import api_view
from .serializer import *

class SongViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Song.objects.all()
    serializer_class = SongSerializer


@api_view(['GET'])
def SongGetView(request):
    tipo = Song.objects.all()
    serializer = SongSerializer(tipo, many = True)
    return Response(serializer.data)


@api_view(['POST'])
def SongPostView(request):
    tipo_nombre = request.data.get('nombre')

    if not tipo_nombre:
        return Response({"msg": "Campo required"}, status=400)
    
    tipo = Song(nombre = tipo_nombre)
    tipo.save()
    return Response({"msg": "Listo broer"})


@api_view(['PUT'])
def SongPutView(request, id):
    tipo = get_list_or_404(Song, id = id)
    tipo.nombre = request.data.get('nombre')
    tipo.save()

    return Response({'msg': 'Actualizado correctamente'})


@api_view(['DELETE'])
def SongDeleteView(request, id):
    tipo = get_list_or_404(Song, id = id)
    tipo.delete()

    return Response({'msg': 'Deleteado correctamente'})
