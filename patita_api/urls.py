from rest_framework import routers
from .views import *
from django.urls import path, include
from rest_framework.documentation import include_docs_urls

router = routers.DefaultRouter()
router.register('personas', PersonaViewSet, 'personas' )
router.register('animalPerdidos', AnimalPerdidoViewSet, 'animalPerdidos' )
router.register('animalEncontrados', AnimalEncontradoViewSet, 'animalEncontrados' )
router.register('animalAdoptables', AnimalAdoptableViewSet, 'animalAdoptables' )
router.register('solicitudAdopciones', SolicitudAdopcionViewSet, 'solicitudAdopciones' )
router.register('solicitudContactos', SolicitudContactoViewSet, 'solicitudContactos' )

urlpatterns = [
    path('api/v1.2/', include(router.urls)),             #http://127.0.0.1:8000/api/v1.2/
    path('docs/', include_docs_urls(title="Patita API")) #http://127.0.0.1:8000/docs
]
