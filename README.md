# Pé Confortável Ltda. — Site (UC3)

Projeto Django com as funcionalidades de **Cliente** e **Produto**, conforme
especificação da atividade UC3.

## Estrutura

```
pe_confortavel/
├── manage.py
├── requirements.txt
├── pe_confortavel/        # configurações do projeto (settings, urls)
└── loja/                  # app com Cliente e Produto
    ├── models.py           # Cliente e Produto
    ├── forms.py            # validações das regras de negócio
    ├── views.py            # index, cadastro e lista de cada entidade
    ├── urls.py
    ├── admin.py
    ├── migrations/
    ├── templates/loja/     # index.html, *_form.html, *_list.html, base.html
    └── static/loja/        # css/style.css
```

## Como rodar

1. Crie e ative um ambiente virtual (recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Aplique as migrações (cria o banco SQLite com as tabelas de Cliente e Produto):
   ```bash
   python manage.py migrate
   ```

4. (Opcional) Crie um super usuário para acessar o /admin:
   ```bash
   python manage.py createsuperuser
   ```

5. Rode o servidor de desenvolvimento:
   ```bash
   python manage.py runserver
   ```

6. Acesse no navegador:
   - `http://127.0.0.1:8000/` — página inicial
   - `http://127.0.0.1:8000/clientes/` — lista de clientes
   - `http://127.0.0.1:8000/clientes/cadastro/` — cadastro de cliente
   - `http://127.0.0.1:8000/produtos/` — lista de produtos
   - `http://127.0.0.1:8000/produtos/cadastro/` — cadastro de produto

## Regras de negócio implementadas

- Todos os campos são obrigatórios (não aceitam vazio ou apenas espaços).
- Nome de usuário do cliente = e-mail informado (preenchido automaticamente).
- Senha do cliente deve ter exatamente 8 caracteres; é armazenada como hash
  SHA-256 (nunca em texto puro) na coluna `senha` (256 posições).
- Nome do cliente deve ter entre 25 e 70 caracteres.
- Estado de domicílio restrito a: RJ, SP, MG, ES, PR, BA, RS.
- CPF e telefone aceitam apenas números.
- E-mail validado pelo próprio `EmailField` do Django.
- Imagem do produto: o arquivo enviado é salvo em `media/produtos/` e o nome
  do arquivo é gravado no campo `imagem` do Produto; a URL da imagem é
  montada dinamicamente a partir desse nome (`Produto.imagem_url`).

## Observações sobre o front-end

- Bootstrap 5 (via CDN) é usado para o layout, cores, tabelas e formulários.
- Os elementos de formulário seguem o padrão de nomenclatura exigido:
  `idFrmXxxxXxxx`, `idTxtXxxxXxxx`, `idBSelXxxxXxxx`, `idRadXxxxXxxx`, etc.
  Como esses nomes não coincidem com os nomes dos campos dos models Django,
  as views fazem um pequeno remapeamento (`MAPA_CAMPOS_CLIENTE` /
  `MAPA_CAMPOS_PRODUTO` em `loja/views.py`) antes de validar os dados com o
  formulário Django.

## Observação importante

Este ambiente de geração de código não tem acesso à internet, então não foi
possível instalar o Django nem rodar `python manage.py runserver` ou
`makemigrations` para testar automaticamente. A migração inicial
(`loja/migrations/0001_initial.py`) foi escrita manualmente para refletir
exatamente os models. Rode `python manage.py migrate` no seu ambiente antes
de testar — se preferir, pode apagar essa migração e gerar a sua própria com
`python manage.py makemigrations`.
