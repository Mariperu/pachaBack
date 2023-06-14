from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.index, name='index'),
    path('crear_usuario/', views.crear_usuario, name='crear_usuario'),
    path('login/', LoginView.as_view(template_name='appColegio/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='appColegio/index.html'), name='logout'),
    path('crear_curso/', views.crear_curso, name='crear_curso'),
    path('perfil/', views.show_perfil, name='perfil'),
    path('crear_evaluacion/', views.crear_evaluacion, name='crear_evaluacion'),
    path('lista_alumnos/', views.lista_alumnos, name='lista_alumnos'),
    path('asistencia_notas/<int:alumno_id>/', views.asistencia_notas, name='asistencia_notas'),
    path('evaluaciones_alumno/', views.evaluaciones_alumno, name='evaluaciones_alumno'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)