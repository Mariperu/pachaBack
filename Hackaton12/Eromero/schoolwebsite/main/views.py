from django.contrib.auth.decorators import login_required
from .models import Profesor, Estudiante, CursoLibre, SalaDeClase
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import ProfesorForm, EstudianteForm


def home(request):
    cursos = CursoLibre.objects.all()
    return render(request, 'home.html', {'cursos': cursos})

@login_required
def matricular(request, curso_id):
    curso = get_object_or_404(CursoLibre, id=curso_id)
    estudiantes = Estudiante.objects.all()
    return render(request, 'matricular.html', {'curso': curso, 'estudiantes': estudiantes})

@login_required
def do_matriculacion(request, curso_id, estudiante_id):
    curso = get_object_or_404(CursoLibre, id=curso_id)
    estudiante = get_object_or_404(Estudiante, id=estudiante_id)
    curso.estudiantes.add(estudiante)
    return redirect('home')

def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            # Return an 'invalid login' error message.
            pass 
    else:
        return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('home')

def registro_profesor(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redireccionar a la página principal después de registrar al profesor
    else:
        form = ProfesorForm()
    return render(request, 'registro_profesor.html', {'form': form})

def registro_estudiante(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redireccionar a la página principal después de registrar al estudiante
    else:
        form = EstudianteForm()
    return render(request, 'registro_estudiante.html', {'form': form})

def sala_clase(request, id):
    sala = SalaDeClase.objects.get(id=id)
    estudiantes = sala.estudiantes.all()
    return render(request, 'sala_clase.html', {'sala': sala, 'estudiantes': estudiantes})
