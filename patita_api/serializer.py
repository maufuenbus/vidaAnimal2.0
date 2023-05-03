from rest_framework import serializers
from .models import * # Persona, AnimalPerdido, AnimalEncontrado, AnimalAdoptable, SolicitudAdopcion, SolicitudContacto


class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ('id_persona', 'nombre', 'apellido', 'email', 'contrasena')

class AnimalPerdidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalPerdido
        fields = ('id_anim_perdido', 'especie', 'raza', 'tamano', 'color', 'fecha_perdido', 'ubicacion','descripcion')

class AnimalEncontradoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalEncontrado
        fields = ('id_anim_encontrado', 'especie', 'raza', 'tamano', 'color', 'fecha_encontrado', 'ubicacion', 'descripcion')

class AnimalAdoptableSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalAdoptable
        fields = ('id_anim_adoptable', 'especie', 'raza' , 'tamano' , 'color', 'edad', 'ubicacion' , 'descripcion')

class SolicitudAdopcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolicitudAdopcion
        fields = ('id_solic_adop', 'fecha_solicitud', 'estado')

class SolicitudContactoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolicitudContacto
        fields = ('id_solic_contac', 'fecha_solicitud', 'estado')