
from django.shortcuts import render
from django.http import JsonResponse

def index(request):
    return render(request, 'index.html')

def realizar_venta(request):
    return JsonResponse({'message': 'Venta realizada correctamente'})
