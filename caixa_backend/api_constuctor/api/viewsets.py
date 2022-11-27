from rest_framework import viewsets
from api_constuctor.api import serializers
from api_constuctor import models

from rest_framework.permissions import AllowAny

class ItemViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ItemSerializers
    queryset = models.Item.objects.all()
    permission_classes = [AllowAny]

class VendaViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.VendaSerializers
    queryset = models.Item.objects.all()
    permission_classes = [AllowAny]