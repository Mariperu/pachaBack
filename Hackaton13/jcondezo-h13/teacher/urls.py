from django.urls import path
from .views import Home, crear_notas, editar_nota, eliminar_nota, HomeAsistencia, crear_asistencia, editar_asistencia, eliminar_asistencia

app_name='teacher'

urlpatterns = [
    path('', Home, name='index'),
    path('crear/', crear_notas, name='crear'),
    path('editar/<int:id>/', editar_nota, name='editar'),
    path('eliminar/<int:id>/', eliminar_nota, name='eliminar'),
    # asistencia
    path('attendance/', HomeAsistencia, name='indexAsistencia'),
    path('attendance/crear/', crear_asistencia, name='crearAsistencia'),
    path('attendance/editar/<int:id>/', editar_asistencia, name='editarAsistencia'),
    path('attendance/eliminar/<int:id>/', eliminar_asistencia, name='eliminarAsistencia'),
]