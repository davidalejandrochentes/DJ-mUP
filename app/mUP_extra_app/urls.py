from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.log_in, name="login"),
    path('logout/', views.log_out, name="logout"), 
    path('soporte/', views.soporte, name="soporte"),
    path('info/', views.info, name="info"),

    path('manual_area/', views.manual_area, name="manual_area"),
    path('manual_herramienta/', views.manual_herramienta, name="manual_herramienta"),
    path('manual_maquina/', views.manual_maquina, name="manual_maquina"),
    path('manual_pc/', views.manual_pc, name="manual_pc"),
    path('manual_repuesto/', views.manual_repuesto, name="manual_repuesto"),
    path('info/manual_vehiculo', views.manual_vehiculo, name="manual_vehiculo"),
]