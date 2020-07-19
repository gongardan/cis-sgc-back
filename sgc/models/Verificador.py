from django.db import models
#from .Norma import Norma

class Verificador(models.Model):
    class Meta:
        app_label = 'sgc'
    nombre = models.CharField(max_length=119)
    #normas =  models.ManyToManyField(Norma)
    user = models.ForeignKey('auth.User',on_delete=models.CASCADE)