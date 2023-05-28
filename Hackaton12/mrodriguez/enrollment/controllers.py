from .forms import RequestForm
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
