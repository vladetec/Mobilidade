from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from apps.cadastros.models import Onibus




class OnibusSerializer(ModelSerializer):

    class Meta:
        model = Onibus
        fields = (
            'id', 'numero', 'empresa', 'descricao')
        read_only_fields = ('numero', )

