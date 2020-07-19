from rest_framework import serializers
from sgc.models.OrdenTrabajo import OrdenTrabajo

class OrdenTrabajoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False,allow_blank)