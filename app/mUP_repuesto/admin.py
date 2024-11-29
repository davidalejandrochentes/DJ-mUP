from django.contrib import admin
from .models import Maquina, Parte, Inventario


admin.site.register(Maquina)
admin.site.register(Parte)
admin.site.register(Inventario)
