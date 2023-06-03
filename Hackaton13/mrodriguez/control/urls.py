from django.urls import path

from . import views

# app_name = "control"

urlpatterns = [
    path("", views.index, name="index"),
    path("teachers/", views.teachers, name="teachers"),
    path("course_detail/<str:id>", views.course_detail, name="course_detail"),
    path("request/", views.create_request, name="request"),
    path("teachers/", views.teachers, name="teachers"),
    path("grade_form/", views.create_grade, name="grade_form"),
    path("attendance_form/", views.create_attendance, name="attendance_form"),
    path("students/", views.students, name="students"),
    path("student_detail/<str:id>", views.student_detail, name="student_detail"),
]
