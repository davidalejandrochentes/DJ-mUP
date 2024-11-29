from django.db import models
from datetime import date
from datetime import datetime
from django.db.models.signals import post_save, pre_delete, pre_save
from django.dispatch import receiver
import os




class PC(models.Model):
    nombre = models.CharField(max_length=100, null=False, blank=False)
    modelo = models.CharField(max_length=100, null=False, blank=False)
    número_de_inventario = models.CharField(max_length=100, blank=False, null=False)
    encargado = models.CharField(max_length=100, blank=False, null=False)
    teléfono_encargado = models.CharField(max_length=100, blank=False, null=False)
    descripción = models.TextField(max_length=500, null=False, blank=False)
    ubicación = models.CharField(max_length=100, null=False, blank=False)
    costo_de_adquisición = models.IntegerField(blank=False, null=False)
    fecha_de_adquisición = models.DateField(default=date.today, blank=False, null=False)
    fecha_de_retirada = models.DateField(default=date.today, blank=False, null=False)
    estado = models.CharField(max_length=100, null=False, blank=False)
    garantía = models.CharField(max_length=100, null=False, blank=False)
    software_instalado = models.CharField(max_length=100, null=False, blank=False)
    fecha_ultimo_mantenimiento = models.DateField(default=date.today, blank=False, null=False)
    intervalo_mantenimiento = models.IntegerField(blank=False, null=False)
    imagen = models.ImageField(upload_to="pc/imagen", null=False, blank=False)

    def dias_restantes_mantenimiento(self):
        dias_pasados = (date.today() - self.fecha_ultimo_mantenimiento).days
        dias_restantes = self.intervalo_mantenimiento - dias_pasados
        return dias_restantes 
    
    def __str__(self):
        return self.nombre




class TipoMantenimientoPC(models.Model):
    tipo = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.tipo


class DiasParaAlerta(models.Model):
    días = models.IntegerField(blank=False, null=False, default=7)

    def __str__(self):
        txt = "Días para la alerta: {}"
        return txt.format(self.días)  




class MantenimientoPC(models.Model):
    pc = models.ForeignKey(PC, on_delete=models.CASCADE)
    tipo = models.ForeignKey(TipoMantenimientoPC, on_delete=models.CASCADE)
    fecha_inicio = models.DateField(default=date.today)
    hora_inicio = models.TimeField(default=datetime.now().time()) 
    fecha_fin = models.DateField(default=date.today)
    hora_fin = models.TimeField(default=datetime.now().time())
    operador = models.CharField(max_length=100, blank=False, null=False, default="")
    partes_y_piezas = models.TextField(max_length=500, null=False, blank=False, default="")
    descripción = models.TextField(max_length=500, null=False, blank=False, default="")
    imagen = models.ImageField(upload_to="pc/mantenimiento/imagen", null=False, blank=False, default=None)   

    def __str__(self):
        txt = "Equipo: {}, Tipo: {}, Fecha: {}"
        return txt.format(self.pc, self.tipo, self.fecha_fin)
    



@receiver(post_save, sender=MantenimientoPC)
def actualizar_fecha_ultimo_mantenimiento(sender, instance, **kwargs):
    if instance.tipo.id == 1:
        pc = instance.pc
        if instance.fecha_fin > pc.fecha_ultimo_mantenimiento:
            pc.fecha_ultimo_mantenimiento = instance.fecha_fin
            pc.save()   

@receiver(pre_delete, sender=MantenimientoPC)
def revertir_fecha_ultimo_mantenimiento(sender, instance, **kwargs):
    if instance.tipo.id == 1:
        pc = instance.pc
        mantenimientos_restantes = MantenimientoPC.objects.filter(pc=pc).exclude(id=instance.id).order_by('-fecha_fin')
        if mantenimientos_restantes.exists():
            ultimo_mantenimiento = mantenimientos_restantes.first()
            pc.fecha_ultimo_mantenimiento = ultimo_mantenimiento.fecha_fin
        else:
            pc.fecha_ultimo_mantenimiento = date.today()  # Otra opción si no hay mantenimientos restantes
        pc.save()

@receiver(pre_delete, sender=PC)
def eliminar_imagen_de_pc(sender, instance, **kwargs):
    # Verificar si el área tiene una imagen asociada y eliminarla
    if instance.imagen:
        if os.path.isfile(instance.imagen.path):
            os.remove(instance.imagen.path)

@receiver(pre_save, sender=PC)
def eliminar_imagen_anterior_al_actualizar(sender, instance, **kwargs):
    if not instance.pk:  # El área es nueva, no hay imagen anterior que eliminar
        return False

    try:
        pc_anterior = PC.objects.get(pk=instance.pk)  # Obtener el área anterior de la base de datos
    except PC.DoesNotExist:
        return False  # El área anterior no existe, no hay imagen anterior que eliminar

    if pc_anterior.imagen:  # Verificar si el área anterior tiene una imagen
        nueva_imagen = instance.imagen
        if pc_anterior.imagen != nueva_imagen:  # Verificar si se ha seleccionado una nueva imagen
            if os.path.isfile(pc_anterior.imagen.path):  # Verificar si el archivo de imagen existe en el sistema de archivos
                os.remove(pc_anterior.imagen.path)

#-----------------------------------------------------------------------------------------------------------------------------
@receiver(pre_delete, sender=MantenimientoPC)
def eliminar_imagen_de_mantenimineto(sender, instance, **kwargs):
    # Verificar si la máquina tiene una imagen asociada y eliminarla
    if instance.imagen:
        if os.path.isfile(instance.imagen.path):
            os.remove(instance.imagen.path)

@receiver(pre_save, sender=MantenimientoPC)
def eliminar_imagen_anterior_al_actualizar_mantenimineto(sender, instance, **kwargs):
    if not instance.pk:  # La máquina es nueva, no hay imagen anterior que eliminar
        return False

    try:
        mantenimineto_anterior = MantenimientoPC.objects.get(pk=instance.pk)  # Obtener la máquina anterior de la base de datos
    except MantenimientoPC.DoesNotExist:
        return False  # La máquina anterior no existe, no hay imagen anterior que eliminar

    if mantenimineto_anterior.imagen:  # Verificar si la máquina anterior tiene una imagen
        nueva_imagen = instance.imagen
        if mantenimineto_anterior.imagen != nueva_imagen:  # Verificar si se ha seleccionado una nueva imagen
            if os.path.isfile(mantenimineto_anterior.imagen.path):  # Verificar si el archivo de imagen existe en el sistema de archivos
                os.remove(mantenimineto_anterior.imagen.path)     