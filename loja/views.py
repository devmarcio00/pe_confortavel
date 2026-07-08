import hashlib
import os

from django.conf import settings
from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import ClienteForm, ProdutoForm
from .models import Cliente, Produto


MAPA_CAMPOS_CLIENTE = {
    'cpfCliente': 'cpf',
    'nomeCliente': 'nome',
    'enderecoCliente': 'endereco',
    'telefoneCliente': 'telefone',
    'estadoCliente': 'estado',
    'cidadeCliente': 'cidade',
    'generoCliente': 'genero',
    'contatoCliente': 'contato',
    'emailCliente': 'email',
    'senhaCliente': 'senha_plana',
}

MAPA_CAMPOS_PRODUTO = {
    'nomeProduto': 'nome',
    'precoCompraProduto': 'preco_compra',
    'precoVendaProduto': 'preco_venda',
    'corProduto': 'cor',
    'dataFabricacaoProduto': 'data_fabricacao',
}

MAPA_ARQUIVO_PRODUTO = {
    'imagemProduto': 'arquivo_imagem',
}


def _remapear(querydict, mapa):
    """Cria uma copia do QueryDict trocando as chaves conforme o mapa."""
    novo = querydict.copy()
    for chave_html, chave_form in mapa.items():
        if chave_html in querydict:
            novo[chave_form] = querydict[chave_html]
    return novo


def index(request):
    """Pagina principal do site."""
    return render(request, 'loja/index.html')


def cliente_cadastro(request):
    """Cadastro de um novo Cliente."""
    if request.method == 'POST':
        dados = _remapear(request.POST, MAPA_CAMPOS_CLIENTE)
        form = ClienteForm(dados)
        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.username = cliente.email  # username = e-mail informado
            senha_plana = form.cleaned_data['senha_plana']
            cliente.senha = hashlib.sha256(senha_plana.encode('utf-8')).hexdigest()
            cliente.save()
            messages.success(request, 'Cliente cadastrado com sucesso!')
            return redirect('loja:cliente_lista')
    else:
        form = ClienteForm()
    return render(request, 'loja/cliente_form.html', {'form': form})


def cliente_lista(request):
    """Lista dos Clientes cadastrados."""
    clientes = Cliente.objects.all()
    return render(request, 'loja/cliente_list.html', {'clientes': clientes})


def produto_cadastro(request):
    """Cadastro de um novo Produto."""
    if request.method == 'POST':
        dados = _remapear(request.POST, MAPA_CAMPOS_PRODUTO)
        arquivos = _remapear(request.FILES, MAPA_ARQUIVO_PRODUTO)
        form = ProdutoForm(dados, arquivos)
        if form.is_valid():
            produto = form.save(commit=False)

            arquivo = form.cleaned_data['arquivo_imagem']
            pasta_produtos = os.path.join(settings.MEDIA_ROOT, 'produtos')
            os.makedirs(pasta_produtos, exist_ok=True)
            caminho_destino = os.path.join(pasta_produtos, arquivo.name)
            with open(caminho_destino, 'wb+') as destino:
                for chunk in arquivo.chunks():
                    destino.write(chunk)

            produto.imagem = arquivo.name
            produto.save()
            messages.success(request, 'Produto cadastrado com sucesso!')
            return redirect('loja:produto_lista')
    else:
        form = ProdutoForm()
    return render(request, 'loja/produto_form.html', {'form': form})


def produto_lista(request):
    """Lista dos Produtos cadastrados."""
    produtos = Produto.objects.all()
    return render(request, 'loja/produto_list.html', {'produtos': produtos})
