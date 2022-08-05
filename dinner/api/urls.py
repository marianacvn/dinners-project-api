from django.urls import path
from api import views

urlpatterns = [
    path('cliente/', views.ClienteList.as_view()),
    path('produto/', views.ProdutoList.as_view()),
    path('mesa/', views.MesaList.as_view()),
    path('pedido/', views.PedidoList.as_view()),
]