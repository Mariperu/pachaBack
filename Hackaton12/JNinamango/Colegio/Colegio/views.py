from django.http import HttpRequest, HttpResponse
from django.template import Template,Context, loader
from django.shortcuts import render
from .models import Alumno, Profesor, Curso
def saludo(request):
    #doc = loader.get_template("base.html")
    #renders = doc.render({"context": "contexto1"})#esta funcion render pertenece a los tempaltes, el shortucut es otro
    #return HttpResponse(renders)#context debe ser un diccionario

    return render(request, "base.html", {"context": "context1"})

def home(request):
    cursos = Curso.objects.all()
    context = {"cursos": cursos}
    return render(request, "home.html", context)

def createAlumno(request):
    #return HttpResponse(f"{nombre} - {edad}")
    #context = {"nombreAn": nombre, "edad": edad
    if(request.method == 'POST'):
        name = request.POST["nombre"]
        edad = request.POST["edad"]
        correo = request.POST["correo"]
        print(request.POST["curso"])
        curso = Curso.objects.get(id=request.POST["curso"])#obtengo id

        newAlumno = Alumno(nombre=name, edad=edad, correo=correo, matriculado=True, curso=curso)  
        newAlumno.save()
        return render(request, "base.html")
    else:        
        context_cursos = {'cursos': Curso.objects.all()}
        
        return render(request, "createAlumno.html", context_cursos)
    
def createProfesor(request):

    if(request.method == 'POST'):
        name = request.POST["nombre"]
        edad = request.POST["edad"]
        correo = request.POST["correo"]
        print(request.POST["curso"])
        curso = Curso.objects.get(id=request.POST["curso"])#obtengo id

        newProfesor = Profesor(nombre=name, edad=edad, correo=correo, curso=curso)  
        newProfesor.save()
        return render(request, "base.html")
    else:        
        context_cursos = {'cursos': Curso.objects.all()}
        return render(request, "createProfesor.html", context_cursos)
    
def showClass(request):
        cursos = Curso.objects.all()
        alumnos = Alumno.objects.all()
        profesores = Profesor.objects.all()
        context = {"cursos": cursos, "alumnos": alumnos, "profesores": profesores}
        return render(request, "salones.html", context)