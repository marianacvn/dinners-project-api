
from django.db import models

# Create your models here.

class Cliente(models.Model):
    nomecliente = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    senha = models.CharField(max_length=500)

class Produto(models.Model):
    nomeproduto = models.CharField(max_length=100)
    descricaoproduto = models.CharField(max_length=200)
    preco = models.FloatField()
    quantidade = models.FloatField()
    linkimagem = models.CharField(max_length=4000)

class Mesa(models.Model):
    statusmesa = models.BooleanField(default=False)


class Pedido(models.Model):
    mesa = models.ForeignKey(Mesa, on_delete=models.SET_NULL, null=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)
    produto = models.ManyToManyField(Produto)

    def get_produtos(self):
        return "\n".join([str(p) for p in self.produto.all()])