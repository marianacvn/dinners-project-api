from django.contrib import admin

from .models import Cliente, Mesa, Pedido, Produto


@admin.register(Cliente)
class ClienteAdmin (admin.ModelAdmin):
    list_display = ['id', 'nomecliente', 'email']


@admin.register(Produto)
class ProdutoAdmin (admin.ModelAdmin):
    list_display = ['id', 'nomeproduto', 'descricaoproduto', 'preco', 'linkimagem']

@admin.register(Mesa)
class MesaAdmin (admin.ModelAdmin):
    list_display = ['id', 'statusmesa']


@admin.register(Pedido)
class PedidoAdmin (admin.ModelAdmin):

    list_display = ['id', 'mesa', 'cliente', 'get_produtos']


# Register your models here.
