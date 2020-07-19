from django.db import models

class Cliente(models.Model):
    class Meta:
        app_label = 'sgc'
    razonsocial = models.CharField(max_length=119)
    rfc = models.CharField(max_length=15)
   
    
