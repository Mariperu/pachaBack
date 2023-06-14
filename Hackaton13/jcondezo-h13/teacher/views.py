from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.http import require_http_methods
from .models import Notas, Asistencia
from .forms import NotaForm, AsistenciaForm

from django.core import serializers

# Create your views here.
def Home(request):
    data = Notas.objects.all()
    return render(request, 'notas/index.html', {'notas' : data })


@require_http_methods(["POST","GET"])
def crear_notas(request):
    if request.method == 'POST':
        nota_forms = NotaForm(request.POST)
        if nota_forms.is_valid():
            nota_forms.save()
            return redirect('teacher:index')
    else:
        nota_forms = NotaForm()

    return render(request, 'notas/crear_notas.html', {'nota_forms' : nota_forms })


def editar_nota(request, id):
    obj_format = Notas.objects.get(id=id)
    data = {
        'form': NotaForm(instance=obj_format)
    }

    if request.method == 'POST':
        form = NotaForm(data=request.POST, instance=obj_format)
        if form.is_valid():
            form.save()
            return redirect('teacher:index')
        data["form"] = form

    return render(request, 'notas/editar_notas.html', data)


def eliminar_nota(request, id):
    nota = get_object_or_404(Notas, id=id)
    nota.delete()
    return redirect('teacher:index')


# ASISTENCIA
def HomeAsistencia(request):
    data = Asistencia.objects.all()
    return render(request, 'asistencia/index.html', {'asistencia' : data })


@require_http_methods(["POST","GET"])
def crear_asistencia(request):
    if request.method == 'POST':
        asistenForm = AsistenciaForm(request.POST)
        if asistenForm.is_valid():
            asistenForm.save()
            return redirect('teacher:indexAsistencia')
    else:
        asistenForm = AsistenciaForm()

    return render(request, 'asistencia/crear_asisten.html', {'asistencia_forms' : asistenForm })


def editar_asistencia(request, id):
    obj_format = Asistencia.objects.get(id=id)
    data = { 'form': AsistenciaForm(instance=obj_format) }

    if request.method == 'POST':
        form = AsistenciaForm(data=request.POST, instance=obj_format)
        if form.is_valid():
            form.save()
            return redirect('teacher:indexAsistencia')
        data["form"] = form

    return render(request, 'asistencia/editar_asisten.html', data)


def eliminar_asistencia(request, id):
    asistencia = get_object_or_404(Asistencia, id=id)
    asistencia.delete()
    return redirect('teacher:indexAsistencia')

