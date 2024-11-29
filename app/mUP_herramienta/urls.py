from django.urls import path
from . import views

urlpatterns = [
    path('herramienta/', views.herramienta, name="herramienta"),
    path('alertas/', views.alertas, name="herramienta_alertas"),
    path('tabla/', views.tabla_mantenimientos, name="herramienta_tabla_mantenimientos"),
    path('nueva/', views.crear_herramienta, name="herramienta_nueva"),
    path('detalles/<int:id>', views.detalles, name="detalles_herramienta"),
    path('delete/<int:id>', views.eliminar, name="eliminar_herramienta"),
    path('delete_mantenimiento/<int:id>', views.eliminar_mantenimiento, name="eliminar_mantenimiento_herramienta"),
    path('descargar_herramientas/', views.descargar_herramientas, name='descargar_herramientas'),
    #path('generar_documento_mantenimientos_por_mes/', views.generar_documento_mantenimientos_por_mes, name='generar_documento_mantenimientos_general_herramienta'),
    #path('generar_documento_mantenimientos_herramienta/<int:id>/', views.generar_documento_mantenimientos_herramienta, name='generar_documento_mantenimientos_herramienta'),
]