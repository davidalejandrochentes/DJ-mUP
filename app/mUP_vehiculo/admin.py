from django.contrib import admin
from .models import Vehiculo, TipoMantenimientoVehiculo, MantenimientoVehiculo, KmParaAlerta

admin.site.register(TipoMantenimientoVehiculo)
admin.site.register(MantenimientoVehiculo)
admin.site.register(KmParaAlerta)

class VehiculoAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        if obj:  # Verifica si el objeto ya existe (es decir, si se está editando y no creando uno nuevo)
            return ['fecha_ultimo_mantenimiento']
        else:
            return []

admin.site.register(Vehiculo, VehiculoAdmin)