from django.urls import path
from . import views

urlpatterns = [
    path('pc/', views.pc, name="pc"),
    path('alertas/', views.alertas, name="pc_alertas"),
    path('tabla/', views.tabla_mantenimientos, name="pc_tabla_mantenimientos"),
    path('nueva/', views.crear_pc, name="pc_nueva"),
    path('detalles/<int:id>', views.detalles, name="detalles_pc"),
    path('delete/<int:id>', views.eliminar, name="eliminar_pc"),

    path('mantenimientos_pc_preventivos/<int:id>', views.mantenimientos_pc_preventivos, name="mantenimientos_pc_preventivos"),
    path('mod_mantenimiento_pc_preventivo/<int:id>', views.mod_mantenimiento_pc_preventivo, name="mod_mantenimiento_pc_preventivo"),
    path('nuevo_mantenimiento_pc_preventivo/<int:id>', views.nuevo_mantenimiento_pc_preventivo, name="nuevo_mantenimiento_pc_preventivo"),

    path('mantenimientos_pc_correctivos/<int:id>', views.mantenimientos_pc_correctivos, name="mantenimientos_pc_correctivos"),
    path('mod_mantenimiento_pc_correctivo/<int:id>', views.mod_mantenimiento_pc_correctivo, name="mod_mantenimiento_pc_correctivo"),
    path('nuevo_mantenimiento_pc_correctivo/<int:id>', views.nuevo_mantenimiento_pc_correctivo, name="nuevo_mantenimiento_pc_correctivo"),

    path('delete_mantenimiento/<int:id>', views.eliminar_mantenimiento, name="eliminar_mantenimiento_pc"),
    
    path('documento_general_mantenimientos_pc/', views.documento_general_mantenimientos_pc, name='documento_general_mantenimientos_pc'),
    path('documento_mantenimientos_preventivos_pc/<int:id>/', views.documento_mantenimientos_preventivos_pc, name='documento_mantenimientos_preventivos_pc'),
    path('documento_mantenimientos_correctivos_pc/<int:id>/', views.documento_mantenimientos_correctivos_pc, name='documento_mantenimientos_correctivos_pc'),
]
