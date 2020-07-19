from sgc.models.OrdenTrabajo import OrdenTrabajo
from sgc.serializers.OrdenTrabajoSerializer import OrdenTrabajoSerializer
from rest_framework import generics

class OrdenTrabajoList(generics.ListCreateAPIView):
    queryset = OrdenTrabajo.objects.all()
    serializer_class = OrdenTrabajoSerializer

class OrdenTrabajoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrdenTrabajo.objects.all()
    serializer_class = OrdenTrabajoSerializer
