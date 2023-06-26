from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from autos.views import MarcaViewSet, TipoViewSet, AutoViewSet

router = DefaultRouter()
router.register(r'marcas', MarcaViewSet)
router.register(r'tipos', TipoViewSet)
router.register(r'autos', AutoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
