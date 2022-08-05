from .models import Cliente, Mesa, Pedido, Produto
from .serializers import ClienteSerializer, MesaSerialize, PedidoSerialize, ProdutoSerializer
from rest_framework.generics import ListAPIView

class ClienteList(ListAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer



class ProdutoList(ListAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer


class MesaList(ListAPIView):
    queryset = Mesa.objects.all()
    serializer_class = MesaSerialize


class PedidoList(ListAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerialize