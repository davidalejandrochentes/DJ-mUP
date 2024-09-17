from django.db import models
from datetime import date
from datetime import datetime
from django.db.models.signals import post_save, pre_delete, pre_save
from django.dispatch import receiver
import os

# Create your models here.
class Maquina(models.Model):
    nombre = models.CharField(max_length=100, null=False, blank=False)
    
    def __str__(self):
        return self.nombre


class Parte(models.Model):
    maquina = models.ForeignKey(Maquina, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    image = models.ImageField(upload_to="repuesto/image", null=False, blank=False, default=None) 
    
    def __str__(self):
        return self.nombre


class Inventario(models.Model):
    parte = models.ForeignKey(Parte, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=50, null=False, blank=False, default="")
    rosca = models.CharField(max_length=50, null=False, blank=False, default="")
    largo = models.CharField(max_length=50, null=False, blank=False, default="")
    und = models.CharField(max_length=50, null=False, blank=False, default="")
    cantidad_necesaria = models.IntegerField(null=False, blank=False)
    existencia_stock = models.IntegerField(null=False, blank=False)
    salida = models.IntegerField(null=False, blank=False)

    def existencia_fisica(self):
        cantidad_existencia_fisica = self.existencia_stock - self.salida
        return cantidad_existencia_fisica 
    
    def __str__(self):
        txt = "Parte: {}"
        return txt.format(self.parte)


#---------------------------------------------------------------------------------------------
@receiver(pre_delete, sender=Parte)
def eliminar_imagen_de_repuesto(sender, instance, **kwargs):
    # Verificar si la máquina tiene una imagen asociada y eliminarla
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)
