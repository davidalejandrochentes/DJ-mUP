from django.urls import path
from . import views

urlpatterns = [
    path('vehiculo/', views.vehiculo, name="vehiculo"),
    path('alertas/', views.alertas, name="vehiculo_alertas"),
    path('tabla/', views.tabla_mantenimientos, name="vehiculo_tabla_mantenimientos"),
    path('nueva/', views.crear_vehiculo, name="vehiculo_nueva"),
    path('detalles/<int:id>', views.detalles, name="detalles_vehiculo"),
    path('delete/<int:id>', views.eliminar, name="eliminar_vehiculo"),
    path('delete_mantenimiento/<int:id>', views.eliminar_mantenimiento, name="eliminar_mantenimiento_vehiculo"),

    path('mantenimientos_vehiculo/<int:id>/<int:mant>', views.mantenimientos_vehiculo, name="mantenimientos_vehiculo"),
    path('mod_mantenimineto_vehiculo/<int:id>/<int:mant>', views.mod_mantenimineto_vehiculo, name="mod_mantenimineto_vehiculo"),
    path('nuevo_mantenimineto_vehiculo/<int:id>/<int:mant>', views.nuevo_mantenimineto_vehiculo, name="nuevo_mantenimineto_vehiculo"),

    path('documento_general_mantenimientos_vehiculo/', views.documento_general_mantenimientos_vehiculo, name='documento_general_mantenimientos_vehiculo'),
    path('documento_mantenimientos_vehiculo/<int:id>//<int:mant>', views.documento_mantenimientos_vehiculo, name='documento_mantenimientos_vehiculo'),
]
