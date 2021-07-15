from django.apps import AppConfig


class EjemploConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Aplicación1'

    #def ready(self):
     #   from jobs import updater
      #  updater.start()
