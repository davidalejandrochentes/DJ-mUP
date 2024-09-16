from django.urls import path
from . import views

urlpatterns = [
    path('area/', views.area, name="area"),
    path('alertas/', views.alertas, name="area_alertas"),
    path('tabla/', views.tabla_mantenimientos, name="area_tabla_mantenimientos"),
    path('nueva/', views.crear_area, name="area_nueva"),
    path('detalles/<int:id>', views.detalles, name="detalles_area"),
    path('delete/<int:id>', views.eliminar, name="eliminar_area"),

    path('mantenimientos_area_preventivo/<int:id>', views.mantenimientos_area_preventivo, name="mantenimientos_area_preventivo"),
    path('mod_mantenimineto_area_preventivo/<int:id>', views.mod_mantenimineto_area_preventivo, name="mod_mantenimineto_area_preventivo"),
    path('nuevo_mantenimineto_area_preventivo/<int:id>', views.nuevo_mantenimineto_area_preventivo, name="nuevo_mantenimineto_area_preventivo"),
    
    path('mantenimientos_area_correctivo/<int:id>', views.mantenimientos_area_correctivo, name="mantenimientos_area_correctivo"),
    path('mod_mantenimineto_area_correctivo/<int:id>', views.mod_mantenimineto_area_correctivo, name="mod_mantenimineto_area_correctivo"),
    path('nuevo_mantenimineto_area_correctivo/<int:id>', views.nuevo_mantenimineto_area_correctivo, name="nuevo_mantenimineto_area_correctivo"),
    
    path('delete_mantenimiento/<int:id>', views.eliminar_mantenimiento, name="eliminar_mantenimiento_area"),
    
    path('documento_general_mantenimientos_area/', views.documento_general_mantenimientos_area, name='documento_general_mantenimientos_area'),
    path('documento_mantenimientos_preventivos_area/<int:id>/', views.documento_mantenimientos_preventivos_area, name='documento_mantenimientos_preventivos_area'),
    path('documento_mantenimientos_correctivos_area/<int:id>/', views.documento_mantenimientos_correctivos_area, name='documento_mantenimientos_correctivos_area'),
]