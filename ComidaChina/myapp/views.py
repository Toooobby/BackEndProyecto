
from rest_framework import viewsets
from .models import TipoComida, Comida
from .serializers import TipoComidaSerializer, ComidaSerializer

# Create your views here.

class TipoComidaViewSet(viewsets.ModelViewSet):
    queryset = TipoComida.objects.all()
    serializer_class = TipoComidaSerializer

class ComidaViewSet(viewsets.ModelViewSet):
    queryset = Comida.objects.all()
    serializer_class = ComidaSerializer