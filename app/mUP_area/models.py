from django.db import models
from datetime import date
from datetime import datetime
from django.db.models.signals import post_save, pre_delete, pre_save
from django.dispatch import receiver
import os




class Area(models.Model):
    nombre = models.CharField(max_length=100, null=False, blank=False)
    tamaño = models.CharField(max_length=100, blank=False, null=False)
    encargado = models.CharField(max_length=100, blank=False, null=False)
    teléfono_encargado = models.CharField(max_length=100, blank=False, null=False)
    descripción = models.TextField(max_length=500, null=False, blank=False)
    ubicación = models.CharField(max_length=100, null=False, blank=False)
    capacidad = models.CharField(max_length=100, null=False, blank=False)
    tipo_de_área = models.CharField(max_length=100, null=False, blank=False)
    estado_de_ocupación = models.CharField(max_length=100, null=False, blank=False)
    fecha_ultimo_mantenimiento = models.DateField(default=date.today, blank=False, null=False)
    intervalo_mantenimiento = models.IntegerField(blank=False, null=False)
    imagen = models.ImageField(upload_to="area/imagen", null=False, blank=False)

    class Meta:
        indexes = [
            models.Index(fields=['nombre']),
        ]

    def dias_restantes_mantenimiento(self):
        dias_pasados = (date.today() - self.fecha_ultimo_mantenimiento).days
        dias_restantes = self.intervalo_mantenimiento - dias_pasados
        return dias_restantes

    def __str__(self):
        return self.nombre




class TipoMantenimientoArea(models.Model):
    tipo = models.CharField(max_length=100, blank=False, null=False)

    class Meta:
        indexes = [
            models.Index(fields=['tipo']),
        ]

    def __str__(self):
        return self.tipo




class DiasParaAlerta(models.Model):
    días = models.IntegerField(blank=False, null=False, default=7)

    class Meta:
        indexes = [
            models.Index(fields=['días']),
        ]

    def __str__(self):
        txt = "Días para la alerta: {}"
        return txt.format(self.días)    



class MantenimientoArea(models.Model):
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    tipo = models.ForeignKey(TipoMantenimientoArea, on_delete=models.CASCADE)
    fecha_inicio = models.DateField(default=date.today)
    hora_inicio = models.TimeField(default=datetime.now().time()) 
    fecha_fin = models.DateField(default=date.today)
    hora_fin = models.TimeField(default=datetime.now().time())
    operador = models.CharField(max_length=100, blank=False, null=False, default="")
    descripción = models.TextField(max_length=500, null=False, blank=False, default="")
    imagen_antes = models.ImageField(upload_to="area/mantenimiento/antes", null=False, blank=False, default=None) 
    imagen_después = models.ImageField(upload_to="area/mantenimiento/después", null=False, blank=False, default=None)

    class Meta:
        indexes = [
            models.Index(fields=['area']),
        ]

    def __str__(self):
        txt = "Area: {}, Tipo: {}, Fecha: {}"
        return txt.format(self.area, self.tipo, self.fecha_fin)



#--------------------------------- señales ------------------------------------------------------------------

@receiver(post_save, sender=MantenimientoArea)
def actualizar_fecha_ultimo_mantenimiento(sender, instance, **kwargs):
    if instance.tipo.id == 1:  # Verificar si el tipo de mantenimiento tiene id=1
        area = instance.area
        if instance.fecha_fin > area.fecha_ultimo_mantenimiento:
            area.fecha_ultimo_mantenimiento = instance.fecha_fin
            area.save()   

@receiver(pre_delete, sender=MantenimientoArea)
def revertir_fecha_ultimo_mantenimiento(sender, instance, **kwargs):
    if instance.tipo.id == 1:  # Verificar si el tipo de mantenimiento tiene id=1
        area = instance.area
        mantenimientos_restantes = MantenimientoArea.objects.filter(area=area).exclude(id=instance.id).order_by('-fecha_fin')
        if mantenimientos_restantes.exists():
            ultimo_mantenimiento = mantenimientos_restantes.first()
            area.fecha_ultimo_mantenimiento = ultimo_mantenimiento.fecha_fin
        else:
            area.fecha_ultimo_mantenimiento = date.today()  # Otra opción si no hay mantenimientos restantes
        area.save()



