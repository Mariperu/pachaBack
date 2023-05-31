from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('crear_curso', views.crearCurso, name="crear_curso"),
    path('contratar_profesor', views.contratarProfesor, name="contratar_profesor"),
    path('crear_matricula', views.crearMatricula, name="crear_matricula"),
    path('crear_alumno', views.crearAlumno, name='crear_alumno'),
    path('show_curso', views.show_cursos, name='show_curso')
]