from django.urls import path
from . import views

urlpatterns = [
    path('area/', views.area, name="area"),
    path('alertas/', views.alertas, name="area_alertas"),
    path('tabla/', views.tabla_mantenimientos, name="area_tabla_mantenimientos"),
    path('nueva/', views.crear_area, name="area_nueva"),
    path('detalles/<int:id>', views.detalles, name="detalles_area"),
    path('delete/<int:id>', views.eliminar, name="eliminar_area"),

    path('mantenimientos_area/<int:id>/<int:mant>', views.mantenimientos_area, name="mantenimientos_area"),
    path('mod_mantenimiento_area/<int:id>/<int:mant>', views.mod_mantenimiento_area, name="mod_mantenimiento_area"),
    path('nuevo_mantenimiento_area/<int:id>/<int:mant>', views.nuevo_mantenimiento_area, name="nuevo_mantenimiento_area"),
    
    path('delete_mantenimiento/<int:id>', views.eliminar_mantenimiento, name="eliminar_mantenimiento_area"),
    
    path('documento_general_mantenimientos_area/', views.documento_general_mantenimientos_area, name='documento_general_mantenimientos_area'),
    path('documento_mantenimientos_area/<int:id>/<int:mant>', views.documento_mantenimientos_area, name='documento_mantenimientos_area'),
]