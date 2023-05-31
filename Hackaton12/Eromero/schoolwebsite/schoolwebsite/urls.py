"""
URL configuration for schoolwebsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from main.views import home, matricular
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # URL para home.html
    path('matricular/<int:curso_id>/', views.matricular, name='matricular'),
    path('do_matriculacion/<int:curso_id>/<int:estudiante_id>/', views.do_matriculacion, name='do_matriculacion'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('registro_profesor/', views.registro_profesor, name='registro_profesor'),
    path('registro_estudiante/', views.registro_estudiante, name='registro_estudiante'),
    path('sala_clase/<int:id>/', views.sala_clase, name='sala_clase'),
]
