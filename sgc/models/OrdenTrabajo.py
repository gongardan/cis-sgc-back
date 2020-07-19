from django.db import models
from .Contacto import Contacto
from .Cotizacion import Cotizacion
from .Verificador import Verificador

class OrdenTrabajo(models.Model):
    class Meta:
        app_label = 'sgc'
    cotizacion = models.ForeignKey(Cotizacion,on_delete = models.CASCADE)
    fechacreacion = models.DateTimeField(auto_now_add=True)
    fechafinalizacion = models.DateTimeField()
    fechaprogramada = models.DateField()
    fecharecibo = models.DateField()
    # TODO: la fecharecibo puede ser distinta de la finalizacion y programada?
    # las fechas estaria bien que todas sean datetimes?

    creadopor = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    atenderavisita = models.ForeignKey(Contacto,on_delete=models.CASCADE)
    # TODO verificador siempre se pone uno por orden de trabajo?
    verificador = models.ForeignKey(Verificador,on_delete=models.CASCADE)
    
    objetivoverificacion = models.TextField()
    #TODO el nombre o identificacion de las areas a verificar vienen directo de la orden de trabajo
    condicionevisita = models.TextField(verbose_name="Condiciones para realizar antes de la verificacion")
    #TODO el equipo de seguridad puede ser un select, siempre va este, es ocpcional...?
    quiposeguridad = models.TextField(default="El requerido por la empresa")
    #TODO pueden ser documental y/o fisica o solamente una u otra,(podria ser tambien un select), 
    #son iguales en todas las normas, se pueden aunentar, etc?
    documental = models.BooleanField(default=False)
    fisica = models.BooleanField(default=False)
    entrevistapersonal = models.BooleanField(default=False)
    # TODO: condiciones especificas de centro de trabajo  van de una configuracion por norma?
    # se seleccinan de un catalogo o algo asi dependiendo de la orden de trabajo?
    #TODO: evidencia fisica solicitada igual que arriba, es por norma, se selecciona dependiendo de la orden de trabajo? etc
    #TODO elClienteSeCompromete a ... igual, que dos anteriores... va por default "Proporcionar las condiciones solicitadas y atender la veridicacion" o como va eso..
    #TODO no de credencial vigente expedida por la UV de CIS... el verificador tiene una credencial especifica??
    posiblesriesgosimparcialidad = False
    #TODO campo de nombre y firma recibio se agrega a manita o va desde la seleccion de los contactos?
    class Meta:
        ordering=["fechacreacion"]
