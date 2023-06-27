from django.urls import include, path
from rest_framework import routers
from singers import views

router = routers.DefaultRouter()

urlpatterns = [
    path("", include(router.urls)),
]
