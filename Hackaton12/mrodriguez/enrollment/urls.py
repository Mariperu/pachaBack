from django.urls import path

from . import views

pp_name = "enrollment"

urlpatterns = [
    path("", views.index, name="index"),
    path("course_detail/<str:id>", views.course_detail, name="course_detail"),
    path("request/", views.create_request, name="request"),
]
