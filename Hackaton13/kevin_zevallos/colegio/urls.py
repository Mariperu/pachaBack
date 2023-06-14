from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    # dashboard 
    path('dashboard/<str:id_usuario>/', views.dashboard, name='dashboard'),
    path('marcar_asistencia/<str:id_profesor>/<str:id_alumno>', views.marcar_asistencia, name="marcar_asistencia"),
    path('calendar/<str:alumno_id>', views.calendar, name='calendar'),
    path('notas/<str:alumno_id>', views.notas, name='notas'),
    # matricular
    path('matricular/', views.matricular_alumno, name="matricular"),
    path('alumno/<str:alumno_id>', views.alumno , name='alumno'),
    # API
    path('api/notas/<str:alumno_id>/', views.NotasList.as_view() , name='api/notas'),
    path('calendario_asistencia/<str:alumno_id>/', views.AsistenciaList.as_view(), name='calendario_asistencia')
]