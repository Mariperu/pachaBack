from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import AlumnoForm, UsuarioAppForm, NotasForm, AsistenciaForm
from .models import Alumno, UsuarioApp, Notas
from django.contrib.auth.decorators import permission_required
# Create your views here.

def list_alumno(request):
    alumnos = Alumno.objects.all()
    context = {'title': "Alumnos", 'list': alumnos}

    return render(request, 'list.html', {'context': context})

def create_alumno(request):
    if(request.method == 'POST'):

        form = AlumnoForm(request.POST)

        if(form.is_valid()):
            form.save()
            return redirect("/")
    else:
        form = AlumnoForm()
        context = {'title': "Alumnos", 'form': form}

    return render(request, 'create.html', {'context': context})

def detail_alumno(request):
    alumno = Alumno.objects.all()
    context = {'title': "Alumnos", 'list': alumno}
    return render(request, 'detail.html', {"context": context})


def update_alumno(request):#el nombre del parametro debe ser el mismo en aca y urls patterns

    alumno = Alumno.objects.get(pk=request.POST["id"])

    if(request.method == 'POST'):

        form = AlumnoForm(request.POST, instance=alumno)
        if(form.is_valid()):
            form.save()
            return redirect("/") 

    else:
        form = AlumnoForm(instance=alumno)
        context = {'title': "Alumnos", 'form': form}

    return render(request, 'create.html', {'context': context})


def delete_alumno(request):
    item = Alumno.objects.get(pk=request.POST["id"])
    context = {'title': "Alumnos", 'item': item}
    if request.method == 'POST':
        item.delete()
        return redirect("/")
    
    return render(request, 'delete.html', {'context': context})


def create_usuario(request):
    if(request.method == 'POST'):

        form = UsuarioAppForm(request.POST)

        if(form.is_valid()):
            form.save()
            return redirect("/")
    else:
        form = UsuarioAppForm()
        context = {'title': "Elige tu rol", 'form': form}

    return render(request, 'create.html', {'context': context})



def create_asistencia(request):
    if(request.method == 'POST'):
        form = AsistenciaForm(request.POST)
        if(form.is_valid()):
            form.save()
            return render(request, 'asistencia.html')
    else:
        form = AsistenciaForm()
        context = {'title': "Agrega una nota", 'form': form}

    return render(request, 'create.html', {'context': context})


def show_rol(request):
    if request.user.is_authenticated:
        return request.user.usuarioapp.rol
    else:
        return None

def main(request):
    user_role = show_rol(request)
    context = {'user_role': user_role}
    return render(request, "main.html", context)


def list_notas(request):
    if(request.method == 'POST'):
        form = NotasForm(request.POST)
        if(form.is_valid()):
            form.save()
            return render(request, "notas.html", context)
    else:
        form = NotasForm()
        context = {'title': "Agrega notas", 'form': form}

    return render(request, 'notas.html', {'context': context})

def hola(request):
       return HttpResponse("hola")

