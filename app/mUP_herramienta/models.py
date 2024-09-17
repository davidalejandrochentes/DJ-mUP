from django.db import models
from datetime import date
from datetime import datetime
from django.db.models.signals import post_save, pre_delete, pre_save
from django.dispatch import receiver
import os

    
class Herramienta(models.Model):
    nombre = models.CharField(max_length=100, null=False, blank=False)
    número_de_serie = models.CharField(max_length=100, null=False, blank=False)
    encargado = models.CharField(max_length=100, blank=False, null=False)
    teléfono_encargado = models.CharField(max_length=100, blank=False, null=False)
    descripción = models.TextField(max_length=500, null=False, blank=False)
    fecha_de_adquisición = models.DateField(default=date.today, blank=False, null=False)
    costo = models.IntegerField(blank=False, null=False)
    proveedor = models.CharField(max_length=100, null=False, blank=False)
    ubicación = models.CharField(max_length=100, null=False, blank=False)
    estado_de_la_herramienta = models.CharField(max_length=100, null=False, blank=False)
    fecha_ultimo_mantenimiento = models.DateField(default=date.today, blank=False, null=False)
    intervalo_mantenimiento = models.IntegerField(blank=True, null=True, default=0)
    image = models.ImageField(upload_to="herramienta/image", null=False, blank=False)

    def dias_restantes_mantenimiento(self):
        dias_pasados = (date.today() - self.fecha_ultimo_mantenimiento).days
        dias_restantes = self.intervalo_mantenimiento - dias_pasados
        return dias_restantes 
    
    def __str__(self):
        return self.nombre

class TipoMantenimientoHerramienta(models.Model):
    tipo = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.tipo

class MantenimientoHerramienta(models.Model):
    herramienta = models.ForeignKey(Herramienta, on_delete=models.CASCADE)
    tipo = models.ForeignKey(TipoMantenimientoHerramienta, on_delete=models.CASCADE)
    fecha = models.DateField(default=date.today)
    hora = models.TimeField(default=datetime.now().time())   

    def __str__(self):
        txt = "Herramienta: {}, Tipo: {}, Fecha: {}"
        return txt.format(self.herramienta, self.tipo, self.fecha)
    

@receiver(post_save, sender=MantenimientoHerramienta)
def actualizar_fecha_ultimo_mantenimiento(sender, instance, **kwargs):
    herramienta = instance.herramienta
    if instance.fecha > herramienta.fecha_ultimo_mantenimiento:
        herramienta.fecha_ultimo_mantenimiento = instance.fecha
        herramienta.save()   

@receiver(pre_delete, sender=MantenimientoHerramienta)
def revertir_fecha_ultimo_mantenimiento(sender, instance, **kwargs):
    herramienta = instance.herramienta
    mantenimientos_restantes = MantenimientoHerramienta.objects.filter(herramienta=herramienta).exclude(id=instance.id).order_by('-fecha')
    if mantenimientos_restantes.exists():
        ultimo_mantenimiento = mantenimientos_restantes.first()
        herramienta.fecha_ultimo_mantenimiento = ultimo_mantenimiento.fecha
    else:
        herramienta.fecha_ultimo_mantenimiento = herramienta.fecha_ultimo_mantenimiento  # Otra opción si no hay mantenimientos restantes
    herramienta.save()

@receiver(pre_delete, sender=Herramienta)
def eliminar_imagen_de_herramienta(sender, instance, **kwargs):
    # Verificar si el área tiene una imagen asociada y eliminarla
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)

@receiver(pre_save, sender=Herramienta)
def eliminar_imagen_anterior_al_actualizar(sender, instance, **kwargs):
    if not instance.pk:  # El área es nueva, no hay imagen anterior que eliminar
        return False

    try:
        herramienta_anterior = Herramienta.objects.get(pk=instance.pk)  # Obtener el área anterior de la base de datos
    except Herramienta.DoesNotExist:
        return False  # El área anterior no existe, no hay imagen anterior que eliminar

    if herramienta_anterior.image:  # Verificar si el área anterior tiene una imagen
        nueva_imagen = instance.image
        if herramienta_anterior.image != nueva_imagen:  # Verificar si se ha seleccionado una nueva imagen
            if os.path.isfile(herramienta_anterior.image.path):  # Verificar si el archivo de imagen existe en el sistema de archivos
                os.remove(herramienta_anterior.image.path)
