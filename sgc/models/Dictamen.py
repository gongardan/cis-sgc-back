from django.db import models
from .Fc00 import Fc00
from .ActaVerificacion import ActaVerificacion
class Dictamen(models.Model):
    class Meta:
        app_label = 'sgc'
    actaverificacion = models.ForeignKey(to=ActaVerificacion,on_delete=models.CASCADE)
    creadopor = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    