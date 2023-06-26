# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from auto import views

router = DefaultRouter()
router.register(r'auto', views.AutoViewSet, basename='auto')

urlpatterns = [
    path('', include(router.urls))
]
