# Create your models here.
from django.db import models
from .validators import validate_professor_responsavel, validate_min_30


class ServicoProducaoDeMaterial(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class EquipamentoProducaoDeMaterial(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class ProducaoDeMaterial(models.Model):
   
    CHOICES_PARTICIPANTES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
    )
    
    servicos = models.ManyToManyField('ServicoProducaoDeMaterial', blank=True, verbose_name='Serviços')
    outro = models.CharField(max_length=100, null=True, blank=True)
    
    professor_responsavel = models.CharField(max_length=100, verbose_name='Professor Responsável', validators=[validate_professor_responsavel])
    setor_curso = models.CharField(max_length=100, verbose_name="Setor Curso")
    email = models.EmailField(verbose_name="E-mail")
    telefone = models.CharField(max_length=20, blank=True, null=True)
    
    data_agendamento = models.DateField(verbose_name='Data de Agendamento', blank=True, null=True)
    horario_agendamento = models.TimeField(verbose_name='Horário de Agendamento', blank=True, null=True)
    duracao_estimada = models.CharField(max_length=20, verbose_name='Duração da Estimada', blank=True, null=True)
    data_entrega_material = models.DateField(verbose_name='Data de Entrega do Material')
    
    finalidade_solicitacao = models.TextField(verbose_name='Finalidade da Solicitação', validators=[validate_min_30])
    arte_pronta = models.FileField(upload_to='arte_pronta/', null=True, blank=True, verbose_name='Arte para produção de material')
    detalhes_arte = models.TextField(verbose_name='Descreva sua arte aqui', blank=True, null=True)
    equipamentos = models.ManyToManyField('EquipamentoProducaoDeMaterial', blank=True)
    equipe_cead = models.BooleanField(verbose_name='Precisará de nossa equipe de cinegrafistas?', default=False)
    numero_participantes = models.IntegerField(choices=CHOICES_PARTICIPANTES, verbose_name='Número de participantes', null=True, blank=True)
    observacao = models.CharField(max_length=255, verbose_name='Observações', blank=True, null=True)

    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Produção de Material-{self.professor_responsavel}"