#--------------------------------------------------------------------------------------------------------

@receiver(pre_delete, sender=Area)
def eliminar_imagen_de_area(sender, instance, **kwargs):
    # Verificar si el área tiene una imagen asociada y eliminarla
    if instance.imagen:
        if os.path.isfile(instance.imagen.path):
            os.remove(instance.imagen.path)

@receiver(pre_save, sender=Area)
def eliminar_imagen_anterior_al_actualizar(sender, instance, **kwargs):
    if not instance.pk:  # El área es nueva, no hay imagen anterior que eliminar
        return False

    try:
        area_anterior = Area.objects.get(pk=instance.pk)  # Obtener el área anterior de la base de datos
    except Area.DoesNotExist:
        return False  # El área anterior no existe, no hay imagen anterior que eliminar

    if area_anterior.imagen:  # Verificar si el área anterior tiene una imagen
        nueva_imagen = instance.imagen
        if area_anterior.imagen != nueva_imagen:  # Verificar si se ha seleccionado una nueva imagen
            if os.path.isfile(area_anterior.imagen.path):  # Verificar si el archivo de imagen existe en el sistema de archivos
                os.remove(area_anterior.imagen.path)


#---------------------------------------------------------------------------------------------------------

@receiver(pre_delete, sender=MantenimientoArea)
def eliminar_imagen_de_mantenimineto_después(sender, instance, **kwargs):
    # Verificar si la máquina tiene una imagen asociada y eliminarla
    if instance.imagen_después:
        if os.path.isfile(instance.imagen_después.path):
            os.remove(instance.imagen_después.path)

@receiver(pre_save, sender=MantenimientoArea)
def eliminar_imagen_anterior_después_al_actualizar_mantenimineto(sender, instance, **kwargs):
    if not instance.pk:  # La máquina es nueva, no hay imagen anterior que eliminar
        return False

    try:
        mantenimineto_anterior = MantenimientoArea.objects.get(pk=instance.pk)  # Obtener la máquina anterior de la base de datos
    except MantenimientoArea.DoesNotExist:
        return False  # La máquina anterior no existe, no hay imagen anterior que eliminar

    if mantenimineto_anterior.imagen_después:  # Verificar si la máquina anterior tiene una imagen
        nueva_imagen = instance.imagen_después
        if mantenimineto_anterior.imagen_después != nueva_imagen:  # Verificar si se ha seleccionado una nueva imagen
            if os.path.isfile(mantenimineto_anterior.imagen_después.path):  # Verificar si el archivo de imagen existe en el sistema de archivos
                os.remove(mantenimineto_anterior.imagen_después.path)  


#---------------------------------------------------------------------------------------------------------

@receiver(pre_delete, sender=MantenimientoArea)
def eliminar_imagen_de_mantenimineto_antes(sender, instance, **kwargs):
    # Verificar si la máquina tiene una imagen asociada y eliminarla
    if instance.imagen_antes:
        if os.path.isfile(instance.imagen_antes.path):
            os.remove(instance.imagen_antes.path)

@receiver(pre_save, sender=MantenimientoArea)
def eliminar_imagen_anterior_antes_al_actualizar_mantenimineto(sender, instance, **kwargs):
    if not instance.pk:  # La máquina es nueva, no hay imagen anterior que eliminar
        return False

    try:
        mantenimineto_anterior = MantenimientoArea.objects.get(pk=instance.pk)  # Obtener la máquina anterior de la base de datos
    except MantenimientoArea.DoesNotExist:
        return False  # La máquina anterior no existe, no hay imagen anterior que eliminar

    if mantenimineto_anterior.imagen_antes:  # Verificar si la máquina anterior tiene una imagen
        nueva_imagen = instance.imagen_antes
        if mantenimineto_anterior.imagen_antes != nueva_imagen:  # Verificar si se ha seleccionado una nueva imagen
            if os.path.isfile(mantenimineto_anterior.imagen_antes.path):  # Verificar si el archivo de imagen existe en el sistema de archivos
                os.remove(mantenimineto_anterior.imagen_antes.path)  