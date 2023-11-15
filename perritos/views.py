from django.shortcuts import render
from django.urls import reverse_lazy 
from django.views.generic import  ListView, DetailView, CreateView, DeleteView, UpdateView, TemplateView
from perritos.models import Propietarios, Perritos, Raza



# Create your views here.
class PropietariosListView(ListView):
    model = Propietarios

class PropietariosDetailView(DetailView):
    model = Propietarios
    context_object_name = 'perrito'

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
    success_url = reverse_lazy('perritos-list')

class PerritosCreate(CreateView):
    model = Perritos
    fields = '__all__'
    success_url = reverse_lazy('perritos-list')

class PerritosDelete(DeleteView):
    model = Perritos
    success_url = reverse_lazy('perritos-list')



class PropietariosUpdate(UpdateView):
    model = Propietarios
    fields = '__all__' 
    success_url = reverse_lazy('propietarios-list')

class PropietariosCreate(CreateView):
    model = Propietarios
    fields = '__all__'
    success_url = reverse_lazy('propietarios-list')

class PropietariosDelete(DeleteView):
    model = Propietarios
    success_url = reverse_lazy('propietarios-list')


class RazaUpdate(UpdateView):
    model = Raza
    fields = '__all__' 
    success_url = reverse_lazy('raza-list')

class RazaCreate(CreateView):
    model = Raza
    fields = '__all__'
    success_url = reverse_lazy('raza-list')

class RazaDelete(DeleteView):
    model = Raza
    success_url = reverse_lazy('raza-list')


class InicioView(TemplateView):
    template_name = 'inicio'

    


    
