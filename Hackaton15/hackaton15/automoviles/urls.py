"""
URL configuration for automoviles project.

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
from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    # Django Admin
    path('admin/', admin.site.urls),

    path('', include(('users.urls', 'users'), namespace='users')),
    path('', include(('auto.urls', 'auto'), namespace='auto')),
    path('', include(('tipo.urls', 'tipo'), namespace='tipo')),
    path('', include(('marca.urls', 'marca'), namespace='marca')),
    path('', include(('search.urls', 'search'), namespace='search')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
