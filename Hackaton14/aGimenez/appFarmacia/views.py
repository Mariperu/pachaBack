from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages
from django.views.generic import TemplateView
from .forms import UserForm
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import render, redirect
from .models import Factura, DetalleFactura
from .forms import FacturaForm, DetalleFacturaFormSet
from django.http import JsonResponse
from django.views import View
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Factura


class IndexView(TemplateView):
    template_name = 'appFarmacia/index.html'


def registro(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado')
            return redirect('index')
    else:
        form = UserForm()

    context = { 'form' : form }
    return render(request, 'appFarmacia/registro.html', context)


class AddProductoView(CreateView):
    form_class = AddProducto
    template_name = 'appFarmacia/addProducto.html'
    success_url = '/producto'


class ListProductosView(ListView):
    model = Producto


class DetailProductosView(DetailView):
    model = Producto


class DeleteProductosView(DeleteView):
    model = Producto
    success_url ="/producto"
    template_name = "appFarmacia/confirm_delete.html"


class UpdateProductosView(UpdateView):
    model = Producto
    form_class = UpdateProducto
    success_url ="/producto"


class FacturaListView(ListView):
    model = Factura


class AddFacturaView(CreateView):
    form_class = AddFactura
    template_name = 'appFarmacia/addFactura.html'
    success_url = '/factura'


class DetailFacturasView(DetailView):
    model = Factura
    template_name = 'appFarmacia/factura_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        factura = self.get_object()
        detalles = factura.detallefactura_set.all()
        total = sum(detalle.cantProducto * detalle.precio for detalle in detalles)
        context['productos'] = detalles
        context['total'] = total
        return context


def cargar_factura(request):
    if request.method == 'POST':
        factura_form = FacturaForm(request.POST)
        detalle_formset = DetalleFacturaFormSet(request.POST)

        if factura_form.is_valid() and detalle_formset.is_valid():
            # Crear la factura
            cliente = factura_form.cleaned_data['cliente']
            factura = Factura(
                numero_factura=factura_form.cleaned_data['numero_factura'],
                cliente=cliente
            )
            factura.save()
            total = 0.0
            # Crear los detalles de la factura
            for detalle_form in detalle_formset:
                cantProducto = detalle_form.cleaned_data['cantProducto']
                nombre = detalle_form.cleaned_data['nombre']
                detalle=DetalleFactura(
                    factura=factura,
                    nombre=nombre,
                    precio=detalle_form.cleaned_data['precio'],
                    cantProducto=cantProducto
                )

                detalle.save()
                # Calcula Total
                total = total +detalle.subtotal

                # Obtiene el producto que se esta comprando y actualiza el stock
                producto = Producto.objects.get(nombre=nombre)
                if producto.stock >= cantProducto:
                    producto.stock = producto.stock - cantProducto
                else:
                    messages.success(request, f'El stock es menor a los productos necesarios')
                producto.save()

            # Busca el identificador en la base de datos
            # Si está creado actualiza los puntos
            # Si no, crea
            clientePuntos = Cliente.objects.filter(identificador=cliente).first()
            puntos = total / 10
            if clientePuntos:
                clientePuntos.puntos = clientePuntos.puntos + puntos
                clientePuntos.save()
            else:
                clientePuntos = Cliente(
                    identificador=cliente,
                    puntos=puntos
                )
                clientePuntos.save()

            return redirect('factura_list')

    else:
        factura_form = FacturaForm()
        detalle_formset = DetalleFacturaFormSet()

    context = {
        'form': factura_form,
        'detalles': detalle_formset
    }

    return render(request, 'appFarmacia/factura_form.html', context)


def buscar_producto(request):
    nombre = request.POST.get('nombre')
    producto = Producto.objects.filter(nombre=nombre).first()  # Assuming 'Product' is the model for products
    if producto:
        response = {
            'precio': producto.precio,
            'stock': producto.stock
        }
    else:
        response = {
            'error': 'Producto no encontrado'
        }

    return JsonResponse(response)


def buscar_cliente(request):
    identificador = request.POST.get('identificador')
    cliente = Cliente.objects.filter(identificador=identificador).first()
    if cliente:
        response = {
            'puntos': cliente.puntos,

        }
    else:
        response = {
            'error': 'Cliente no encontrado'
        }

    return JsonResponse(response)


class ExportarFacturaTXTView(View):

    def get(self, request, pk):
        try:
            factura = Factura.objects.get(pk=pk)
            contenido = f"Factura: {factura.numero_factura}\n"
            contenido += f"Fecha: {factura.created}\n"
            contenido += f"Cliente: {factura.cliente}\n"
            contenido += "\nDetalles:\n"

            total = 0.00
            for detalle in factura.detallefactura_set.all():
                contenido += f"Nombre: {detalle.nombre}\n"
                contenido += f"Precio: {detalle.precio}\n"
                contenido += f"Cantidad: {detalle.cantProducto}\n"
                contenido += f"Subtotal: s/{detalle.subtotal}\n"
                total += detalle.subtotal
                contenido += "\n"
            contenido += f"Total: s/{ total }\n"

            response = HttpResponse(content_type='text/plain')
            response['Content-Disposition'] = f'attachment; filename="factura_{factura.numero_factura}.txt"'
            response.write(contenido)
            return response
        except Factura.DoesNotExist:
            return HttpResponse("La factura no existe", status=404)