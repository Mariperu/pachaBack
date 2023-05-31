from django.urls import path
from . import views

app_name = "gest_users"

urlpatterns = [
    path('', views.index, name="index"),
]
