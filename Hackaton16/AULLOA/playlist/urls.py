from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'playlist', views.PlaylistViewSet, basename='playlist')

urlpatterns = [
    path('', include(router.urls)),
]
