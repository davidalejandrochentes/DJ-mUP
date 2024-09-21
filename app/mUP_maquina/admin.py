from django.contrib import admin
from .models import Maquina, TipoMantenimientoMaquina, MantenimientoMaquina, DiasParaAlerta


admin.site.register(TipoMantenimientoMaquina)
admin.site.register(MantenimientoMaquina)
admin.site.register(DiasParaAlerta)

class MaquinaAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        if obj:  # Verifica si el objeto ya existe (es decir, si se está editando y no creando uno nuevo)
            return ['fecha_ultimo_mantenimiento']
        else:
            return []

admin.site.register(Maquina, MaquinaAdmin)
