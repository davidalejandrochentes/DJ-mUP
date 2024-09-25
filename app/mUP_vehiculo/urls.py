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
    
    path('log_in_vehiculo', views.log_in_vehiculo, name="log_in_vehiculo"),
    path('viaje/<int:id>', views.viaje, name="viaje"),
    path('nuevo_viaje_vehiculo/<int:id>', views.nuevo_viaje_vehiculo, name="nuevo_viaje_vehiculo"),
    path('eliminar_viaje/<int:id>', views.eliminar_viaje, name="eliminar_viaje"),
    path('mod_viaje_vehiculo_admin/<int:id>', views.mod_viaje_vehiculo_admin, name="mod_viaje_vehiculo_admin"),

    path('mantenimientos_vehiculo_preventivo/<int:id>', views.mantenimientos_vehiculo_preventivo, name="mantenimientos_vehiculo_preventivo"),
    path('mod_mantenimineto_vehiculo_preventivo/<int:id>', views.mod_mantenimineto_vehiculo_preventivo, name="mod_mantenimineto_vehiculo_preventivo"),
    path('nuevo_mantenimineto_vehiculo_preventivo/<int:id>', views.nuevo_mantenimineto_vehiculo_preventivo, name="nuevo_mantenimineto_vehiculo_preventivo"),

    path('mantenimientos_vehiculo_correctivo/<int:id>', views.mantenimientos_vehiculo_correctivo, name="mantenimientos_vehiculo_correctivo"),
    path('mod_mantenimineto_vehiculo_correctivo/<int:id>', views.mod_mantenimineto_vehiculo_correctivo, name="mod_mantenimineto_vehiculo_correctivo"),
    path('nuevo_mantenimineto_vehiculo_correctivo/<int:id>', views.nuevo_mantenimineto_vehiculo_correctivo, name="nuevo_mantenimineto_vehiculo_correctivo"),
    
    path('mantenimientos_vehiculo_cambio_filtro_aceite/<int:id>', views.mantenimientos_vehiculo_cambio_filtro_aceite, name="mantenimientos_vehiculo_cambio_filtro_aceite"),
    path('mod_mantenimineto_vehiculo_cambio_filtro_aceite/<int:id>', views.mod_mantenimineto_vehiculo_cambio_filtro_aceite, name="mod_mantenimineto_vehiculo_cambio_filtro_aceite"),
    path('nuevo_mantenimineto_vehiculo_cambio_filtro_aceite/<int:id>', views.nuevo_mantenimineto_vehiculo_cambio_filtro_aceite, name="nuevo_mantenimineto_vehiculo_cambio_filtro_aceite"),

    path('mantenimientos_vehiculo_cambio_filtro_aire_combustible/<int:id>', views.mantenimientos_vehiculo_cambio_filtro_aire_combustible, name="mantenimientos_vehiculo_cambio_filtro_aire_combustible"),
    path('mod_mantenimineto_vehiculo_cambio_filtro_aire_combustible/<int:id>', views.mod_mantenimineto_vehiculo_cambio_filtro_aire_combustible, name="mod_mantenimineto_vehiculo_cambio_filtro_aire_combustible"),
    path('nuevo_mantenimineto_vehiculo_cambio_filtro_aire_combustible/<int:id>', views.nuevo_mantenimineto_vehiculo_cambio_filtro_aire_combustible, name="nuevo_mantenimineto_vehiculo_cambio_filtro_aire_combustible"),

    path('mantenimientos_vehiculo_cambio_filtro_caja_corona/<int:id>', views.mantenimientos_vehiculo_cambio_filtro_caja_corona, name="mantenimientos_vehiculo_cambio_filtro_caja_corona"),
    path('mod_mantenimineto_vehiculo_cambio_filtro_caja_corona/<int:id>', views.mod_mantenimineto_vehiculo_cambio_filtro_caja_corona, name="mod_mantenimineto_vehiculo_cambio_filtro_caja_corona"),
    path('nuevo_mantenimineto_vehiculo_cambio_filtro_caja_corona/<int:id>', views.nuevo_mantenimineto_vehiculo_cambio_filtro_caja_corona, name="nuevo_mantenimineto_vehiculo_cambio_filtro_caja_corona"),
    
    path('documento_general_mantenimientos_vehiculo/', views.documento_general_mantenimientos_vehiculo, name='documento_general_mantenimientos_vehiculo'),
    path('documento_mantenimientos_preventivos_vehiculo/<int:id>/', views.documento_mantenimientos_preventivos_vehiculo, name='documento_mantenimientos_preventivos_vehiculo'),
    path('documento_mantenimientos_correctivos_vehiculo/<int:id>/', views.documento_mantenimientos_correctivos_vehiculo, name='documento_mantenimientos_correctivos_vehiculo'),
    path('documento_mantenimientos_cambio_filtro_aceite_vehiculo/<int:id>/', views.documento_mantenimientos_cambio_filtro_aceite_vehiculo, name='documento_mantenimientos_cambio_filtro_aceite_vehiculo'),
    path('documento_mantenimientos_cambio_filtro_aire_combustible_vehiculo/<int:id>/', views.documento_mantenimientos_cambio_filtro_aire_combustible_vehiculo, name='documento_mantenimientos_cambio_filtro_aire_combustible_vehiculo'),
    path('documento_mantenimientos_cambio_filtro_caja_corona_vehiculo/<int:id>/', views.documento_mantenimientos_cambio_filtro_caja_corona_vehiculo, name='documento_mantenimientos_cambio_filtro_caja_corona_vehiculo'),
    path('documento_viajes_vehiculo/<int:id>/', views.documento_viajes_vehiculo, name='documento_viajes_vehiculo'),
]
