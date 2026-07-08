from django.urls import path

from . import views

app_name = 'loja'

urlpatterns = [
    path('', views.index, name='index'),
    path('clientes/cadastro/', views.cliente_cadastro, name='cliente_cadastro'),
    path('clientes/', views.cliente_lista, name='cliente_lista'),
    path('produtos/cadastro/', views.produto_cadastro, name='produto_cadastro'),
    path('produtos/', views.produto_lista, name='produto_lista'),
]
