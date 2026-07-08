from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(max_length=11, verbose_name='CPF')),
                ('nome', models.CharField(max_length=70, verbose_name='Nome')),
                ('endereco', models.CharField(max_length=100, verbose_name='Endereço')),
                ('telefone', models.CharField(max_length=11, verbose_name='Telefone')),
                ('estado', models.CharField(choices=[('RJ', 'Rio de Janeiro'), ('SP', 'São Paulo'), ('MG', 'Minas Gerais'), ('ES', 'Espírito Santo'), ('PR', 'Paraná'), ('BA', 'Bahia'), ('RS', 'Rio Grande do Sul')], max_length=2, verbose_name='Estado de domicílio')),
                ('cidade', models.CharField(max_length=50, verbose_name='Cidade')),
                ('genero', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outros')], max_length=1, verbose_name='Gênero')),
                ('contato', models.CharField(choices=[('C', 'Carta'), ('E', 'E-mail'), ('T', 'Telefone'), ('F', 'Fax')], max_length=1, verbose_name='Forma de contato preferida')),
                ('email', models.EmailField(max_length=100, verbose_name='E-mail')),
                ('username', models.CharField(max_length=100, verbose_name='Nome de usuário')),
                ('senha', models.CharField(max_length=256, verbose_name='Senha (hash)')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False, verbose_name='Código')),
                ('nome', models.CharField(max_length=70, verbose_name='Nome')),
                ('preco_compra', models.FloatField(verbose_name='Preço de compra')),
                ('preco_venda', models.FloatField(verbose_name='Preço de venda')),
                ('cor', models.CharField(choices=[('AZUL', 'Azul'), ('VERMELHO', 'Vermelho'), ('VERDE', 'Verde'), ('AMARELO', 'Amarelo'), ('BRANCO', 'Branco'), ('PRETO', 'Preto'), ('MARROM', 'Marrom')], max_length=20, verbose_name='Cor')),
                ('data_fabricacao', models.DateField(verbose_name='Data de Fabricação')),
                ('imagem', models.CharField(max_length=25, verbose_name='Imagem')),
            ],
            options={
                'verbose_name': 'Produto',
                'verbose_name_plural': 'Produtos',
                'ordering': ['nome'],
            },
        ),
    ]
