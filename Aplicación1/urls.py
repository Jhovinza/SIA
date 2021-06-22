from django.urls import path
from Aplicación1.views import Aplicación1, listaClientes, agregarClientes, listaPlanes, agregarPlanes, archivoReportes, \
    modificarClientes, eliminarClientes, modificarPlanes, eliminarPlanes, calendario

urlpatterns = [
    path("", Aplicación1),

    path('clientes/', listaClientes, name='clientes'),
    path('agregarClientes/', agregarClientes, name='agregarClientes'),

    path('planes/', listaPlanes, name='planes'),
    path('agregarPlanes/', agregarPlanes, name='agregarPlanes'),

    path('reportes/', archivoReportes, name='reportes'),

    path('modificarClientes/<id_cliente>', modificarClientes, name='modificarClientes'),
    path('eliminarClientes/<id_cliente>', eliminarClientes, name='eliminarClientes'),

    path('modificarPlanes/<id_plan>', modificarPlanes, name='modificarPlanes'),
    path('eliminarPlanes/<id_plan>', eliminarPlanes, name='eliminarPlanes'),

#path('<int:year>/<str:month>', calendario, name='calendario')
#path('calendario/<year>/<month>', calendario, name='calendario')
#path('calendario', calendario, name='calendario')


]

