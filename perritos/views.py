from django.shortcuts import render
from django.views.generic import  ListView, DetailView
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

