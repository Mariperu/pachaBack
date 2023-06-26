# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from tipo import views

router = DefaultRouter()
router.register(r'tipo', views.TipoViewSet, basename='tipo')

urlpatterns = [
    path('', include(router.urls))
]
