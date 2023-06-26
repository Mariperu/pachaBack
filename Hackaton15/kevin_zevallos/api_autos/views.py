from django.shortcuts import render,get_object_or_404
from rest_framework import viewsets,permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Tipo,Marca,Auto
from .serializers import TipoSerializer,MarcaSerializer,AutoSerializer
# Create your views here.
class TipoViewSet(viewsets.ModelViewSet):
    queryset= Tipo.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class=TipoSerializer

class MarcaViewSet(viewsets.ModelViewSet):
    queryset= Marca.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class=MarcaSerializer

class AutoViewSet(viewsets.ModelViewSet):
    queryset= Auto.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class=AutoSerializer
@api_view(['GET'])
def TipoGetView(request):
    tipo = Tipo.objects.all()
    serializer= TipoSerializer(tipo,many=True)

@api_view(['POST'])
def TipoPostView(request):
    tipo_nombre = request.data.get('nombre') #nombre corresponde al campo que se desea obtener del modelo de datos creado
    if not tipo_nombre:
        return Response({"msg":"El campo nombre es requerido."})
    tipo=Tipo(nombre = tipo_nombre)
    tipo.save()
    return Response({"msg":"Creado correctamente."})
@api_view(['PUT'])
def TipoPutView(request,id):
    tipo = get_object_or_404(Tipo,id=id)
    tipo.nombre=request.data.get("nombre")
    tipo.save()
    return Response({"msg":"Tipo actualizado exitosamente."})

@api_view(['DELETE'])
def TipoDeleteView(request,id):
    tipo = get_object_or_404(Tipo,id=id)
    tipo.delete()
    return Response({"msg":"Tipo eliminado exitosamente."})
@api_view(['GET'])
def AutoFilterViewByYear(request,year):
    auto=Auto.objects.filter(year=year)
    serializer=AutoSerializer(auto,many=True)
    return Response(serializer.data)
@api_view(['GET'])
def AutoFilterView(request,filter_value,tipo):
    if filter_value == "tipo":
        auto=Auto.objects.filter(tipo=tipo)
    elif filter_value == "marca":
        auto=Auto.objects.filter(marca=tipo)
    elif filter_value =="color":
        auto=Auto.objects.filter(color=tipo)
    elif filter_value =="modelo":
        auto=Auto.objects.filter(modelo=tipo)
    serializer=AutoSerializer(auto,many=True)
    return Response(serializer.data)