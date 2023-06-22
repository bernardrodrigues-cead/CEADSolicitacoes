# Generated by Django 4.2.1 on 2023-06-21 15:20

import SolicitacoesApp.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DadosDaViagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logradouro', models.CharField(max_length=100)),
                ('numero', models.IntegerField()),
                ('complemento', models.CharField(blank=True, max_length=100, null=True)),
                ('bairro', models.CharField(max_length=100)),
                ('cidade', models.CharField(max_length=100)),
                ('UF', models.CharField(max_length=2)),
                ('data_saida', models.DateField()),
                ('data_retorno', models.DateField()),
                ('objetivo_viagem', models.CharField(max_length=200)),
                ('outras_informacoes', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DadosDoPreposto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=11, validators=[SolicitacoesApp.validators.validate_cpf])),
                ('rg', models.CharField(max_length=20)),
                ('filiacao_mae', models.CharField(max_length=100)),
                ('filiacao_pai', models.CharField(blank=True, max_length=100, null=True)),
                ('agencia', models.CharField(max_length=15)),
                ('conta_corrente', models.CharField(max_length=15)),
                ('banco', models.CharField(max_length=15)),
                ('logradouro', models.CharField(max_length=100)),
                ('numero', models.IntegerField()),
                ('complemento', models.CharField(blank=True, max_length=100, null=True)),
                ('bairro', models.CharField(max_length=100)),
                ('cidade', models.CharField(max_length=100)),
                ('UF', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='EquipamentoProducaoDeMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ServicoProducaoDeMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Viagens',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curso', models.CharField(max_length=100)),
                ('coordenador', models.CharField(max_length=100)),
                ('dados_da_viagem', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='SolicitacoesApp.dadosdaviagem')),
                ('preposto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='SolicitacoesApp.dadosdopreposto')),
            ],
        ),
        migrations.CreateModel(
            name='ProducaoDeMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('outro', models.CharField(blank=True, max_length=100, null=True)),
                ('professor_responsavel', models.CharField(max_length=100, validators=[SolicitacoesApp.validators.validate_nome_completo], verbose_name='Professor Responsável')),
                ('setor_curso', models.CharField(max_length=100, verbose_name='Setor Curso')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('telefone', models.CharField(blank=True, max_length=20, null=True)),
                ('data_agendamento', models.DateField(blank=True, null=True, validators=[SolicitacoesApp.validators.validate_data_futuro], verbose_name='Data de Agendamento')),
                ('horario_agendamento', models.TimeField(blank=True, null=True, validators=[SolicitacoesApp.validators.validate_horario_agendamento], verbose_name='Horário de Agendamento')),
                ('duracao_estimada', models.CharField(blank=True, max_length=20, null=True, verbose_name='Duração da Estimada')),
                ('data_entrega_material', models.DateField(validators=[SolicitacoesApp.validators.validate_data_futuro], verbose_name='Data de Entrega do Material')),
                ('finalidade_solicitacao', models.TextField(validators=[SolicitacoesApp.validators.validate_min_30], verbose_name='Finalidade da Solicitação')),
                ('arte_pronta', models.FileField(blank=True, null=True, upload_to='arte_pronta/', verbose_name='Arte para produção de material')),
                ('detalhes_arte', models.TextField(blank=True, null=True, verbose_name='Descreva sua arte aqui')),
                ('equipe_cead', models.BooleanField(choices=[(False, 'Não, iremos utilizar a nossa própria equipe'), (True, 'Sim, precisaremos da equipe do CEAD')], default=False, verbose_name='Precisará de nossa equipe de cinegrafistas?')),
                ('numero_participantes', models.IntegerField(blank=True, choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4')], null=True, verbose_name='Número de participantes')),
                ('observacao', models.TextField(blank=True, null=True, verbose_name='Observações')),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('equipamentos', models.ManyToManyField(blank=True, to='SolicitacoesApp.equipamentoproducaodematerial')),
                ('servicos', models.ManyToManyField(blank=True, to='SolicitacoesApp.servicoproducaodematerial', verbose_name='Serviços')),
            ],
        ),
    ]
