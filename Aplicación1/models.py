import recurrence
from django.db import models
from recurrence import *

# Create your models here.
class Plan_reciclaje(models.Model):
    id_plan = models.BigAutoField(primary_key=True)
    nombre_plan = models.CharField(max_length=30, null=False, blank=False)
    valor_plan = models.IntegerField(null=False, blank=False)
    num_retiros = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return(self.nombre_plan)

class Cliente(models.Model):
    id_cliente = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    rut = models.CharField(max_length=10, null=False, blank=False)
    direccion = models.CharField(max_length=100, null=False, blank=False)
    telefono = models.IntegerField(null=False, blank=False)
    correo = models.CharField(max_length=50, null=True, blank=True)
    plan_reciclaje = models.ForeignKey(Plan_reciclaje, null=True, on_delete=models.SET_NULL)
    opCiudad = [("1", "La Serena"), ("2", "Coquimbo")]
    ciudad = models.CharField(max_length=20, blank=False, null=True, choices=opCiudad)
    fecha_entrega= models.DateField(null=True)
    recurrencias =

    def __str__(self):
        return(self.nombre)


class Ficha_Plan(models.Model):
    id_ficha = models.BigAutoField(primary_key=True)
    info_cliente = models.ForeignKey(Cliente, null=True, on_delete=models.SET_NULL)
    info_plan = models.ForeignKey(Plan_reciclaje, null=True, on_delete=models.SET_NULL)
    fecha_retiro = models.DateField(null=True, blank=False)

    def __str__(self):
        return(str(self.info_cliente))

class Reporte(models.Model):
    fecha = models.DateField(null=False, blank=False)




