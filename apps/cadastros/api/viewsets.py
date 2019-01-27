
from rest_framework import viewsets
from apps.cadastros.models import Onibus
from .serializers import OnibusSerializer


class OnibusViewSet(viewsets.ModelViewSet):

    queryset = Onibus.objects.all().order_by('numero')
    serializer_class = OnibusSerializer




