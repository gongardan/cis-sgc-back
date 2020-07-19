from django.db import models
from .Cliente import Cliente

class Direccion(models.Model):
    class Meta:
        app_label = 'sgc'
    cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE)
    etiqueta = models.CharField(max_length=50) 
    calle = models.CharField(max_length=119)
    numero = models.PositiveIntegerField()    
    colonia = models.CharField(max_length=119)
    cp = models.PositiveIntegerField()
    ciudad = models.CharField(max_length=119)
    interior = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)

