# Create your models here.
from django.db import models

from SolicitacoesApp.utils import CHOICES_EQUIPE_CEAD, CHOICES_PARTICIPANTES
from .validators import validate_min_30, validate_data_futuro, validate_horario_agendamento, validate_nome_completo, validate_cpf

class ServicoProducaoDeMaterial(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class EquipamentoProducaoDeMaterial(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class ProducaoDeMaterial(models.Model):
    servicos = models.ManyToManyField('ServicoProducaoDeMaterial', blank=True, verbose_name='Serviços')
    outro = models.CharField(max_length=100, null=True, blank=True)
    
    professor_responsavel = models.CharField(max_length=100, verbose_name='Professor Responsável', validators=[validate_nome_completo])
    setor_curso = models.CharField(max_length=100, verbose_name="Setor Curso")
    email = models.EmailField(verbose_name="E-mail")
    telefone = models.CharField(max_length=20, blank=True, null=True)
    
    data_agendamento = models.DateField(verbose_name='Data de Agendamento', blank=True, null=True, validators=[validate_data_futuro])
    horario_agendamento = models.TimeField(verbose_name='Horário de Agendamento', blank=True, null=True, validators=[validate_horario_agendamento])
    duracao_estimada = models.CharField(max_length=20, verbose_name='Duração da Estimada', blank=True, null=True)
    data_entrega_material = models.DateField(verbose_name='Data de Entrega do Material', validators=[validate_data_futuro])
    
    finalidade_solicitacao = models.TextField(verbose_name='Finalidade da Solicitação', validators=[validate_min_30])
    arte_pronta = models.FileField(upload_to='arte_pronta/', null=True, blank=True, verbose_name='Arte para produção de material')
    detalhes_arte = models.TextField(verbose_name='Descreva sua arte aqui', blank=True, null=True)
    equipamentos = models.ManyToManyField('EquipamentoProducaoDeMaterial', blank=True)
    equipe_cead = models.BooleanField(verbose_name='Precisará de nossa equipe de cinegrafistas?', default=False, choices=CHOICES_EQUIPE_CEAD)
    numero_participantes = models.IntegerField(choices=CHOICES_PARTICIPANTES, verbose_name='Número de participantes', null=True, blank=True)
    observacao = models.TextField(verbose_name='Observações', blank=True, null=True)

    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Produção de Material-{self.professor_responsavel}"


class DadosDoPreposto(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, validators=[validate_cpf])
    rg = models.CharField(max_length=20)
    
    filiacao_1 = models.CharField(max_length=100)
    filiacao_2 = models.CharField(max_length=100, blank=True, null=True)
    
    banco = models.CharField(max_length=100)
    agencia = models.CharField(max_length=15)
    conta_corrente = models.CharField(max_length=15)
    
    preposto_logradouro = models.CharField(max_length=100)
    preposto_numero = models.IntegerField()
    preposto_complemento = models.CharField(max_length=100, blank=True, null=True)
    preposto_bairro = models.CharField(max_length=100)
    preposto_cidade = models.CharField(max_length=100)
    preposto_UF = models.CharField(max_length=2)

    def __str__(self):
        return self.nome

class DadosDaViagem(models.Model):
    logradouro = models.CharField(max_length=100)
    numero = models.IntegerField()
    complemento = models.CharField(max_length=100, blank=True, null=True)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    UF = models.CharField(max_length=2)

    data_saida = models.DateField(validators=[validate_data_futuro])
    horario_saida = models.TimeField()
    data_retorno = models.DateField(validators=[validate_data_futuro])
    horario_retorno = models.TimeField()
    
    objetivo_viagem = models.TextField(blank=False, null=False)
    outras_informacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.cidade    

class Viagens(models.Model):
    email = models.EmailField()
    curso = models.CharField(max_length=100)
    coordenador = models.CharField(max_length=100)

    preposto = models.ForeignKey(DadosDoPreposto, on_delete=models.SET_NULL, null=True)
    dados_da_viagem = models.ForeignKey(DadosDaViagem, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.curso

class SolicitacaoAlmoxarifadoGrafica(models.Model):
    solicitante = models.CharField(max_length=100)
    departamento_curso = models.CharField(max_length=100, verbose_name="Departamento/Curso")
    email = models.EmailField()
    data_criacao = models.DateField(auto_now=True, verbose_name="Data Criação")

class MaterialConsumo(models.Model):
    material_solicitado = models.CharField(max_length=100)
    quantidade = models.IntegerField()
    observacoes = models.TextField(null=True, verbose_name="Observações")
    solicitacao = models.ForeignKey(SolicitacaoAlmoxarifadoGrafica, on_delete=models.CASCADE, verbose_name="Solicitação")

class ImpressaoProvasApostilas(models.Model):
    arquivo = models.FileField(upload_to="arte_pronta")
    quantidade_provas_apostilas = models.IntegerField(verbose_name="Quantidade de Provas/Apostilas")
    separar_por_polos = models.BooleanField(default=False, verbose_name="Separar por Pólos?")
    localizacao_polo = models.CharField(max_length=100, null=True, verbose_name="Localização do Polo")
    observacoes = models.TextField(null=True, verbose_name="Observações")
    solicitacao = models.ForeignKey(SolicitacaoAlmoxarifadoGrafica, on_delete=models.CASCADE, verbose_name="Solicitação")

class CortePapel(models.Model):
    altura_papel_mm = models.IntegerField(verbose_name="Altura do Papel (mm)")
    largura_papel_mm = models.IntegerField(verbose_name="Largura do Papel(mm)")
    quantidade = models.IntegerField()
    observacoes = models.TextField(null=True, verbose_name="Observações")
    solicitacao = models.ForeignKey(SolicitacaoAlmoxarifadoGrafica, on_delete=models.CASCADE, verbose_name="Solicitação")        