from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.http import require_http_methods
from .forms import AutorForm

# Create your views here. = trabaja con el HttpResponse que se encuentra en django.http propio de Django
def Home(request): # Primera Funcion Vista Home
    return render(request, 'libro/index.html') #retorna la vista

@require_http_methods(["POST","GET"])
def crear_autor(request): # Funcion Vista Crear Autor
    
    if request.method == 'POST':
        autor_forms = AutorForm(request.POST)
        if autor_forms.is_valid():
            autor_forms.save()
            return redirect('libro.index')
    else:
        autor_forms = AutorForm()

    return render(request, 'libro/crear_autor.html', {'autor_forms' : autor_forms })
