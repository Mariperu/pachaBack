"""
URL configuration for Colegio project.

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
from ColegioApp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.create_usuario, name='create_alumno'),
    path('create_alumno/', views.create_alumno, name='create_alumno'),
    path('list_alumno/', views.list_alumno, name='list_alumno'),
    path('detail/update_alumno/', views.update_alumno, name='update_alumno'),
    path('detail/delete_alumno/', views.delete_alumno, name='delete_alumno'),

    #path('create_usuario/', views.create_usuario, name='create_usuario'),

    path('detail/', views.detail_alumno, name='detail_alumno'),
]
