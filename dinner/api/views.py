from urllib import response
from .models import Cliente, Mesa, Pedido, Produto
from .serializers import ClienteSerializer, MesaSerialize, PedidoSerialize, ProdutoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ClienteList(APIView):
    

    def get(self, request):

        clientes = Cliente.objects.all()
        serializer = ClienteSerializer(clientes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ClienteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ProdutoList(APIView):
   

    def get(self, request):

        produtos = Produto.objects.all()
        serializer = ProdutoSerializer(produtos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProdutoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class MesaList(APIView):
    

    def get(self, request):

        mesas = Mesa.objects.all()
        serializer = MesaSerialize(mesas, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MesaSerialize(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class PedidoList(APIView):
    

    def get(self, request):

        pedidos = Pedido.objects.all()
        serializer = PedidoSerialize(pedidos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PedidoSerialize(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
