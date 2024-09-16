from django.contrib import admin
from .models import Area, TipoMantenimientoArea, MantenimientoArea


admin.site.register(TipoMantenimientoArea)
admin.site.register(MantenimientoArea)

class AreaAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        if obj:  # Verifica si el objeto ya existe (es decir, si se está editando y no creando uno nuevo)
            return ['fecha_ultimo_mantenimiento']
        else:
            return []

admin.site.register(Area, AreaAdmin)