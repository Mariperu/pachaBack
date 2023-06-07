from django.urls import path
from core.views import profesor_dashboard, alumno_dashboard, administrador_dashboard


urlpatterns = [
    path('profesor/', profesor_dashboard, name='profesor_dashboard'),
    path('alumno/', alumno_dashboard, name='alumno_dashboard'),
    path('administrador/', administrador_dashboard, name='administrador_dashboard'),
    # Agrega las rutas adicionales que sean necesarias
]
