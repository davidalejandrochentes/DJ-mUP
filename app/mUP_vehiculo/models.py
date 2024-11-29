from django.db import models
from datetime import date
from datetime import datetime
from django.db.models.signals import post_save, pre_delete, pre_save
from django.dispatch import receiver
import os




class Vehiculo(models.Model):
    marca = models.CharField(max_length=50, null=False, blank=False)
    modelo = models.CharField(max_length=50, null=False, blank=False)
    matrícula = models.CharField(max_length=50, null=False, blank=False)
    número_de_chasis = models.CharField(max_length=50, null=False, blank=False)
    capacidad_de_carga = models.CharField(max_length=50, null=False, blank=False)
    uso_del_vehiculo = models.CharField(max_length=50, null=False, blank=False)
    km_recorridos = models.BigIntegerField(blank=False, null=False)
    
    intervalo_mantenimiento = models.IntegerField(blank=False, null=False)
    intervalo_cambio_filtro_aceite = models.IntegerField(blank=False, null=False)
    intervalo_cambio_filtro_aire_combustible = models.IntegerField(blank=False, null=False)
    intervalo_cambio_aceite_caja_corona = models.IntegerField(blank=False, null=False)

    imagen = models.ImageField(upload_to="vehiculo/image", null=False, blank=False)
    fecha_ultimo_mantenimiento = models.DateField(default=date.today, blank=False, null=False)

    nombre_chofer = models.CharField(max_length=50, null=False, blank=False)
    teléfono_chofer = models.CharField(max_length=10, blank=False, null=False)
    dirección_chofer = models.CharField(max_length=30, blank=False, null=False)
    dni_chofer = models.BigIntegerField(max_length=20, blank=True, null=True, default=0)

    
    def obtener_km_restantes(self, tipo_mantenimiento_id, intervalo):
        ultimo_mantenimiento = MantenimientoVehiculo.objects.filter(vehiculo=self, tipo__id=tipo_mantenimiento_id).order_by('-fecha_fin').first()
        km_recorridos_ultimo_mantenimiento = ultimo_mantenimiento.km_recorridos if ultimo_mantenimiento else 0
        proximo_mantenimiento = km_recorridos_ultimo_mantenimiento + intervalo
        return proximo_mantenimiento - self.km_recorridos


    def km_restantes_mantenimiento_correctivo(self):
        return self.obtener_km_restantes(1, self.intervalo_mantenimiento)


    def km_restantes_intervalo_cambio_filtro_aceite(self):
        return self.obtener_km_restantes(3, self.intervalo_cambio_filtro_aceite)


    def km_restantes_intervalo_cambio_filtro_aire_combustible(self):
        return self.obtener_km_restantes(4, self.intervalo_cambio_filtro_aire_combustible)


    def km_restantes_intervalo_cambio_aceite_caja_corona(self):
        return self.obtener_km_restantes(5, self.intervalo_cambio_aceite_caja_corona)

    def __str__(self):
        return self.modelo




class TipoMantenimientoVehiculo(models.Model):
    tipo = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.tipo  




class KmParaAlerta(models.Model):
    km = models.IntegerField(blank=False, null=False)

    def __str__(self):
        txt = "Km para la alerta: {}"
        return txt.format(self.km)  




class MantenimientoVehiculo(models.Model):
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    tipo = models.ForeignKey(TipoMantenimientoVehiculo, on_delete=models.CASCADE)
    fecha_inicio = models.DateField(default=date.today)
    hora_inicio = models.TimeField(default=datetime.now().time())
    fecha_fin = models.DateField(default=date.today)
    hora_fin = models.TimeField(default=datetime.now().time())
    km_recorridos = models.BigIntegerField(blank=False, null=False)
    operador = models.CharField(max_length=100, blank=False, null=False)
    descripción = models.TextField(max_length=400, null=False, blank=False)
    partes_y_piezas = models.TextField(max_length=400, null=False, blank=False)
    imagen = models.ImageField(upload_to="vehiculo/mantenimiento/imagen", null=False, blank=False, default=None)

    def __str__(self):
        txt = "Vehiculo: {}, Tipo: {}, Fecha: {}"
        return txt.format(self.vehiculo, self.tipo, self.fecha_fin)



