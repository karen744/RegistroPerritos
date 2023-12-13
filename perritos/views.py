from django.shortcuts import render
from django.urls import reverse_lazy 
from django.views.generic import  ListView, DetailView, CreateView, DeleteView, UpdateView, TemplateView
from perritos.models import Propietarios, Perritos, Raza

from rest_framework import viewsets
from .serializers import PropietariosSerializer, PerritosSerializer, RazaSerializer



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

class PropietariosViewSet(viewsets.ModelViewSet):
    queryset = Propietarios.objects.all()
    serializer_class = PropietariosSerializer

class PerritosViewSet(viewsets.ModelViewSet):
    queryset = Perritos.objects.all()
    serializer_class = PerritosSerializer    

class RazaViewSet(viewsets.ModelViewSet):
    queryset = Raza.objects.all()
    serializer_class = RazaSerializer  
