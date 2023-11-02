from django.db import models
from django.urls import reverse

# Create your models here.
class Propietarios(models.Model):
    """ propietarios  """
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField(max_length=2)

    def __str__(self):
        return self.nombre

class Perritos(models.Model):
    """ perritos """
    
    nombre = models.ForeignKey('Propietarios', on_delete=models.PROTECT,related_name='get_Propietarios' )
    nombrePerrito = models.CharField(max_length=50)
    edad = models.IntegerField(max_length=2)

    def __str__(self):
        return self.nombrePerrito

class Raza(models.Model):
    """ Raza """
    
    nombrePerrito = models.ForeignKey('Perritos', on_delete=models.PROTECT,related_name='get_perritos' )
    nombreraza = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    

   
    
    def __str__(self):
        return self.nombreraza
    
    def get_absolute_url(self):
        return reverse('perritos-list')
