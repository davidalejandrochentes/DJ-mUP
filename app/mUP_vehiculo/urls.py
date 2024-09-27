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
    path('documento_mantenimientos_preventivos_vehiculo/<int:id>/', views.documento_mantenimientos_preventivos_vehiculo, name='documento_mantenimientos_preventivos_vehiculo'),
    path('documento_mantenimientos_correctivos_vehiculo/<int:id>/', views.documento_mantenimientos_correctivos_vehiculo, name='documento_mantenimientos_correctivos_vehiculo'),
    path('documento_mantenimientos_cambio_filtro_aceite_vehiculo/<int:id>/', views.documento_mantenimientos_cambio_filtro_aceite_vehiculo, name='documento_mantenimientos_cambio_filtro_aceite_vehiculo'),
    path('documento_mantenimientos_cambio_filtro_aire_combustible_vehiculo/<int:id>/', views.documento_mantenimientos_cambio_filtro_aire_combustible_vehiculo, name='documento_mantenimientos_cambio_filtro_aire_combustible_vehiculo'),
    path('documento_mantenimientos_cambio_filtro_caja_corona_vehiculo/<int:id>/', views.documento_mantenimientos_cambio_filtro_caja_corona_vehiculo, name='documento_mantenimientos_cambio_filtro_caja_corona_vehiculo'),
    path('documento_viajes_vehiculo/<int:id>/', views.documento_viajes_vehiculo, name='documento_viajes_vehiculo'),
]
