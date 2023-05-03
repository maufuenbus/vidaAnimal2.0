from rest_framework import viewsets, permissions
from .serializer import *
from .models import *
# Create your views here.


class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
    permission_classes = [permissions.AllowAny]

class AnimalPerdidoViewSet(viewsets.ModelViewSet):
    queryset = AnimalPerdido.objects.all()
    serializer_class = AnimalPerdidoSerializer
    permission_classes = [permissions.AllowAny]

class AnimalEncontradoViewSet(viewsets.ModelViewSet):
    queryset = AnimalEncontrado.objects.all()
    serializer_class = AnimalEncontradoSerializer
    permission_classes = [permissions.AllowAny]

class AnimalAdoptableViewSet(viewsets.ModelViewSet):
    queryset = AnimalAdoptable.objects.all()
    serializer_class = AnimalAdoptableSerializer
    permission_classes = [permissions.AllowAny]

class SolicitudAdopcionViewSet(viewsets.ModelViewSet):
    queryset = SolicitudAdopcion.objects.all()
    serializer_class = SolicitudAdopcionSerializer
    permission_classes = [permissions.AllowAny]

class SolicitudContactoViewSet(viewsets.ModelViewSet):
    queryset = SolicitudContacto.objects.all()
    serializer_class = SolicitudContactoSerializer
    permission_classes = [permissions.AllowAny]