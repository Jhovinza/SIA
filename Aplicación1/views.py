# Create your views here.
import django_filters
from django.shortcuts import render, redirect

from Aplicación1.form import *
from Aplicación1.models import *
from django.views.generic import View
from django_filters.views import FilterView
from .utils import render_to_pdf
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from django.http import FileResponse
import io
import os
from django.conf import settings

from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders


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

class filtroEntregas(django_filters.FilterSet):
    fecha_entrega = django_filters.DateFilter()

    fecha_entrega = django_filters.DateFilter(
        widget=forms.DateInput(
            attrs={
                'id': 'datepicker',
                'type': 'date'
            }
        )
    )

class listaEntregas(FilterView):
    model = Cliente
    template_name = 'entregas1.html'
    context_object_name = 'entregas'
    filterset_class = filtroEntregas
    widgets = {'fecha_entrega': DateInput(attrs={'type': 'date'})}

    class Meta:
        model = Cliente
        fields = ['fecha_entrega']


def render_pdf_view(request):
    template_path = 'lista.html'
    context = {'entregas': listaClientes }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

