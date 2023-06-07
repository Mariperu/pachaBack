from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Profesor, Alumno, Asistencia, Nota


@login_required
def profesor_dashboard(request):
    profesor = Profesor.objects.get(user=request.user)
    cursos = profesor.cursos.all()
    # Realiza las operaciones necesarias y renderiza el template correspondiente


@login_required
def alumno_dashboard(request):
    alumno = Alumno.objects.get(user=request.user)
    asistencias = Asistencia.objects.filter(alumno=alumno)
    notas = Nota.objects.filter(alumno=alumno)
    # Realiza las operaciones necesarias y renderiza el template correspondiente


@login_required
def administrador_dashboard(request):
    # Realiza las operaciones necesarias y renderiza el template correspondiente
    pass
