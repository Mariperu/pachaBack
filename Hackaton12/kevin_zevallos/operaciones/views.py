from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Curso

def home(request):
    cursos = Curso.objects.all()  # Obtener todos los cursos libres
    for curso in cursos:
        print(curso.nombre)
    return render(request, 'colegio/home.html', {'cursos': cursos})
