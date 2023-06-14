from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import SignUpform, LoginForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Product, Sale, Client
from rest_framework import generics
from .serializers import SaleSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.serializers import ListSerializer
from .helpers import generar_boleta_venta
from django.utils import timezone
from django.core import serializers
import json

# Create your views here.
def home(request):
    return HttpResponse('Server is running...')

def login_app(request):
    page = 'login'
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password = password)
            print(user.is_admin, user.is_seller)
            if user is not None and user.is_admin:
                login(request, user)
                return redirect('admin_farmacia')
            else:
                login(request, user)
                return redirect('seller')
        else:
            msg = 'invalid form' 
    context = {'page': page, 'form': form}
    return render(request, 'pages/login_register.html', context)

def register(request):
    form = SignUpform()
    if request.method == 'POST':
        form = SignUpform(request.POST)
        if form.is_valid():
            user = form.save()  
            msg = 'Create User correct! '
            return redirect('login_app')
    context = {"form": form }
    return render(request, 'pages/login_register.html', context)

@login_required(login_url='login')
def is_admin(request):

    return render(request, 'pages/page_admin.html')

@login_required(login_url='login')
def is_seller(request):
    # tiene acceso al crud de productos
    productos = Product.objects.all()
    print(productos)
    context = {"productos": productos}
    return render(request, 'pages/page_seller.html', context)

@api_view(['POST'])
def reggister_sale(request, id_cliente, id_producto):
    serializer = SaleSerializer(data=request.data)
    if serializer.is_valid():    
        id_client = get_object_or_404(Client, id = id_cliente)
        id_producto = get_object_or_404(Product, id = id_producto)

        total = request.data.get('total')
        quantity = request.data.get('quantity')
        sale = Sale(id_client = id_client, id_product = id_producto, total = total, quantity = quantity)    
        sale.save()
        nombre_archivo = id_cliente+str(sale.created)+ '.txt'
        generar_boleta_venta(nombre_archivo,id_producto)
        return HttpResponse('Venta registrada correctamente')
    else:
        return HttpResponse('Venta no registrada')

@api_view(['GET'])
def getReporte(request, id_producto):
    product = get_object_or_404(Product, id=id_producto)
    sales = Sale.objects.filter(id_product=product)
    serializer = SaleSerializer(sales, many=True)
    list_serializer = ListSerializer(child=serializer)
    serialized_data = list_serializer.data
    return Response(serializer.data)
