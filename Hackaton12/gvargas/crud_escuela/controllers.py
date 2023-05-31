from .forms import CursoForm
from django.shortcuts import redirect
from django.http import HttpResponseRedirect

def controlador_crear_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return True
        else:
            return False

def controlador_actualizar_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return True
        else:
            return False

def controlador_eliminar_curso(request, curso):
    if request.method == 'POST':
        curso.delete()
        return True
    else: 
        return False
