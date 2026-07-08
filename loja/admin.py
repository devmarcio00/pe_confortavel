from django.contrib import admin

from .models import Cliente, Produto


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'cidade', 'estado')
    search_fields = ('nome', 'email', 'cpf')


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nome', 'cor', 'preco_venda')
    search_fields = ('nome',)
