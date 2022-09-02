from django.urls import path 
from .views import * 

urlpatterns = [
    path("",inicio, name="inicio"),
    path("renault/", renault, name="renault"),
    path("ford/", ford, name="ford"),
    path("volkswagen/", volkswagen, name="volkswagen"),
    path("autoford/", autoford, name="autoford"),
    path("busquedarenault/", busquedarenault, name="busqueda"),
    path("buscar/", buscar, name="buscar"),
    
]