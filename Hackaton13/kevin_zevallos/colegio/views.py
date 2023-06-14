from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Curso, UsuarioColegio, Matricula, Alumno, Aula, Asistencia, Rol, Notas
from datetime import date
from rest_framework import generics
from .serializers import AssistenciaSerializer, NotasSerializer
from .forms import MatriculaForm
from itertools import chain
# Create your views here.

def home(request):
    getCourses = list(Curso.objects.all())
    context = {'courses': getCourses}
    return render(request, 'pages/home.html', context)

def login(request):
    page = 'login'
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        try:
            encontrar_Usuario_teacher = UsuarioColegio.objects.get(name = nombre)
            return redirect('dashboard', id_usuario  = encontrar_Usuario_teacher.id)
        except:
            encontrar_estudiante = Alumno.objects.get(name = nombre)
            # return redirect('calendar', alumno_id = encontrar_estudiante.id )
            return redirect('alumno', alumno_id = encontrar_estudiante.id)
         
    context = {'page': page}
    return render(request, 'pages/login_register.html', context)

def register(request):
    return render(request, 'pages/login_register.html')

def dashboard(request, id_usuario):
    alumnos = []
    encontrar_Usuario = UsuarioColegio.objects.get(id = id_usuario)
    # print(type(encontrar_Usuario.rol))
    rol = Rol.objects.get( name = encontrar_Usuario.rol)
    if rol.name != 'Profesor':
        return redirect('matricular')
    else: 
        encontrar_alumnos_matriculados = list(Matricula.objects.filter(teacher_id = id_usuario))
        for matriculados in encontrar_alumnos_matriculados:
            encontrar_alumno = Alumno.objects.get(id = matriculados.student_id)
            encontar_aula = Aula.objects.get(id=matriculados.section_id)
            asistencia = Asistencia.objects.filter(student = matriculados.student_id, teacher = id_usuario, attendance=True, registration=date.today())
            if asistencia.exists():
                asistioAlumno = True
            else:
                asistioAlumno = False

            alumno = {
                'id': encontrar_alumno.id,
                'name': encontrar_alumno.name,
                'section': encontar_aula.name,
                'email': encontrar_alumno.email,
                'img_path': encontrar_alumno.img_path,
                'asistio': asistioAlumno
            }
            alumnos.append(alumno)

        context = {'usuario':encontrar_Usuario, 'estudiantes': alumnos}

        return render(request, 'pages/dashboard.html', context)

def marcar_asistencia(request, id_profesor, id_alumno):
    alumno = get_object_or_404(Alumno, id  = id_alumno)
    profesor = get_object_or_404(UsuarioColegio, id  = id_profesor)

    asistencia = Asistencia(student = alumno, teacher = profesor, attendance = True)
    asistencia.save()

    return HttpResponse('Registrado en la tabla de Asistencia correctamente. ')

def calendar(request, alumno_id):
    context = {'id': alumno_id}
    return render(request, 'pages/calendar.html', context)

def notas(request, alumno_id):
    context = {'id': alumno_id}
    return render(request, 'pages/notas.html', context)

def matricular_alumno(request):
    form = MatriculaForm()
    if request.method == 'POST':
        form = MatriculaForm(request.POST)
        if form.is_valid():
            formitems = form.cleaned_data
            curso = Curso.objects.get(name=formitems['course'])
            profesor = UsuarioColegio.objects.get(name=formitems['teacher'])
            
            profesor.availability = profesor.availability - 1 
            curso.availability = curso.availability - 1 
            
            curso.save()
            profesor.save()
            form.save()
            return HttpResponse('matriculado correctamente')
    context = {'form': form}
    return render(request, 'pages/matricula_form.html', context)

def alumno(request, alumno_id):
    getAlumno = Alumno.objects.get(id = alumno_id)

    context  = {'alumno': getAlumno}

    return  render(request, 'pages/student.html', context)

class AsistenciaList(generics.ListAPIView):
    serializer_class = AssistenciaSerializer

    def get_queryset(self):
        alumno = self.kwargs['alumno_id']
        print(alumno)
        queryset = Asistencia.objects.filter(student_id = alumno)
        print(queryset)
        return queryset
    
class NotasList(generics.ListAPIView):
    serializer_class = NotasSerializer

    def get_queryset(self):
        alumno = str(self.kwargs['alumno_id'])
        queryset_notas = Notas.objects.filter(student_id=str(alumno))
        return queryset_notas