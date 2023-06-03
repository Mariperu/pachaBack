from django.shortcuts import render, redirect
from .models import Course, Student, GradeRecord, AttendanceRecord
from .forms import RequestForm, GradeForm, AttendanceForm
from .controllers import (
    create_request_controller,
    create_grade_controller,
    create_attendance_controller,
)


def index(request):
    courses = Course.objects.all()
    context = {"courses": courses}
    return render(request, "control/course_list.html", context)


def course_detail(request, id):
    courses = Course.objects.get(id=id)
    context = {"course": courses}
    return render(request, "control/course_detail.html", context)


def create_request(request):
    form = RequestForm()
    if create_request_controller(request):
        return redirect("index")
    context = {"form": form}
    return render(request, "control/request_form.html", context)


def teachers(request):
    return render(request, "control/teachers.html")


def create_grade(request):
    form = GradeForm()
    if create_grade_controller(request):
        return redirect("teachers")
    context = {"form": form}
    return render(request, "control/grade_form.html", context)


def create_attendance(request):
    form = AttendanceForm()
    if create_attendance_controller(request):
        return redirect("teachers")
    context = {"form": form}
    return render(request, "control/attendance_form.html", context)


def students(request):
    students = Student.objects.all()
    context = {"students": students}
    return render(request, "control/students.html", context)


def student_detail(request, id):
    students = Student.objects.get(id=id)
    grades = GradeRecord.objects.filter(student=id)
    attendances = AttendanceRecord.objects.filter(student=id)
    context = {
        "student": students,
        "grades": grades,
        "attendances": attendances,
    }
    return render(request, "control/student_detail.html", context)
