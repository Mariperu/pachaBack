from django.shortcuts import render
from django.views import View
from .models import Curso, Estudiante, Profesor

class CursoListView(View):
    def get(self, request):
        cursos = Curso.objects.all()
        return render(request, 'courses/list.html', {'cursos': cursos})

class EstudianteCreateView(View):
    def post(self, request, curso_id):
        curso = Curso.objects.get(id=curso_id)
        if curso.estudiante_set.count() < curso.limite_estudiantes:
            nombre_estudiante = request.POST.get('nombre')
            Estudiante.objects.create(nombre=nombre_estudiante, curso=curso)
        return redirect('curso_list')

class ProfesorCreateView(View):
    def post(self, request, curso_id):
        curso = Curso.objects.get(id=curso_id)
        nombre_profesor = request.POST.get('nombre')
        Profesor.objects.create(nombre=nombre_profesor, curso=curso)
        return redirect('curso_list')