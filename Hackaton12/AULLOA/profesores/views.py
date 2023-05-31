from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Cursos
from django.template import loader

# Create your views here.
def index(request):
    latest_cursos_list = Cursos.objects.order_by("-pub_date")[:5]
    template = loader.get_template("profesores/index.html")
    context = {
        "latest_cursos_list": latest_cursos_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, curso_id):
    curso = get_object_or_404(Cursos, pk=curso_id)
    return render(request, "profesores/detail.html", {"curso": curso})


def results(request, curso_id):
    curso = get_object_or_404(Cursos, pk=curso_id)
    return render(request, "profesores/results.html", {"curso": curso})


