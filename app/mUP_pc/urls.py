from django.urls import path
from . import views

urlpatterns = [
    path('pc/', views.pc, name="pc"),
    path('alertas/', views.alertas, name="pc_alertas"),
    path('tabla/', views.tabla_mantenimientos, name="pc_tabla_mantenimientos"),
    path('nueva/', views.crear_pc, name="pc_nueva"),
    path('detalles/<int:id>', views.detalles, name="detalles_pc"),
    path('delete/<int:id>', views.eliminar, name="eliminar_pc"),

    path('mantenimientos_pc/<int:id>/<int:mant>', views.mantenimientos_pc, name="mantenimientos_pc"),
    path('mod_mantenimiento_pc/<int:id>/<int:mant>', views.mod_mantenimiento_pc, name="mod_mantenimiento_pc"),
    path('nuevo_mantenimiento_pc/<int:id>/<int:mant>', views.nuevo_mantenimiento_pc, name="nuevo_mantenimiento_pc"),

    path('delete_mantenimiento/<int:id>', views.eliminar_mantenimiento, name="eliminar_mantenimiento_pc"),
    
    path('documento_general_mantenimientos_pc/', views.documento_general_mantenimientos_pc, name='documento_general_mantenimientos_pc'),
    path('documento_mantenimientos_pc/<int:id>/<int:mant>', views.documento_mantenimientos_pc, name='documento_mantenimientos_pc'),
]
