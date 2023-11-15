from django.shortcuts import render
from django.urls import reverse_lazy 
from django.views.generic import  ListView, DetailView, CreateView, DeleteView, UpdateView, TemplateView
from perritos.models import Propietarios, Perritos, Raza



# Create your views here.
class PropietariosListView(ListView):
    model = Propietarios

class PropietariosDetailView(DetailView):
    model = Propietarios

class PerritosListView(ListView):
    model = Perritos

class PerritosDetailView(DetailView):
    model = Perritos
    
class RazaListView(ListView):
    model = Raza

class RazaDetailView(DetailView):
    model = Raza

class PerritosUpdate(UpdateView):
    model = Perritos
    fields = '__all__' 

class PerritosCreate(CreateView):
    model = Perritos
    fields = '__all__'

class PerritosDelete(DeleteView):
    model = Perritos
    success_url = reverse_lazy('perritos-list')

class InicioView(TemplateView):
    template_name = 'inicio'


    
