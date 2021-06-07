# Create your views here.
from django.shortcuts import render, redirect

from Aplicación1.form import *
from Aplicación1.models import *


def Aplicación1(request):
    return render(request, "home.html")

def listaClientes(request):
    datos = {'listaClientes': Cliente.objects.all()}
    return render(request, 'clientes.html', datos)

def agregarClientes(request):
    if request.method == 'POST':
        formulario = ClienteForm(request.POST)

        if formulario.is_valid():
            formulario.save()
            return redirect('clientes')

    else:
        formulario = ClienteForm()

    datos = {'form': formulario}
    return render(request, 'agregarClientes.html', datos)

def listaPlanes(request):
    datos = {'listaPlanes': Plan_reciclaje.objects.all()}
    return render(request, 'planes.html', datos)

def agregarPlanes(request):
    if request.method == 'POST':
        formulario = PlanForm(request.POST)

        if formulario.is_valid():
            formulario.save()
            return redirect('planes')

    else:
        formulario = PlanForm()

    datos = {'form': formulario}
    return render(request, 'agregarPlanes.html', datos)

def archivoReportes(request):
    datos = {'archivoReportes': Reporte.objects.all()}
    return render(request, 'reportes.html', datos)