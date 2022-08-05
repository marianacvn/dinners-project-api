from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Cliente, Mesa, Pedido, Produto

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nomecliente', 'email']


class ProdutoSerializer (serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ['id', 'nomeproduto', 'descricaoproduto', 'preco', 'linkimagem']

class MesaSerialize(serializers.ModelSerializer):
    class Meta:
        model = Mesa
        fields = ['id', 'statusmesa']


class PedidoSerialize (serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = ['id', 'mesa', 'cliente', 'produto']
