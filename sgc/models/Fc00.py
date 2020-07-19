from django.db import models
from .OrdenTrabajo import OrdenTrabajo

class Fc00(models.Model):
    class Meta:
        app_label = 'sgc'
    ordentrabajo = models.ForeignKey(to=OrdenTrabajo,on_delete=models.CASCADE)
    