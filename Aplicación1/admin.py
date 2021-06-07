from django.contrib import admin

# Register your models here.
from Aplicación1.models import *

admin.site.register(Plan_reciclaje)
admin.site.register(Cliente)
admin.site.register(Ficha_Plan)
admin.site.register(Reporte)