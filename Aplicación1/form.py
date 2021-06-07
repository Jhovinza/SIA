from django import forms
from .models import *


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['id_cliente', 'nombre', 'rut', 'direccion', 'telefono', 'correo', 'plan_reciclaje']

class PlanForm(forms.ModelForm):
    class Meta:
        model = Plan_reciclaje
        fields = ['id_plan', 'nombre_plan', 'valor_plan', 'num_retiros']