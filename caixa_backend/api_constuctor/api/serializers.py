from rest_framework import serializers
from api_constuctor import models

class ItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Item
        fields = '__all__'

class VendaSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Venda
        fields = '__all__'