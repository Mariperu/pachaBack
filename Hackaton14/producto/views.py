from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.core import serializers

from .forms import AddProducto, UpdateProducto, AddFactura
from .models import Producto, Factura, Cliente

import json

# Create your views here.
class IndexView(generic.TemplateView):
    template_name = 'producto/index.html'

class AddProducto(CreateView):
    form_class = AddProducto
    template_name = 'producto/addProducto.html'
    success_url = '/producto/prod'

class ListProductoView(ListView):
    model = Producto

class UpdateProductos(UpdateView):
    model = Producto
    form_class = UpdateProducto
    success_url ="/producto/prod"

class DeleteProductos(DeleteView):
    model = Producto
    success_url ="/producto/prod"
    template_name = "producto/confirm_delete.html"

class ListBoleta(ListView):
    model = Factura


def registrar_boleta(request):
    if request.method == 'POST':
        form = AddFactura(request.POST)
        product = Producto.objects.get(id=request.POST['producto'])
        product.cantidad = int(product.cantidad) - int(request.POST['Cantidad'])
        product.save()
        montoTotal_ = float(product.precio)*float(request.POST['Cantidad'])
        if form.is_valid():
            post = form.save(commit=False)
            post.montoTotal = montoTotal_
            post.save()

            if(montoTotal_ >= 10):
                pts = int(montoTotal_) // 10
                data = Cliente.objects.filter(id=request.POST['cliente'])
                format_data = serializers.serialize('json', data, indent=2, use_natural_foreign_keys=True)
                format_data = json.loads(format_data)
                for d in format_data:
                    cliente = Cliente.objects.get(id=d['pk'])
                    cliente.puntos = pts+d['fields']['puntos']
                    cliente.save()

            return redirect('producto:view_boleta')

    else:
        form = AddFactura()

    return render(request, 'producto/addFactura.html', {'form' : form })


class ListClienteView(ListView):
    model = Cliente