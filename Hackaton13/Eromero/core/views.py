from django.shortcuts import render, redirect
from .models import User, Curso, Asistencia, Nota
from .forms import UserForm, CursoForm, AsistenciaForm, NotaForm

def index(request):
    return render(request, 'index.html')

def usuarios(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usuarios')
    else:
        form = UserForm()
    users = User.objects.all()
    return render(request, 'users.html', {'users': users, 'form': form})

def cursos(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cursos')
    else:
        form = CursoForm()
    cursos = Curso.objects.all()
    return render(request, 'cursos.html', {'cursos': cursos, 'form': form})

def asistencias(request):
    if request.method == 'POST':
        form = AsistenciaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('asistencias')
    else:
        form = AsistenciaForm()
    asistencias = Asistencia.objects.all()
    return render(request, 'asistencias.html', {'asistencias': asistencias, 'form': form})

def notas(request):
    if request.method == 'POST':
        form = NotaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notas')
    else:
        form = NotaForm()
    notas = Nota.objects.all()
    return render(request, 'notas.html', {'notas': notas, 'form': form})
