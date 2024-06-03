from rest_framework import serializers
from .models import TipoComida, Comida

class TipoComidaSerializer(serializer.ModelSerializer):
    
    class Meta:
        model = TipoComida
        fields = "__all__"

class ComidaSerializer(serializer.ModelSerializer):

    class Meta:
        model = Comida
        fields = "__all__"