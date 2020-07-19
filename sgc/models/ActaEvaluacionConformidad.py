from django.db import models
from .OrdenTrabajo import OrdenTrabajo

class ActaEvaualcionConformidad(models.Model):
    class Meta:
        app_label = 'sgc'
    ordentrabajo = models.ForeignKey(OrdenTrabajo,on_delete=models.CASCADE)
    #TODO Aprobacion STPs meidante oficio______ de donde sale ese oficio?
    #TODO No, Acreditacion de donde sale ? tambien de Norma? para agregar esos campos en norma ... ?Quiza institucion , oficio y n acreditacion por norma?
    #TODO AEC de donde sa saca...
    fecha = models.DateTimeField()#TODO default para esta fecha
    #TODO la redaccion se saca a partir de la orden de trabajo o en que momento se obtiene "El C. qye actuo como verifiacdor de la UV CENTRO INTEGRAL DE SOLDADURA se constituyo en el blablabla"?
    # TODO oficio de comision de dode se saca?
    # TODO las lineas de los nombres o identificadoes de las areas a verificar quedan fijas desde la cotizacion tambien?
    # TODO no se podria generar el acta de evaluacion de la conformidad solamente como un reporte a entregar al usuario?
    # TODO LA guia de verificacion GV-N22 va fija por acta de evaluacion de la conformidad, por norma o como va?
    # TODO igual para "ELEMENTOS A VERIFICAR EV-22"
    
    # TODO Como se suele llevar control de esta fecha? no se podria enviar una notificacion periodica?
    fechaenvioelementosverificar = models.DateTimeField()
    #TODO medianteenvio hay opciones envio y recibido? o texto libre 
    medianteenvio = models.CharField(max_length=119)
    fechaconfirmado = models.DateTimeField()
    medianteconfirmado = models.CharField(max_length=119)
    #TODO ESTE  QUEDA A PARTIR DE LOS TESTIGOS PARA VER COMO SE ESTRUCTURAN LOS DATOS O VER SI SE PUEDE DEJAR COMO UN WIZARD DE LLENADO
