from django.db import models


class Cliente(models.Model):
    """Cliente da rede de lojas Pé Confortável."""

    ESTADO_CHOICES = [
        ('RJ', 'Rio de Janeiro'),
        ('SP', 'São Paulo'),
        ('MG', 'Minas Gerais'),
        ('ES', 'Espírito Santo'),
        ('PR', 'Paraná'),
        ('BA', 'Bahia'),
        ('RS', 'Rio Grande do Sul'),
    ]

    GENERO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outros'),
    ]

    CONTATO_CHOICES = [
        ('C', 'Carta'),
        ('E', 'E-mail'),
        ('T', 'Telefone'),
        ('F', 'Fax'),
    ]

    cpf = models.CharField('CPF', max_length=11)
    nome = models.CharField('Nome', max_length=70)
    endereco = models.CharField('Endereço', max_length=100)
    telefone = models.CharField('Telefone', max_length=11)
    estado = models.CharField('Estado de domicílio', max_length=2, choices=ESTADO_CHOICES)
    cidade = models.CharField('Cidade', max_length=50)
    genero = models.CharField('Gênero', max_length=1, choices=GENERO_CHOICES)
    contato = models.CharField('Forma de contato preferida', max_length=1, choices=CONTATO_CHOICES)
    email = models.EmailField('E-mail', max_length=100)
    username = models.CharField('Nome de usuário', max_length=100)
    senha = models.CharField('Senha (hash)', max_length=256)

    class Meta:
        ordering = ['nome']
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return f'{self.nome} ({self.email})'


class Produto(models.Model):
    """Produto (calçado) comercializado pela rede de lojas."""

    COR_CHOICES = [
        ('AZUL', 'Azul'),
        ('VERMELHO', 'Vermelho'),
        ('VERDE', 'Verde'),
        ('AMARELO', 'Amarelo'),
        ('BRANCO', 'Branco'),
        ('PRETO', 'Preto'),
        ('MARROM', 'Marrom'),
    ]

    codigo = models.AutoField('Código', primary_key=True)
    nome = models.CharField('Nome', max_length=70)
    preco_compra = models.FloatField('Preço de compra')
    preco_venda = models.FloatField('Preço de venda')
    cor = models.CharField('Cor', max_length=20, choices=COR_CHOICES)
    data_fabricacao = models.DateField('Data de Fabricação')
    imagem = models.CharField('Imagem', max_length=25)

    class Meta:
        ordering = ['nome']
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return f'{self.nome} (cód. {self.codigo})'

    @property
    def imagem_url(self):
        """Monta a URL da imagem do produto a partir do nome salvo na tabela."""
        from django.conf import settings
        if self.imagem:
            return f'{settings.MEDIA_URL}produtos/{self.imagem}'
        return ''
