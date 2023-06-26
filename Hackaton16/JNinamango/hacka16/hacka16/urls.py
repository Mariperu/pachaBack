"""
URL configuration for hacka16 project.

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
from django.urls import path, include
from rest_framework import routers
from Canciones.views import *

router = routers.DefaultRouter()
router.register(r'canciones', SongViewSet, basename='canciones')




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),

    path('canciones/get', SongGetView, name='canciones_get_view'),
    path('canciones/post', SongPostView, name='canciones_post_view'),
    path('canciones/put/<int:id>', SongPutView, name='canciones_put_view'),
    path('canciones/delete/<int:id>', SongDeleteView, name='canciones_delete_view'),

]

urlpatterns+= [
    path('api_auth', include('rest_framework.urls'))
]