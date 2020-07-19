from django.db import models
from .Cotizacion import Cotizacion

class ItemPropuestaEconomica(models.Model):
    class Meta:
        app_label = 'sgc'
    cotizacion = models.ForeignKey(Cotizacion,on_delete=models.CASCADE)
    areaverificar = models.CharField(max_length=119)
    costounitario = models.DecimalField(max_digits=17,decimal_places=2)
    costototal = models.DecimalField(max_digits=17,decimal_places=2)
    #TODO : No se incrementa en automatice, es la cantidad de verificaciones etc