from django.shortcuts import render, redirect
from .models import Curso
from .forms import CursoForm
from .controllers import controlador_crear_curso, controlador_actualizar_curso, controlador_eliminar_curso
# Create your views here.

def home(request):
    cursos = Curso.objects.all()
    context = {'cursos': cursos}
    return render(request, 'crud_escuela/cursos_lista.html', context)

def detalle_curso(request, id):
    cursos = Curso.objects.get(id=id) 
    context = {'curso': cursos}
    return render(request, 'crud_escuela/curso_detalle.html', context)

def crear_curso(request):
    form = CursoForm()

    if controlador_crear_curso(request):
        return redirect('home')
    
    context = {'form': form}
    return render(request, 'crud_escuela/form_curso.html', context)

def actualizar_curso(request, id):
    curso = Curso.objects.get(id=id)
    form = CursoForm(instance=curso)
    if controlador_actualizar_curso(request):
        return redirect('home')
    context = {'form': form}
    return render(request, 'crud_escuela/form_curso.html', context)

def eliminar_curso(request, id):
    curso = Curso.objects.get(id=id)
    if controlador_eliminar_curso(request, curso):
        return redirect('home')
    context = {'obj': curso}
    return render(request, 'crud_escuela/eliminar.html', context)
