from django.contrib import admin
from .models.Cotizacion import Cotizacion
from .models.ActaEvaluacionConformidad import ActaEvaualcionConformidad
from .models.ActaVerificacion import ActaVerificacion
from .models.Cliente import Cliente
from .models.Contacto import Contacto
from .models.Dictamen import Dictamen
from .models.Direccion import Direccion
from .models.Fc00 import Fc00
from .models.ItemPropuestaEconomica import ItemPropuestaEconomica
from .models.Norma import Norma
from .models.OrdenTrabajo import OrdenTrabajo
from .models.UnidadVerificacion import UnidadVerificacion
from .models.Verificador import Verificador

# Register your models here.
admin.site.register(ActaEvaualcionConformidad)
admin.site.register(ActaVerificacion)
admin.site.register(Cliente)
admin.site.register(Contacto)
admin.site.register(Cotizacion)
admin.site.register(Dictamen)
admin.site.register(Fc00)
admin.site.register(ItemPropuestaEconomica)
admin.site.register(Norma)
admin.site.register(OrdenTrabajo)
admin.site.register(UnidadVerificacion)
admin.site.register(Verificador)

