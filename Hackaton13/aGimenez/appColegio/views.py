from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.contrib import messages
from django.db.models import Max

def index(request):
	return render(request, 'appColegio/index.html')

def crear_usuario(request):
	if request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			messages.success(request, f'Usuario {username} creado')
			return redirect('index')
	else:
		form = UserForm()

	context = { 'form' : form }
	return render(request, 'appColegio/crear_usuario.html', context)

def crear_curso(request, template_name='appColegio/crear_curso.html'):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            messages.success(request, 'Curso creado correctamente')
            return redirect('index')
    else:
        form = CursoForm()
        dato = {"form": form}
        return render(request, template_name, dato)

def show_perfil(request, template_name='appColegio/perfil.html'):
    cursos = Curso.objects.all()
    users = User.objects.all()
    datos = {"cursos": cursos, "users": users}
    return render(request, template_name, datos)

def crear_evaluacion(request, template_name='appColegio/crear_evaluacion.html'):
    if request.method == 'POST':
        form = EvaluacionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Evaluacion creada correctamente')
        return redirect('lista_alumnos')
    else:
        user = request.user
        cursos = user.cursos.all()
        datos_iniciales = {
            'profesor': user,
            'cursos': cursos
        }
        form = EvaluacionForm(initial=datos_iniciales)

        context = {'form': form, 'profesor': user, 'cursos': cursos}
        return render(request, template_name, context)

def lista_alumnos(request, template_name='appColegio/lista_alumnos.html'):
    max_evaluacion_id = Evaluacion.objects.latest('id').id
    alumnos_notas = NotasAsistencia.objects.filter(curso__id=max_evaluacion_id).select_related('alumnos')
    contador = alumnos_notas.count()
    print(contador)
    alumnos = User.objects.filter(cursos__evaluacion__id=max_evaluacion_id, role='Alumno')
    context = {'alumnos': alumnos, 'alumnos_notas': alumnos_notas}
    return render(request, template_name, context)

def asistencia_notas(request, *, alumno_id, template_name='appColegio/asistencia_notas.html'):
    if request.method == 'POST':
        form = NotasAsistenciaForm(request.POST)
        if form.is_valid():
            max_evaluacion_id = Evaluacion.objects.latest('id').id
            curso = NotasAsistencia.objects.filter(curso_id=max_evaluacion_id, alumnos_id = alumno_id).count()

            if curso == 0:
                form.save()
                messages.success(request, 'Alumno guardado correctamente')
            else:
                messages.success(request, 'Alumno ya cargado')
        return redirect('lista_alumnos')
    else:
        mayor_id = Evaluacion.objects.aggregate(Max('id'))
        curso = Evaluacion.objects.get(id=mayor_id['id__max'])

        alumno = get_object_or_404(User, id=alumno_id)

        datos_iniciales = {
            'curso': curso,
            'alumnos':alumno
        }

        form = NotasAsistenciaForm(initial=datos_iniciales)

        context = {'form': form, 'cursos': curso, 'alumno':alumno}

        return render(request, template_name, context)

@login_required
def evaluaciones_alumno(request):
    alumno = request.user
    evaluaciones = Evaluacion.objects.filter(curso__usuarios=alumno)

    return render(request, 'appColegio/evaluaciones_alumno.html', {'evaluaciones': evaluaciones})