#----------signals------------------------------------------------------------------------------

@receiver(post_save, sender=MantenimientoVehiculo)
def actualizar_fecha_ultimo_mantenimiento(sender, instance, **kwargs):
    vehiculo = instance.vehiculo
    if instance.fecha_fin > vehiculo.fecha_ultimo_mantenimiento:
        vehiculo.fecha_ultimo_mantenimiento = instance.fecha_fin
        vehiculo.save()




@receiver(pre_delete, sender=MantenimientoVehiculo)
def revertir_fecha_ultimo_mantenimiento(sender, instance, **kwargs):
    vehiculo = instance.vehiculo
    mantenimientos_restantes = MantenimientoVehiculo.objects.filter(vehiculo=vehiculo).exclude(id=instance.id).order_by('-fecha_fin')
    if mantenimientos_restantes.exists():
        ultimo_mantenimiento = mantenimientos_restantes.first()
        vehiculo.fecha_ultimo_mantenimiento = ultimo_mantenimiento.fecha_fin
    else:
        vehiculo.fecha_ultimo_mantenimiento = date.today()  # Otra opción si no hay mantenimientos restantes
    vehiculo.save()


#-----------------------------------------------------------------------------------------------------------------------------

@receiver(pre_delete, sender=Vehiculo)
def eliminar_imagen_de_vehiculo(sender, instance, **kwargs):
    # Verificar si Vehiculo tiene una imagen asociada y eliminarla
    if instance.imagen:
        if os.path.isfile(instance.imagen.path):
            os.remove(instance.imagen.path)



@receiver(pre_save, sender=Vehiculo)
def eliminar_imagen_anterior_al_actualizar(sender, instance, **kwargs):
    if not instance.pk:  # Vehiculo es nuevo, no hay imagen anterior que eliminar
        return False

    try:
        vehiculo_anterior = Vehiculo.objects.get(pk=instance.pk)  # Obtener Vehiculo anterior de la base de datos
    except Vehiculo.DoesNotExist:
        return False  # Vehiculo anterior no existe, no hay imagen anterior que eliminar

    if vehiculo_anterior.imagen:  # Verificar si Vehiculo anterior tiene una imagen
        nueva_imagen = instance.imagen
        if vehiculo_anterior.imagen != nueva_imagen:  # Verificar si se ha seleccionado una nueva imagen
            if os.path.isfile(vehiculo_anterior.imagen.path):  # Verificar si el archivo de imagen existe en el sistema de archivos
                os.remove(vehiculo_anterior.imagen.path)


#-----------------------------------------------------------------------------------------------------------------------------
@receiver(pre_delete, sender=MantenimientoVehiculo)
def eliminar_imagen_de_mantenimineto(sender, instance, **kwargs):
    # Verificar si Vehiculo tiene una imagen asociada y eliminarla
    if instance.imagen:
        if os.path.isfile(instance.imagen.path):
            os.remove(instance.imagen.path)

@receiver(pre_save, sender=MantenimientoVehiculo)
def eliminar_imagen_anterior_al_actualizar_mantenimineto(sender, instance, **kwargs):
    if not instance.pk:
        return False

    try:
        mantenimiento_anterior = MantenimientoVehiculo.objects.get(pk=instance.pk)
    except MantenimientoVehiculo.DoesNotExist:
        return False

    # Comparar y eliminar image
    if mantenimiento_anterior.imagen and instance.imagen != mantenimiento_anterior.imagen:
        if os.path.isfile(mantenimiento_anterior.imagen.path):
            os.remove(mantenimiento_anterior.imagen.path)

#---------------------------------------------------------------------------------------------


