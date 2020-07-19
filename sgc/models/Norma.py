from django.db import models
from .Verificador import Verificador

class Norma(models.Model):
    class Meta:
        app_label = 'sgc'
    nombre = models.CharField(max_length=119)
    codigo = models.CharField(max_length=50)
    acreditacion = models.CharField(max_length=110)
    vigenciadictamen = models.CharField(max_length=30)
    tipoproceso = models.CharField(max_length=30)
    tiemporealizaciondictamenes = models.CharField(max_length=30)
    vigenciacotizacion = models.CharField(max_length=50)
    gerentetecnico = models.ForeignKey(Verificador,on_delete=models.CASCADE,related_name="normagerentetecnico")
    gerentetecnicosustituto = models.ForeignKey(Verificador,on_delete=models.CASCADE,related_name="normagerentesustituto")# TODO si esta bien que sean llaves o mejor texto ...