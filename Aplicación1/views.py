# Create your views here.
from django.shortcuts import render, redirect

from Aplicación1.form import *
from Aplicación1.models import *

import calendar
from calendar import HTMLCalendar


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

def modificarClientes(request, id_cliente):
    cliente = Cliente.objects.get(id_cliente=id_cliente)

    if request.method == "POST":
        formulario = ClienteForm(request.POST, instance=cliente)

        if formulario.is_valid():
            formulario.save()
            return redirect('clientes')

    else:
        formulario = ClienteForm(instance=cliente)

    datos = {'form': formulario}

    return render(request, 'modificarClientes.html', datos)

def eliminarClientes(request, id_cliente):
    cliente = Cliente.objects.get(id_cliente=id_cliente)
    cliente.delete()
    return redirect('clientes')

def modificarPlanes(request, id_plan):
    planes = Plan_reciclaje.objects.get(id_plan=id_plan)

    if request.method == "POST":
        formulario = PlanForm(request.POST, instance=planes)

        if formulario.is_valid():
            formulario.save()
            return redirect('planes')

    else:
        formulario = PlanForm(instance=planes)

    datos = {'form': formulario}

    return render(request, 'modificarPlanes.html', datos)

def eliminarPlanes(request, id_plan):
    planes = Cliente.objects.get(id_plan=id_plan)
    planes.delete()
    return redirect('planes')

def calendario(request, year, month):
    month = month.capitalize()
    month_num = list(calendar.month_name).index(month)
    month_num = int(month)

    cal = HTMLCalendar().formatmonth(year, month_num)

    datos = {"year": year, "month": month, "month_num": month_num, "cal": cal}

    return render(request, 'calendario.html', datos)

