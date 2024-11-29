from django.urls import path
from . import views

urlpatterns = [
    path('repuesto_maquina/', views.repuesto_maquina, name="repuesto_maquina"),
    path('eliminar_repuesto_maquina/<int:id>', views.eliminar_repuesto_maquina, name="eliminar_repuesto_maquina"),
    path('detalles_repuesto_maquina/<int:id>', views.detalles, name="detalles_repuesto_maquina"),
    path('mod_inventario/<int:id>', views.mod_inventario, name="mod_inventario"),
    path('actualizar_inventario/<int:id>/', views.actualizar_inventario, name='actualizar_inventario'),
    path('eliminar_inventario/<int:id>', views.eliminar_inventario, name="eliminar_inventario"),
    path('descargar-excel/<int:id>/', views.descargar_excel, name='descargar_excel'),
    path('tabla_repuesto_general/', views.tabla_general, name='tabla_general'),
    path('descargar_excel_general/', views.descargar_excel_general, name='descargar_excel_general'),
    path('alertas_repuesto/', views.alerta_repuesto, name='alerta_repuesto'),
]