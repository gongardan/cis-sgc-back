from django.db import models

class UnidadVerificacion(models.Model):
    class Meta:
        app_label = 'sgc'
    nombre = models.CharField(max_length=119)
    acronimo = models.CharField(max_length=119)
    rfc = models.CharField(max_length=50)
    directorgeneral = models.CharField(max_length = 119)
    telefono = models.CharField(max_length = 119)
    correo = models.EmailField(max_length=119)
    domicilio = models.CharField(max_length=119)
    imagen = models.FileField(upload_to='uploads/%Y/%m/%d/')
