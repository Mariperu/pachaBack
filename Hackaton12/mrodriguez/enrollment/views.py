from django.shortcuts import render, redirect
from .models import Course
from .forms import RequestForm
from .controllers import create_request_controller


def index(request):
    courses = Course.objects.all()
    context = {"courses": courses}
    return render(request, "enrollment/course_list.html", context)


def course_detail(request, id):
    courses = Course.objects.get(id=id)
    context = {"course": courses}
    return render(request, "enrollment/course_detail.html", context)


def create_request(request):
    form = RequestForm()
    if create_request_controller(request):
        return redirect("index")
    context = {"form": form}
    return render(request, "enrollment/request_form.html", context)
