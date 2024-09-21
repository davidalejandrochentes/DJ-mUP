from django.urls import path
from . import views

urlpatterns = [
    path('maquina/', views.maquina, name="maquina"),
    path('alertas/', views.alertas, name="maquina_alertas"),
    path('tabla/', views.tabla_mantenimientos, name="maquina_tabla_mantenimientos"),
    path('nueva/', views.crear_maquina, name="maquina_nueva"),
    path('detalles/<int:id>', views.detalles, name="detalles_maquina"),
    path('delete/<int:id>', views.eliminar, name="eliminar_maquina"),

    path('mantenimientos_maquina_preventivo/<int:id>', views.mantenimientos_maquina_preventivo, name="mantenimientos_maquina_preventivo"),
    path('mod_mantenimineto_maquina_preventivo/<int:id>', views.mod_mantenimineto_maquina_preventivo, name="mod_mantenimineto_maquina_preventivo"),
    path('nuevo_mantenimineto_maquina_preventivo/<int:id>', views.nuevo_mantenimineto_maquina_preventivo, name="nuevo_mantenimineto_maquina_preventivo"),

    path('mantenimientos_maquina_correctivo/<int:id>', views.mantenimientos_maquina_correctivo, name="mantenimientos_maquina_correctivo"),
    path('mod_mantenimineto_maquina_correctivo/<int:id>', views.mod_mantenimineto_maquina_correctivo, name="mod_mantenimineto_maquina_correctivo"),
    path('nuevo_mantenimineto_maquina_correctivo/<int:id>', views.nuevo_mantenimineto_maquina_correctivo, name="nuevo_mantenimineto_maquina_correctivo"),

    path('delete_mantenimiento/<int:id>', views.eliminar_mantenimiento, name="eliminar_mantenimiento_maquina"),
    
    path('documento_general_mantenimientos_maquina/', views.documento_general_mantenimientos_maquina, name='documento_general_mantenimientos_maquina'),
    path('documento_mantenimientos_preventivos_maquina/<int:id>/', views.documento_mantenimientos_preventivos_maquina, name='documento_mantenimientos_preventivos_maquina'),
    path('documento_mantenimientos_correctivos_maquina/<int:id>/', views.documento_mantenimientos_correctivos_maquina, name='documento_mantenimientos_correctivos_maquina'),
]
