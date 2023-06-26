from django.shortcuts import render, get_list_or_404
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view
 
from .models import Tipo, Auto, Marca
from .serializers import TipoSerializer, MarcaSerializer, AutoSerializer
# Create your views here.
class TipoViewSet(viewsets.ModelViewSet):
    queryset = Tipo.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = TipoSerializer

class MarcaViewSet(viewsets.ModelViewSet):
    queryset = Marca.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = MarcaSerializer

class AutoViewSet(viewsets.ModelViewSet):
    queryset = Auto.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = AutoSerializer

@api_view(['GET'])
def TipoGetView(request):
    tipo = Tipo.objects.all()
    serializer = TipoSerializer(tipo, many = True)
    return Response(serializer.data)


@api_view(['POST'])
def TipoPostView(request):
    tipo_nombre = request.data.get('nombre')

    if not tipo_nombre:
        return Response({"msg": "Campo required"}, status=400)
    
    tipo = Tipo(nombre = tipo_nombre)
    tipo.save()
    return Response({"msg": "Listo broer"})


@api_view(['PUT'])
def TipoPutView(request, id):
    tipo = get_list_or_404(Tipo, id = id)
    tipo.nombre = request.data.get('nombre')
    tipo.save()

    return Response({'msg': 'Actualizado correctamente'})

@api_view(['DELETE'])
def TipoDeleteView(request, id):
    tipo = get_list_or_404(Tipo, id = id)
    tipo.delete()

    return Response({'msg': 'Deleteado correctamente'})



@api_view(['GET'])
def AutoFilterView(request, filter_value, tipo):

    if(filter_value == "tipo"):
        auto = Auto.objects.get(tipo = tipo)

    elif(filter_value == "marca"):
        auto = Auto.objects.get(marca = tipo)

    serializer = AutoSerializer(auto, many = True)
    return Response(serializer.data)