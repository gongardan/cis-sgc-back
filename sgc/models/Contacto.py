from django.db import models
from .Cliente import Cliente

class Contacto(models.Model):
    class Meta:
        app_label = 'sgc'
    cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE)
    nombrecontacto = models.CharField(max_length=119)
    emailcontacto = models.EmailField()
    telefonocontacto = models.CharField(max_length=15)
    etiqueta = models.CharField(max_length=50)