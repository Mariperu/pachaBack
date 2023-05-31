from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Alumno, Profesor, Curso, Salon, Matricula
from django.urls import reverse


# Create your views here.
def index(request):
    data_cursos = Curso.objects.order_by()
    template = loader.get_template("./index.html")
    context = {
        "cursos": data_cursos,
    }
    return HttpResponse(template.render(context, request))
