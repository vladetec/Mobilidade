
from rest_framework import viewsets
from apps.cadastros.models import Onibus, Parada, Endereco
from .serializers import OnibusSerializer, ParadaSerializer, EnderecoSerializer


class OnibusViewSet(viewsets.ModelViewSet):

    queryset = Onibus.objects.all().order_by('numero')
    serializer_class = OnibusSerializer

class ParadaViewSet(viewsets.ModelViewSet):

    queryset = Parada.objects.all().order_by('numero')
    serializer_class = ParadaSerializer

class EnderecoViewSet(viewsets.ModelViewSet):

    queryset = Endereco.objects.all().order_by('bairro')
    serializer_class = EnderecoSerializer
