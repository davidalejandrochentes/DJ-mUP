from django.contrib import admin
from .models import PC, TipoMantenimientoPC, MantenimientoPC, DiasParaAlerta


admin.site.register(TipoMantenimientoPC)
admin.site.register(MantenimientoPC)
admin.site.register(DiasParaAlerta)

class PCAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        if obj:  # Verifica si el objeto ya existe (es decir, si se está editando y no creando uno nuevo)
            return ['fecha_ultimo_mantenimiento']
        else:
            return []

admin.site.register(PC, PCAdmin)
