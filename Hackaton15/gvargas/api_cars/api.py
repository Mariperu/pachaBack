from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Tipo, Marca, Auto
from .serializers import TipoSerializer, MarcaSerializer, AutoSerializer
from rest_framework import generics

# Create your views here.

class TipoViewSet(viewsets.ModelViewSet):
    queryset = Tipo.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializar_class = TipoSerializer

class MarcaViewSet(viewsets.ModelViewSet):
    queryset = Marca.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializar_class = MarcaSerializer

class AutoViewSet(viewsets.ModelViewSet):
    queryset = Auto.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializar_class = AutoSerializer

@api_view(['GET'])
def TipoGetView(request):
    tipo =Tipo.objects.all()
    serializer = TipoSerializer(tipo, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def TipoPostView(request):
    tipo_nombre = request.data.get('nombre')
    
    if not tipo_nombre:
        return Response({"msg": "El campo nombre es requerido."}, status=400)
    tipo = Tipo(nombre = tipo_nombre)
    tipo.save()
    return Response({"msg": "Tipo creado correctamente."})

@api_view(['PUT'])
def TipoPutView(request, id):
    tipo = get_object_or_404(Tipo, id = id)
    tipo.nombre = request.data.get("nombre")
    tipo.save()
    return Response({"msg": "Tipo actualizado correctamente."})

@api_view(['DELETE'])
def TipoDeleteView(request, id):
    tipo = get_object_or_404(Tipo, id = id)
    tipo.delete()
    return Response({"msg": "Tipo eliminado correctamente."})

@api_view(['GET'])
def AutoFilterView(request, filter_value, tipo):
    if filter_value == "tipo":
        auto = Auto.objects.filter(tipo = tipo)
    elif filter_value == "marca":
        auto = Auto.objects.filter(marca = tipo)
    serializer = AutoSerializer(auto, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def TipoGetFilterView(request, marca):
    # Realiza el filtrado utilizando los parámetros proporcionados
    tipos = Auto.objects.filter(marca=marca)

    # Serializa los resultados
    serializer = AutoSerializer(tipos, many=True)

    # Devuelve la respuesta con los datos serializados
    return Response(serializer.data)

@api_view(['GET'])
def AutoGetView(request):
    auto =Auto.objects.all()
    serializer = AutoSerializer(auto, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def AutoPostView(request):
    auto_color = request.data.get('color')
    auto_year = request.data.get('year')
    auto_modelo = request.data.get('modelo')
    auto_img = request.data.get('img_apth')
    
    if not auto_color:
        return Response({"msg": "El campo nombre es requerido."}, status=400)
    if not auto_year:
        return Response({"msg": "El campo nombre es requerido."}, status=400)
    if not auto_modelo:
        return Response({"msg": "El campo nombre es requerido."}, status=400)
    if auto_img:
        auto = Auto(color = auto_color, year = auto_year, modelo = auto_modelo, img_apth = auto_img)
        auto.save()
        return Response({"msg": "Auto creado correctamente."})
    auto = Auto(color = auto_color, year = auto_year, modelo = auto_modelo)
    auto.save()
    return Response({"msg": "Auto creado correctamente."})

@api_view(['PUT'])
def AutoPutView(request, id):
    auto = get_object_or_404(Auto, id = id)
    auto.color = request.data.get("color")
    auto.year = request.data.get("year")
    auto.modelo = request.data.get("modelo")
    auto.img_apth = request.data.get("img_apth") 
    auto.save()
    return Response({"msg": "Auto actualizado correctamente."})

@api_view(['DELETE'])
def AutoDeleteView(request, id):
    auto = get_object_or_404(Tipo, id = id)
    auto.delete()
    return Response({"msg": "Auto eliminado correctamente."})

@api_view(['GET'])
def MarcaGetView(request):
    marca =Marca.objects.all()
    serializer = MarcaSerializer(marca, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def MarcaPostView(request):
    marca_nombre = request.data.get('nombre')
    
    if not marca_nombre:
        return Response({"msg": "El campo nombre es requerido."}, status=400)
    marca = Marca(nombre = marca_nombre)
    marca.save()
    return Response({"msg": "Marca creada correctamente."})

@api_view(['PUT'])
def MarcaPutView(request, id):
    marca = get_object_or_404(Tipo, id = id)
    marca.nombre = request.data.get("nombre")
    marca.save()
    return Response({"msg": "Marca actualizada correctamente."})

@api_view(['DELETE'])
def MarcaDeleteView(request, id):
    marca = get_object_or_404(Tipo, id = id)
    marca.delete()
    return Response({"msg": "Marca eliminada correctamente."})
