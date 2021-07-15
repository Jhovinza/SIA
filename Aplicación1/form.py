from django import forms
from .models import *
from django.forms.widgets import DateInput

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['id_cliente', 'nombre', 'rut', 'direccion', 'telefono', 'correo', 'plan_reciclaje', 'ciudad', 'fecha_entrega', 'recurrencias']
        widgets = {'fecha_entrega': DateInput(attrs={'type': 'date'})}

class PlanForm(forms.ModelForm):
    class Meta:
        model = Plan_reciclaje
        fields = ['id_plan', 'nombre_plan', 'valor_plan', 'num_retiros']

#class DateInput(forms.DateInput):
 #   input_type: 'date'

class FichaForm(forms.ModelForm):
    class Meta:
        model = Ficha_Plan
        fields = ['id_ficha', 'info_cliente','info_plan', 'fecha_retiro']
        widgets = {'fecha_retiro': DateInput(attrs={'type': 'date'})}
