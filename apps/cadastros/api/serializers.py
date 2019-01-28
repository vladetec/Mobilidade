from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from apps.cadastros.models import Onibus, Parada, Endereco




class OnibusSerializer(ModelSerializer):

    class Meta:
        model = Onibus
        fields = (
            'id', 'numero', 'empresa', 'descricao')
        read_only_fields = ('numero', )

class ParadaSerializer(ModelSerializer):

    class Meta:
        model = Parada
        fields = (
            'id', 'numero', 'onibus', 'endereco', 'latitude', 'longitude')
        read_only_fields = ('numero', )

class EnderecoSerializer(ModelSerializer):

    class Meta:
        model = Endereco
        fields = (
            'id', 'uf', 'cidade', 'bairro', 'logradouro', 'pontoreferencia')
        read_only_fields = ('bairro', )