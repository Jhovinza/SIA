from django.urls import path
from Aplicación1.views import Aplicación1, listaClientes, agregarClientes, listaPlanes, agregarPlanes, \
    modificarClientes, eliminarClientes, modificarPlanes, eliminarPlanes,  listaEntregas, render_pdf_view


urlpatterns = [
    path("", Aplicación1),

    path('clientes/', listaClientes, name='clientes'),
    path('agregarClientes/', agregarClientes, name='agregarClientes'),

    path('planes/', listaPlanes, name='planes'),
    path('agregarPlanes/', agregarPlanes, name='agregarPlanes'),



    path('modificarClientes/<id_cliente>', modificarClientes, name='modificarClientes'),
    path('eliminarClientes/<id_cliente>', eliminarClientes, name='eliminarClientes'),

    path('modificarPlanes/<id_plan>', modificarPlanes, name='modificarPlanes'),
    path('eliminarPlanes/<id_plan>', eliminarPlanes, name='eliminarPlanes'),


    path('entregas1/', listaEntregas.as_view(), name="entregas1"),

    path('lista/', render_pdf_view, name='lista'),

]

