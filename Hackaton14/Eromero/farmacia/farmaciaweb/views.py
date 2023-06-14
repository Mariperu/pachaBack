from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from .models import Producto, Compra, Cliente
from .forms import CompraForm
from django.http import HttpResponse

@login_required
@permission_required('auth.view_user', raise_exception=True)
def dashboard(request):
    """ Vista para el  """
    return render(request, 'farmaciaweb/dashboard.html')

@login_required
@permission_required('farmaciaweb.view_producto', raise_exception=True)
def ver_productos(request):
    """ Vista para el cajero para ver los productos """
    productos = Producto.objects.all()
    return render(request, 'farmaciaweb/ver_productos.html', {'productos': productos})

@login_required
@permission_reqadministradoruired('farmaciaweb.add_compra', raise_exception=True)
def realizar_compra(request, cliente_id):
    """ Vista para el cajero para realizar una compra """
    cliente = Cliente.objects.get(id=cliente_id)
    if request.method == 'POST':
        form = CompraForm(request.POST)
        if form.is_valid():
            compra = form.save(commit=False)
            compra.cliente = cliente
            compra.save()
            return redirect('ver_productos')
    else:
        form = CompraForm()
    return render(request, 'farmaciaweb/realizar_compra.html', {'form': form, 'cliente': cliente})

@login_required
@permission_required('farmaciaweb.export_report', raise_exception=True)
def export_report(request):
    """ Vista para exportar un reporte en formato TXT """
    # Lógica para generar el reporte en formato TXT
    report_data = "Este es el contenido del reporte TXT que se exportará."
    
    # Configuración de la respuesta HTTP
    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename="reporte.txt"'

    # Escritura del contenido del reporte en la respuesta
    response.write(report_data)

    return response
