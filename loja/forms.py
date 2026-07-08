from django import forms
from django.core.exceptions import ValidationError

from .models import Cliente, Produto


def _campo_obrigatorio(valor, nome_campo):
    """Garante que um campo obrigatório não esteja vazio nem só com espaços."""
    if valor is None or str(valor).strip() == '':
        raise ValidationError(f'O campo {nome_campo} é obrigatório e não pode ficar em branco.')
    return str(valor).strip()


class ClienteForm(forms.ModelForm):
    
    senha_plana = forms.CharField(
        label='Senha',
        max_length=8,
        min_length=8,
        widget=forms.PasswordInput(render_value=False),
    )

    class Meta:
        model = Cliente
        fields = [
            'cpf', 'nome', 'endereco', 'telefone',
            'estado', 'cidade', 'genero', 'contato', 'email',
        ]

    def clean_cpf(self):
        cpf = _campo_obrigatorio(self.cleaned_data.get('cpf'), 'CPF')
        if not cpf.isdigit():
            raise ValidationError('O CPF deve conter apenas números.')
        if len(cpf) != 11:
            raise ValidationError('O CPF deve conter 11 dígitos.')
        return cpf

    def clean_telefone(self):
        telefone = _campo_obrigatorio(self.cleaned_data.get('telefone'), 'Telefone')
        if not telefone.isdigit():
            raise ValidationError('O telefone deve conter apenas números.')
        return telefone

    def clean_nome(self):
        nome = _campo_obrigatorio(self.cleaned_data.get('nome'), 'Nome')
        if not (25 <= len(nome) <= 70):
            raise ValidationError('O nome deve ter entre 25 e 70 caracteres.')
        return nome

    def clean_endereco(self):
        return _campo_obrigatorio(self.cleaned_data.get('endereco'), 'Endereço')

    def clean_cidade(self):
        return _campo_obrigatorio(self.cleaned_data.get('cidade'), 'Cidade')

    def clean_senha_plana(self):
        senha = self.cleaned_data.get('senha_plana', '')
        if senha.strip() == '':
            raise ValidationError('A senha é obrigatória.')
        if len(senha) != 8:
            raise ValidationError('A senha deve conter exatamente 8 caracteres.')
        return senha

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        # Regra de negócio: nome de usuário = e-mail informado
        if email:
            cleaned_data['username'] = email
        return cleaned_data


class ProdutoForm(forms.ModelForm):
    
    arquivo_imagem = forms.ImageField(label='Imagem do produto', required=True)

    class Meta:
        model = Produto
        fields = [
            'nome', 'preco_compra', 'preco_venda', 'cor', 'data_fabricacao',
        ]
        widgets = {
            'data_fabricacao': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_nome(self):
        return _campo_obrigatorio(self.cleaned_data.get('nome'), 'Nome')

    def clean_preco_compra(self):
        preco = self.cleaned_data.get('preco_compra')
        if preco is None:
            raise ValidationError('O preço de compra é obrigatório.')
        if preco <= 0:
            raise ValidationError('O preço de compra deve ser maior que zero.')
        return preco

    def clean_preco_venda(self):
        preco = self.cleaned_data.get('preco_venda')
        if preco is None:
            raise ValidationError('O preço de venda é obrigatório.')
        if preco <= 0:
            raise ValidationError('O preço de venda deve ser maior que zero.')
        return preco

    def clean_arquivo_imagem(self):
        arquivo = self.cleaned_data.get('arquivo_imagem')
        if arquivo and len(arquivo.name) > 25:
            raise ValidationError('O nome do arquivo de imagem deve ter no máximo 25 caracteres.')
        return arquivo
