from django.db import models

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

    def __str__(self):
        return (self.id_cliente+" - "+self.nombre+" - "+self.rut+" - "+self.direccion+" - "+str(self.telefono)+" - "+self.correo+" - "+self.plan_reciclaje)

class Ficha_Plan(models.Model):
    id_ficha = models.BigAutoField(primary_key=True)
    info_cliente = models.ForeignKey(Cliente, null=True, on_delete=models.SET_NULL)
    info_plan = models.ForeignKey(Plan_reciclaje, null=True, on_delete=models.SET_NULL)
    fecha_retiro = models.DateField(null=True, blank=True)
    fecha_entrega= models.DateField(null=True, blank=True)

    def __str__(self):
        return (self.id_ficha+" - "+self.info_cliente+" - "+self.info_plan+" - "+self.fecha_retiro+" - "+self.fecha_entrega)

class Reporte(models.Model):
    fecha = models.DateField(null=False, blank=False)


