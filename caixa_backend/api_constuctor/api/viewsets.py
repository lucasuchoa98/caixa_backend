from rest_framework import viewsets
from api_constuctor.api import serializers
from api_constuctor import models

class ItemViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ItemSerializers
    queryset = models.Item.objects.all()

class VendaViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.VendaSerializers
    queryset = models.Item.objects.all()