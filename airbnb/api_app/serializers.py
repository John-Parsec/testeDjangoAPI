from rest_framework import serializers
from api_app.models import Produto
from api_app.models import Nivel
from api_app.models import Relacao

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'

class NivelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nivel
        fields = '__all__'

class RelacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Relacao
        fields = '__all__'
