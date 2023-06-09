from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


from .forms import AddVuelo, UpdateVuelo, AddTipoAsiento, UpdateTipoAsiento
from .models import Vuelo, TipoAsiento

# Create your views here.
class IndexView(generic.TemplateView):
    template_name = 'checking/index.html'

class AddVueloView(CreateView):
    form_class = AddVuelo
    template_name = 'checking/addVuelo.html'
    success_url = '/checking/vuelo'

class ListVuelosView(ListView):
    model = Vuelo

class DetailVuelosView(DetailView):
    model = Vuelo

class DeleteVuelosView(DeleteView):
    model = Vuelo
    success_url ="/checking/vuelo"
    template_name = "checking/confirm_delete.html"

class UpdateVuelosView(UpdateView):
    model = Vuelo
    form_class = UpdateVuelo
    success_url ="/checking/vuelo"

class ListTipoAsientoView(ListView):
    model = TipoAsiento

class DetailTipoAsientoView(DetailView):
    model=TipoAsiento

class UpdateTipoAsientoView(UpdateView):
    model = TipoAsiento
    form_class = UpdateTipoAsiento
    success_url = '/checking/tipoasiento'

class DeleteTipoAsientoView(DeleteView):
    model = TipoAsiento
    success_url ="/checking/tipoasiento"
    template_name = "checking/confirm_delete.html"

class AddTipoAsientoView(CreateView):
    form_class = AddTipoAsiento
    template_name = 'checking/addTipoAsiento.html'
    success_url = '/checking/tipoasiento/'