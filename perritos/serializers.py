from rest_framework import serializers
from .models import Perritos, Propietarios, Raza

class PropietariosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Propietarios
        fields = ('url', 'nombre', 'apellido', 'edad')

class PerritosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Perritos
        fields = ('__all__')

class RazaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Raza
        fields = ('__all__')

