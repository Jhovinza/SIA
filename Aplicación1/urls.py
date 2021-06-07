from django.urls import path
from Aplicación1.views import Aplicación1, listaClientes, agregarClientes, listaPlanes, agregarPlanes, archivoReportes

urlpatterns = [
    path("", Aplicación1),

    path('clientes/', listaClientes, name='clientes'),
    path('agregarClientes/', agregarClientes, name='agregarClientes'),

    path('planes/', listaPlanes, name='planes'),
    path('agregarPlanes/', agregarPlanes, name='agregarPlanes'),

    path('reportes/', archivoReportes, name='reportes'),
]

