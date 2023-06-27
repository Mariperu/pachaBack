from django.urls import include, path
from rest_framework import routers
from songs import views

router = routers.DefaultRouter()

urlpatterns = [
    path("", include(router.urls)),
]
