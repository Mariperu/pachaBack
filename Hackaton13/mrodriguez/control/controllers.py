from .forms import RequestForm, GradeForm, AttendanceForm
from django.shortcuts import redirect
from django.http import HttpResponseRedirect


def create_request_controller(request):
    if request.method == "POST":
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return True
        else:
            return False


def create_grade_controller(request):
    if request.method == "POST":
        form = GradeForm(request.POST)
        if form.is_valid():
            form.save()
            return True
        else:
            return False


def create_attendance_controller(request):
    if request.method == "POST":
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return True
        else:
            return False
