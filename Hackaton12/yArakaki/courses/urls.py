from django.urls import path
from .views import CursoListView, EstudianteCreateView, ProfesorCreateView

urlpatterns = [
    path('', CursoListView.as_view(), name='curso_list'),
    path('<int:curso_id>/agregar_estudiante/', EstudianteCreateView.as_view(), name='agregar_estudiante'),
    path('<int:curso_id>/asignar_profesor/', ProfesorCreateView.as_view(), name='asignar_profesor'),
]
