from django.db import models
from .Cliente import Cliente

class Cotizacion(models.Model):
    class Meta:
        app_label = 'sgc'
    cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE)
    creadopor = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    fechacreacion = models.DateTimeField(auto_now=True)
    descripcionservicio = models.TextField()
    moneda = models.CharField(max_length=5,choices=[("MXN","PESOS MEXICANOS"),("USD","DOLARES")])
    total = models.DecimalField(max_digits=17,decimal_places=2)
    riesgoimparcialidad = models.BooleanField(default=False)
