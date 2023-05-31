from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import *
from .forms import *
# Create your views here.

def index(request, template_name='appAdminColegio/index.html'):
    cursos = Curso.objects.all()
    datos = {"cursos": cursos}
    return render(request, template_name, datos)

def show_cursos(request, template_name='appAdminColegio/show_curso.html'):
    cursos = Curso.objects.all()
    profesores = Profesor.objects.all()
    alumnos = Alumno.objects.all()
    datos = {"cursos": cursos, "profesores": profesores, "alumnos": alumnos}
    return render(request, template_name, datos)

def crearCurso(request, template_name='appAdminColegio/crear_curso.html'):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('index')
    else:
        form = CursoForm()
        dato = {"form": form}
        return render(request, template_name, dato)

def contratarProfesor(request, template_name='appAdminColegio/contratar_profesor.html'):
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('index')
    else:
        form = ProfesorForm()
        dato = {"form": form}
        return render(request, template_name, dato)

def crearMatricula(request, template_name='appAdminColegio/crear_matricula.html'):
    if request.method == 'POST':
        form = MatriculaForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('index')
    else:
        form = MatriculaForm()
        dato = {"form": form}

        return render(request, template_name, dato)
def crearAlumno(request, template_name='appAdminColegio/crear_alumno.html'):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('index')
    else:
        form = AlumnoForm()
        dato = {"form": form}

        return render(request, template_name, dato)